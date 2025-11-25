# 🧠 Athena Brain Core

**Give your AI a brain that remembers and evolves**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/mkmlab-hq/athena-brain-core?style=social)](https://github.com/mkmlab-hq/athena-brain-core)

---

## 🎯 What is Athena Brain?

**Athena Brain** solves the fundamental limitations of large language models:

- ❌ **No long-term memory** - ChatGPT forgets everything after each conversation
- ❌ **No personalization** - Same answers for everyone
- ❌ **No evolution** - Repeats the same mistakes

**Athena Brain** gives any AI:

- 🧠 **Long-term memory** - Remembers everything, maintains project context
- 🔄 **Self-evolution** - Learns from mistakes, auto-generates rules
- 👤 **True personalization** - Understands your style, learns your preferences
- 🔒 **Privacy-first** - 100% local storage, your data stays on your computer

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/mkmlab-hq/athena-brain-core.git
cd athena-brain-core

# Install dependencies
pip install -r requirements.txt

# Initialize Athena Brain
python -m athena_brain init
```

### Basic Usage

```python
from athena_brain import AthenaBrain

# Initialize
brain = AthenaBrain()

# Store a memory
brain.store_memory(
    content="User prefers Python over JavaScript",
    category="preference"
)

# Search memories
results = brain.search_memory(
    query="What programming language does the user prefer?",
    limit=5
)

# Auto-evolution: Track mistakes and learn
brain.track_mistake(
    pattern="validation_error",
    solution="Always validate input before processing"
)
```

---

## ✨ Core Features

### 1. Long-term Memory (Local Qdrant)

- **Automatic conversation storage** - Every chat is saved
- **Semantic search** - Find relevant memories instantly
- **Project context** - Maintains context across sessions
- **100% local** - Your data never leaves your computer

### 2. Self-Evolution

- **Mistake pattern tracking** - Automatically detects repeated errors
- **Rule auto-generation** - Creates rules from mistakes
- **Continuous improvement** - Gets smarter every day

### 3. Personalization

- **Style learning** - Learns your coding style, preferences
- **Constitution-based analysis** (MKM12) - Understands your personality
- **Adaptive responses** - Tailored to you

### 4. Privacy-First

- **Local storage** - All data on your PC
- **Encryption** - AES-128-CBC + HMAC-SHA256
- **No cloud required** - Works completely offline

---

## 🏗️ Architecture

```
Athena Brain Core
├── Local Memory (Qdrant)
│   ├── Conversation storage
│   ├── Semantic search
│   └── Vector embeddings
├── Self-Evolution Engine
│   ├── Mistake tracking
│   ├── Rule generation
│   └── Continuous learning
├── Personalization Engine
│   ├── Style learning
│   ├── Preference tracking
│   └── Adaptive responses
└── AI Integration
    ├── ChatGPT API
    ├── Claude API
    ├── Gemini API
    └── Cursor (MCP)
```

---

## 🌐 Integration with MKM Life Ecosystem

**Athena Brain Core** is the open-source foundation for **Athena API** - the self-evolving memory system:

- **Athena API**: Cloud-based API service built on Athena Brain Core - [Learn More](https://mkmlife.com/api/athena)
- **Jema API**: Korean medicine intelligence API - [Learn More](https://mkmlife.com/api/jema)
- **Athena Search**: Real-time web search with domain filtering
- **B2B Private Box**: On-Premise LLM solutions for enterprises

**Platform**: [MKM Life](https://mkmlife.com) | **Developer Portal**: [A-Code AI](https://a-codeai.com)

---

## 🚀 Latest Features (2025)

- ✅ **Agentic RAG**: Intelligent query routing with LLM Router (Adaptive RAG)
- ✅ **GraphRAG**: Knowledge graph-based search for domain expertise
- ✅ **CRAG**: Corrective RAG for quality assurance and automatic fallback
- ✅ **Pattern Recognition**: FAST/MEDIUM/DEEP adaptive analysis paths
- ✅ **Emotion Tagging**: 5 emotion types (satisfaction, frustration, surprise, confusion, pride)
- ✅ **Neural Network Expansion**: Automatic memory connection creation and strengthening
- ✅ **MCP Integration**: 15+ MCP servers for enhanced AI capabilities

---

## 📋 Requirements

- Python 3.11+
- Qdrant (local or VPS)
- 4GB RAM minimum
- 10GB disk space

---

## 🔧 Configuration

Create `.athena/config.yaml`:

```yaml
memory:
  qdrant_url: "http://localhost:6333"
  collection_name: "athena_memories"
  
evolution:
  auto_track: true
  rule_threshold: 2
  
personalization:
  enable_mkm12: true
  learning_rate: 0.1
```

---

## 🎯 Use Cases

### For Developers

- **Project context** - AI remembers your entire project
- **Code style** - Learns your coding preferences
- **Mistake prevention** - Auto-generates rules from errors

### For Content Creators

- **Writing style** - Learns your voice and tone
- **Topic memory** - Remembers what you've written about
- **Preference learning** - Adapts to your needs

### For Everyone

- **Personal AI** - Truly understands you
- **Privacy** - Your data stays local
- **Evolution** - Gets smarter over time

---

## 🔗 Part of Athena Ecosystem

- **[Athena MCP Servers](https://github.com/mkmlab-hq/athena-mcp-servers)** - Essential MCP servers for Cursor IDE
- **[Cursor Advanced Rules](https://github.com/mkmlab-hq/cursor-advanced-rules)** - Optimized Cursor Rules system (6 essential rules)
- **[MKM12 Core Engine](https://github.com/mkmlab-hq/mkm12-core-engine)** - Constitutional analysis engine
- **[ICD Unified Model](https://github.com/mkmlab-hq/icd-unified-model)** - Causal AI framework
- **[A-Code AI](https://a-codeai.com)** - Developer portal for Jema API & Athena API
- **[MKM Life](https://mkmlife.com)** - Integrated health platform (Showroom + B2C)
- **[Persona Diary](https://personadiary.com)** - AI-powered diary generation with emotion analysis

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone and setup
git clone https://github.com/mkmlab-hq/athena-brain-core.git
cd athena-brain-core
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linter
black .
flake8 .
```

---

## 📊 Roadmap

- [x] Core memory system (Qdrant)
- [x] Self-evolution engine
- [x] Basic personalization
- [ ] Web dashboard
- [ ] Cloud sync (optional)
- [ ] Team collaboration
- [ ] Enterprise features

---

## 💰 Pricing

**Athena Brain Core**: Free forever (Open Source, MIT License)

**Athena Brain Cloud** (Coming Soon):
- Personal: $9.99/month
- Team: $49/month
- Enterprise: Custom pricing

[🚀 Join Waitlist for Cloud](https://athenabrain.ai/waitlist)

---

## 🔒 Privacy & Security

- **100% Local** - All data stored on your computer
- **Encryption** - AES-128-CBC + HMAC-SHA256
- **No Tracking** - We don't track you
- **Open Source** - Fully auditable

---

## 📚 Documentation

- [Full Documentation](https://docs.athenabrain.ai)
- [API Reference](https://docs.athenabrain.ai/api)
- [Examples](https://docs.athenabrain.ai/examples)
- [Athena API Documentation](https://mkmlife.com/api/athena) - Cloud API service
- [Jema API Documentation](https://mkmlife.com/api/jema) - Korean medicine intelligence API

---

## 🆘 Support

- 📧 Email: support@mkmlife.com
- 🌐 Developer Portal: [a-codeai.com](https://a-codeai.com)
- 🏥 Platform: [mkmlife.com](https://mkmlife.com)
- 🐛 Issues: [GitHub Issues](https://github.com/mkmlab-hq/athena-brain-core/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/mkmlab-hq/athena-brain-core/discussions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ™️ Trademark Notice

**Registered Trademarks:**
- "MKM Lab" ® - Registered trademark of MKM Lab
- "Persona Diary" ® - Registered trademark of MKM Lab

**Trademarks (In Use):**
- "Athena Brain", "Athena API", "Jema API", "MKM Life", "A-Code AI" 
  are trademarks of MKM Lab. All rights reserved.

**Important**: This license does not grant permission to use the trade names, 
trademarks, service marks, or product names of MKM Lab, except as required for 
reasonable and customary use in describing the origin of the Work.

---

## 🙏 Acknowledgments

- Built with [Qdrant](https://qdrant.tech/) for vector storage
- Powered by [sentence-transformers](https://www.sbert.net/) for embeddings
- Inspired by the need for AI that truly understands you

---

## ⭐ Star Us!

If you find Athena Brain useful, please star this repository! It helps us grow the community.

---

**Made with ❤️ by [MKM Lab](https://mkmlife.com)**

**Part of the MKM Life AI Ecosystem**

**© 2025 MKM Lab. All rights reserved.**

