"""
Memory Manager - Long-term memory system using Qdrant
"""

from typing import List, Dict, Any, Optional
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
import uuid
from datetime import datetime


class MemoryManager:
    """
    Manages long-term memory using Qdrant vector database
    """
    
    def __init__(
        self,
        qdrant_url: str = "http://localhost:6333",
        collection_name: str = "athena_memories"
    ):
        """
        Initialize memory manager
        
        Args:
            qdrant_url: Qdrant server URL
            collection_name: Collection name
        """
        self.qdrant_url = qdrant_url
        self.collection_name = collection_name
        
        # Initialize Qdrant client
        self.client = QdrantClient(url=qdrant_url)
        
        # Initialize embedding model
        try:
            self.embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            self.embedding_dimension = 384
        except Exception as e:
            print(f"⚠️ Failed to load embedding model: {e}")
            self.embedding_model = None
            self.embedding_dimension = 384
    
    def init_collection(self):
        """Initialize Qdrant collection"""
        try:
            # Check if collection exists
            collections = self.client.get_collections()
            collection_names = [c.name for c in collections.collections]
            
            if self.collection_name not in collection_names:
                # Create collection
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(
                        size=self.embedding_dimension,
                        distance=Distance.COSINE
                    )
                )
                print(f"✅ Created collection: {self.collection_name}")
            else:
                print(f"✅ Collection already exists: {self.collection_name}")
        except Exception as e:
            print(f"❌ Failed to initialize collection: {e}")
            raise
    
    def store(
        self,
        content: str,
        category: str = "general",
        tags: List[str] = None,
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Store a memory
        
        Args:
            content: Memory content
            category: Category
            tags: Tags
            metadata: Additional metadata
            
        Returns:
            Storage result
        """
        try:
            # Generate embedding
            if self.embedding_model:
                embedding = self.embedding_model.encode(content).tolist()
            else:
                # Fallback: simple hash-based vector
                import hashlib
                hash_obj = hashlib.md5(content.encode())
                embedding = [float(int(hash_obj.hexdigest()[i:i+2], 16)) / 255.0 for i in range(0, min(384, len(hash_obj.hexdigest()), 2))]
                embedding = embedding + [0.0] * (384 - len(embedding))
            
            # Create point
            point_id = str(uuid.uuid4())
            point = PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "content": content,
                    "category": category,
                    "tags": tags or [],
                    "metadata": metadata or {},
                    "timestamp": datetime.now().isoformat()
                }
            )
            
            # Store in Qdrant
            self.client.upsert(
                collection_name=self.collection_name,
                points=[point]
            )
            
            return {
                "success": True,
                "id": point_id,
                "message": "Memory stored successfully"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def search(
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
        try:
            # Generate query embedding
            if self.embedding_model:
                query_embedding = self.embedding_model.encode(query).tolist()
            else:
                # Fallback
                import hashlib
                hash_obj = hashlib.md5(query.encode())
                query_embedding = [float(int(hash_obj.hexdigest()[i:i+2], 16)) / 255.0 for i in range(0, min(384, len(hash_obj.hexdigest()), 2))]
                query_embedding = query_embedding + [0.0] * (384 - len(query_embedding))
            
            # Build filter
            query_filter = None
            if category:
                from qdrant_client.models import Filter, FieldCondition, MatchValue
                query_filter = Filter(
                    must=[
                        FieldCondition(
                            key="category",
                            match=MatchValue(value=category)
                        )
                    ]
                )
            
            # Search
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
                query_filter=query_filter
            )
            
            # Format results
            memories = []
            for result in results:
                memories.append({
                    "id": result.id,
                    "score": result.score,
                    "content": result.payload.get("content", ""),
                    "category": result.payload.get("category", ""),
                    "tags": result.payload.get("tags", []),
                    "metadata": result.payload.get("metadata", {}),
                    "timestamp": result.payload.get("timestamp", "")
                })
            
            return memories
        except Exception as e:
            print(f"❌ Search failed: {e}")
            return []

