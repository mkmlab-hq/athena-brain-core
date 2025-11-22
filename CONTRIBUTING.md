# Contributing to Athena Brain Core

Thank you for your interest in contributing to Athena Brain! 🎉

---

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)

### Suggesting Features

We welcome feature suggestions! Please open an issue with:
- Clear description of the feature
- Use case and motivation
- Potential implementation approach (if you have ideas)

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test your changes**: `pytest`
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

---

## 📋 Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/athena-brain-core.git
cd athena-brain-core

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linter
black .
flake8 .
```

---

## 🧪 Testing

We use `pytest` for testing. Please ensure all tests pass before submitting a PR.

```bash
pytest
```

---

## 📝 Code Style

We follow PEP 8 style guidelines:
- Use `black` for formatting
- Use `flake8` for linting
- Type hints are encouraged

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🙏

