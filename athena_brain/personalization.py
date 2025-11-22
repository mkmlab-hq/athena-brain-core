"""
Personalization Engine - Learns user style and preferences
"""

from typing import Dict, Any, Optional
from pathlib import Path
import json
from datetime import datetime


class PersonalizationEngine:
    """
    Learns user style and preferences for personalization
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize personalization engine
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.enable_mkm12 = self.config.get("enable_mkm12", True)
        self.learning_rate = self.config.get("learning_rate", 0.1)
        
        # Storage for user profiles
        self.profiles_file = Path.home() / ".athena" / "user_profiles.json"
        self.profiles_file.parent.mkdir(parents=True, exist_ok=True)
        self.profiles = self._load_profiles()
    
    def _load_profiles(self) -> Dict[str, Dict[str, Any]]:
        """Load user profiles from file"""
        if self.profiles_file.exists():
            try:
                with open(self.profiles_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_profiles(self):
        """Save user profiles to file"""
        try:
            with open(self.profiles_file, 'w', encoding='utf-8') as f:
                json.dump(self.profiles, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Failed to save profiles: {e}")
    
    def get_profile(self, user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get user profile
        
        Args:
            user_id: Optional user ID (default: "default")
            
        Returns:
            User profile
        """
        user_id = user_id or "default"
        
        if user_id not in self.profiles:
            self.profiles[user_id] = {
                "created": datetime.now().isoformat(),
                "preferences": {},
                "style": {},
                "constitution": None,
                "learning_data": []
            }
            self._save_profiles()
        
        return self.profiles[user_id]
    
    def update_preference(
        self,
        key: str,
        value: Any,
        user_id: Optional[str] = None
    ):
        """
        Update user preference
        
        Args:
            key: Preference key
            value: Preference value
            user_id: Optional user ID
        """
        user_id = user_id or "default"
        profile = self.get_profile(user_id)
        
        profile["preferences"][key] = value
        profile["last_updated"] = datetime.now().isoformat()
        
        self._save_profiles()
    
    def learn_style(
        self,
        style_data: Dict[str, Any],
        user_id: Optional[str] = None
    ):
        """
        Learn user style
        
        Args:
            style_data: Style data (e.g., coding style, writing style)
            user_id: Optional user ID
        """
        user_id = user_id or "default"
        profile = self.get_profile(user_id)
        
        # Merge style data
        for key, value in style_data.items():
            if key in profile["style"]:
                # Update with learning rate
                profile["style"][key] = (
                    profile["style"][key] * (1 - self.learning_rate) +
                    value * self.learning_rate
                )
            else:
                profile["style"][key] = value
        
        profile["last_updated"] = datetime.now().isoformat()
        self._save_profiles()

