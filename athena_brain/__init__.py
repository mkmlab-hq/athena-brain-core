"""
Athena Brain Core - Open-source AI memory and evolution system
"""

__version__ = "0.1.0"
__author__ = "MKM Lab"
__license__ = "MIT"

from .core import AthenaBrain
from .memory import MemoryManager
from .evolution import EvolutionEngine
from .personalization import PersonalizationEngine

__all__ = [
    "AthenaBrain",
    "MemoryManager",
    "EvolutionEngine",
    "PersonalizationEngine",
]

