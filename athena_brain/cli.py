"""
CLI interface for Athena Brain
"""

import sys
import argparse
from pathlib import Path

from .core import AthenaBrain


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Athena Brain - AI memory and evolution system"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize Athena Brain")
    
    # Store command
    store_parser = subparsers.add_parser("store", help="Store a memory")
    store_parser.add_argument("content", help="Memory content")
    store_parser.add_argument("--category", default="general", help="Category")
    store_parser.add_argument("--tags", nargs="+", help="Tags")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search memories")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--limit", type=int, default=5, help="Limit results")
    search_parser.add_argument("--category", help="Category filter")
    
    # Track mistake command
    mistake_parser = subparsers.add_parser("track-mistake", help="Track a mistake")
    mistake_parser.add_argument("pattern", help="Mistake pattern")
    mistake_parser.add_argument("description", help="Description")
    mistake_parser.add_argument("solution", help="Solution")
    mistake_parser.add_argument("--category", default="general", help="Category")
    
    args = parser.parse_args()
    
    if args.command == "init":
        brain = AthenaBrain()
        brain.init()
    elif args.command == "store":
        brain = AthenaBrain()
        result = brain.store_memory(
            content=args.content,
            category=args.category,
            tags=args.tags or []
        )
        print(f"✅ {result.get('message', 'Memory stored')}")
    elif args.command == "search":
        brain = AthenaBrain()
        results = brain.search_memory(
            query=args.query,
            limit=args.limit,
            category=args.category
        )
        for i, result in enumerate(results, 1):
            print(f"\n{i}. Score: {result['score']:.3f}")
            print(f"   Content: {result['content'][:100]}...")
            print(f"   Category: {result['category']}")
    elif args.command == "track-mistake":
        brain = AthenaBrain()
        result = brain.track_mistake(
            pattern=args.pattern,
            description=args.description,
            solution=args.solution,
            category=args.category
        )
        print(f"✅ {result.get('message', 'Mistake tracked')}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

