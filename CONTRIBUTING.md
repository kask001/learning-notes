# Contributing

Thank you for your interest in contributing!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/project.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5. Install dependencies: `pip install -e ".[dev]"`

## Making Changes

1. Create a branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Add tests: `pytest tests/`
4. Format code: `black .` and `isort .`
5. Commit: `git commit -m "Add your feature"`

## Submitting

1. Push to your fork: `git push origin feature/your-feature`
2. Open a Pull Request on GitHub

## Coding Standards

- Follow PEP 8
- Add type hints
- Write docstrings
- Keep functions under 50 lines
- Test coverage > 80%
