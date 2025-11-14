# Contributing to AI Chatbot Support Service

Thank you for your interest in contributing! This document provides guidelines and workflows for contributing to the project.

## Table of Contents

1. Code of Conduct
2. Getting Started
3. Development Workflow
4. Coding Standards
5. Testing Guidelines
6. Pull Request Process
7. Architecture Decisions

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## Getting Started

### Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/chatbot-support-service.git
cd chatbot-support-service
git remote add upstream https://github.com/original-org/chatbot-support-service.git
```

### Set Up Development Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pre-commit
pre-commit install
cp .env.example .env
```

### Run Tests

```bash
pytest
pytest --cov=. --cov-report=html
```

## Development Workflow

### Branch Naming Convention

- feature/<scope>-<short-description>
- fix/<scope>-<short-description>
- docs/<scope>-<short-description>

### Commit Message Guidelines

- Use imperative mood, e.g., "Add", "Fix", "Refactor"
- Reference issues with `#<id>` when applicable

### Pull Requests

- Keep PRs focused and small
- Include tests for new functionality
- Update documentation when needed

## Coding Standards

- Follow PEP 8 for Python
- Enforce linting via pre-commit hooks
- Ensure type hints where appropriate

## Testing Guidelines

- Write unit and integration tests
- Maintain test coverage thresholds
- Use fixtures for test data

## Architecture Decisions

- Record major changes in ADRs
- Discuss in issues before large refactors
