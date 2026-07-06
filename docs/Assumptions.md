# Assumptions

## Purpose

This document lists the assumptions made during the design, development and testing of the Telecom AI NOC RAG Assistant.

These assumptions define the expected environment, available resources and project constraints for Version 1.0.

---

# Development Assumptions

The following assumptions were made during development:

- Python is installed on the development machine.
- Visual Studio Code is used as the development environment.
- Git is available for version control.
- Docker Desktop is installed for containerization.
- Internet connectivity is available.

---

# Azure Assumptions

The application assumes:

- An active Azure subscription is available.
- Azure OpenAI resources have been created.
- Chat and Embedding model deployments are available.
- Valid API credentials are configured.
- Required environment variables are correctly defined.

---

# Knowledge Base Assumptions

The project assumes:

- Telecom documents are available.
- Documents contain accurate technical information.
- Documents have been indexed successfully.
- ChromaDB contains valid vector embeddings.

---

# Application Assumptions

The application assumes:

- FastAPI starts successfully.
- Dependencies are installed correctly.
- Environment variables are available.
- Required Python packages are compatible.

---

# User Assumptions

The intended user is expected to have:

- Basic telecom knowledge.
- Basic understanding of REST APIs.
- Access to Swagger UI.
- Permission to use Azure OpenAI resources.

---

# Deployment Assumptions

The deployment environment assumes:

- Docker is available (if using containers).
- Required network ports are available.
- Azure OpenAI services are accessible.
- Internet connectivity is available.

---

# Security Assumptions

The project assumes:

- API keys remain confidential.
- The `.env` file is excluded from GitHub.
- No sensitive customer data is stored in the knowledge base.
- Users follow standard security practices.

---

# Limitations

The current project assumes a single-user portfolio environment.

The following are outside the scope of Version 1.0:

- Enterprise authentication
- High availability
- Auto scaling
- Multi-user collaboration
- Production monitoring

---

# Key Takeaways

- The project assumes a correctly configured development environment.
- Azure OpenAI resources must be available.
- Telecom documents must be indexed before use.
- Docker is optional but recommended.
- The assumptions support a simple, maintainable portfolio project.