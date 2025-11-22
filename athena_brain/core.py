"""
Athena Brain Core - Main interface
"""

from typing import Optional, List, Dict, Any
from pathlib import Path
import os

from .memory import MemoryManager
from .evolution import EvolutionEngine
from .personalization import PersonalizationEngine


class AthenaBrain:
    """
    Main Athena Brain interface
    
    Usage:
        brain = AthenaBrain()
        brain.store_memory(content="User prefers Python", category="preference")
        results = brain.search_memory(query="What does user prefer?")
    """
    
    def __init__(
        self,
        config_path: Optional[str] = None,
        qdrant_url: Optional[str] = None,
        collection_name: str = "athena_memories"
    ):
        """
        Initialize Athena Brain
        
        Args:
            config_path: Path to config file (default: .athena/config.yaml)
            qdrant_url: Qdrant URL (default: http://localhost:6333)
            collection_name: Collection name for memories
        """
        # Load config
        if config_path is None:
            config_path = Path.home() / ".athena" / "config.yaml"
        
        self.config_path = Path(config_path)
        self.config = self._load_config()
        
        # Initialize components
        qdrant_url = qdrant_url or self.config.get("memory", {}).get("qdrant_url", "http://localhost:6333")
        
        self.memory = MemoryManager(
            qdrant_url=qdrant_url,
            collection_name=collection_name
        )
        
        self.evolution = EvolutionEngine(
            config=self.config.get("evolution", {})
        )
        
        self.personalization = PersonalizationEngine(
            config=self.config.get("personalization", {})
        )
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        import yaml
        
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        
        # Default config
        return {
            "memory": {
                "qdrant_url": "http://localhost:6333",
                "collection_name": "athena_memories"
            },
            "evolution": {
                "auto_track": True,
                "rule_threshold": 2
            },
            "personalization": {
                "enable_mkm12": True,
                "learning_rate": 0.1
            }
        }
    
    def store_memory(
        self,
        content: str,
        category: str = "general",
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Store a memory
        
        Args:
            content: Memory content
            category: Category (e.g., "preference", "project", "conversation")
            tags: Optional tags
            metadata: Optional metadata
            
        Returns:
            Storage result
        """
        return self.memory.store(
            content=content,
            category=category,
            tags=tags or [],
            metadata=metadata or {}
        )
    
    def search_memory(
        self,
        query: str,
        limit: int = 5,
        category: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Search memories
        
        Args:
            query: Search query
            limit: Maximum results
            category: Optional category filter
            
        Returns:
            List of matching memories
        """
        return self.memory.search(
            query=query,
            limit=limit,
            category=category
        )
    
    def track_mistake(
        self,
        pattern: str,
        description: str,
        solution: str,
        category: str = "general",
        threshold: int = 2
    ) -> Dict[str, Any]:
        """
        Track a mistake pattern for auto-evolution
        
        Args:
            pattern: Mistake pattern identifier
            description: Description of the mistake
            solution: Solution to the mistake
            category: Category (e.g., "critical", "mcp", "general")
            threshold: Threshold for rule generation
            
        Returns:
            Tracking result
        """
        return self.evolution.track_mistake(
            pattern=pattern,
            description=description,
            solution=solution,
            category=category,
            threshold=threshold
        )
    
    def get_personalization(self, user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get personalization data
        
        Args:
            user_id: Optional user ID
            
        Returns:
            Personalization data
        """
        return self.personalization.get_profile(user_id)
    
    def init(self):
        """Initialize Athena Brain (first-time setup)"""
        # Create config directory
        config_dir = self.config_path.parent
        config_dir.mkdir(parents=True, exist_ok=True)
        
        # Save default config
        import yaml
        with open(self.config_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, default_flow_style=False)
        
        # Initialize Qdrant
        self.memory.init_collection()
        
        print("✅ Athena Brain initialized successfully!")
        print(f"📁 Config: {self.config_path}")
        print(f"🧠 Memory: {self.memory.qdrant_url}")

