# OWASP LLM Top 10 & MITRE ATLAS Vulnerability Lab

A comprehensive security testing lab demonstrating OWASP Top 10 for Large Language Models and MITRE ATLAS framework vulnerabilities.

## Overview

This project provides a hands-on learning environment for understanding and testing LLM security vulnerabilities including:

- **OWASP Top 10 for LLMs**: Prompt Injection, Insecure Output, Training Data Poisoning, Model DoS, Supply Chain, Sensitive Disclosure, Excessive Agency, Overreliance, Model Theft
- **MITRE ATLAS Framework**: Adversarial tactics and techniques for machine learning systems
- **CWE Mappings**: Common Weakness Enumeration mappings

## Project Structure

```
owasp-llm-mitre-atlas-vuln-lab/
├── app/               # Main application and vulnerable implementations
├── tests/             # Security test cases
├── data/              # Training and inference data
└── docs/              # Documentation and mappings
```

## Getting Started

### Prerequisites

- Python 3.9+
- Docker & Docker Compose
- OpenAI API Key (for testing)

### Installation

```bash
# Clone the repository
cd owasp-llm-mitre-atlas-vuln-lab

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
```

### Running with Docker

```bash
docker-compose up -d
```

## Vulnerabilities Covered

1. **LLM01: Prompt Injection** - Input validation and prompt engineering attacks
2. **LLM02: Insecure Output Handling** - Output validation and sanitization
3. **LLM03: Training Data Poisoning** - Data integrity and verification
4. **LLM04: Model DoS** - Resource exhaustion and rate limiting
5. **LLM05: Supply Chain Vulnerabilities** - Dependency management
6. **LLM06: Sensitive Information Disclosure** - Data leakage prevention
7. **LLM07: Insecure Plugin Design** - Plugin security implementation
8. **LLM08: Excessive Agency** - Model autonomy and boundaries
9. **LLM09: Overreliance** - Human-in-the-loop mechanisms
10. **LLM10: Model Theft** - Model security and IP protection

## Testing

```bash
# Run all tests
pytest

# Run specific vulnerability tests
pytest tests/test_llm01_prompt_injection.py
```

## Documentation

- [OWASP LLM Mapping](docs/OWASP_LLM_Mapping.md)
- [MITRE ATLAS Mapping](docs/MITRE_ATLAS_Mapping.md)
- [CWE Mapping](docs/CWE_Mapping.md)

## License

MIT License
