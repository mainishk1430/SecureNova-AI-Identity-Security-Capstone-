SecureNova — AI Identity Security Capstone
Overview
This repository contains the five projects completed as part of the SecureNova AI Identity Security Capstone.

The capstone focuses on identifying, testing, and securing identity-related risks in AI-powered applications through threat modelling, IAM implementation, Red Team assessments, Blue Team controls, and security governance.

Project Portfolio
Project 1 — Threat Model the AI Identity System
Identifies human and non-human identities in the SecureNova AI platform and evaluates security threats using STRIDE, attack trees, risk prioritization, and MITRE ATLAS mapping.

Folder: 01-threat-model/

Project 2 — Build and Secure the Auth0-Backed AI Application
Implements Auth0-based authentication and authorization, OAuth 2.0, AI agent identity claims, MFA, attack protection, token validation, and SSO.

Folder: 02-iam-design/

Project 3 — Red Team: AI Identity Attacks
Evaluates AI identity security through simulated prompt injection, agent identity spoofing, system prompt extraction, RAG poisoning, and MCP abuse scenarios.

Folder: 03-red-team/

Project 4 — Blue Team: Guardrails, Hardening and Detection
Implements defensive controls including input/output guardrails, cryptographic identity verification, Auth0 hardening, anomaly detection, and before/after security comparisons.

Folder: 04-blue-team/

Project 5 — Policy, Compliance and Risk Management
Documents AI identity security governance, compliance mappings, incident response procedures, and risk-prioritized security recommendations.

Folder: 05-policy/

Repository Structure
SecureNova-AI-Identity-Security-Capstone/
│
├── 01-threat-model/
│   ├── diagrams/
│   └── screenshots/
│
├── 02-iam-design/
│   ├── app/
│   ├── scripts/
│   ├── screenshots/
│   └── README.md
│
├── 03-red-team/
│   ├── attacks/
│   ├── data/
│   ├── evidence/
│   ├── reports/
│   ├── screenshots/
│   └── README.md
│
├── 04-blue-team/
│   ├── anomaly_detection/
│   ├── auth0_hardening/
│   ├── comparison/
│   ├── cryptographic_identity/
│   ├── evidence/
│   ├── guardrails/
│   ├── reports/
│   ├── screenshots/
│   └── README.md
│
├── 05-policy/
│   ├── 01-ai-security-policy/
│   ├── 02-compliance-mapping/
│   └── 03-risk-matrix/
│
└── README.md
Technology Stack
Auth0
OAuth 2.0 and OpenID Connect
JWT
Python
Ed25519 Cryptography
AI Security Guardrails
Anomaly Detection
OWASP Top 10 for LLM Applications
MITRE ATLAS
NIST AI Risk Management Framework
Security and Documentation
Each project directory contains its relevant source files, documentation, reports, screenshots, or supporting evidence.

Sensitive credentials, private keys, access tokens, and environment-specific secrets must not be committed to this repository.

Capstone Outcome
The portfolio demonstrates an end-to-end approach to AI identity security:

Identify and model threats.
Build secure identity and access management.
Evaluate weaknesses through Red Team testing.
Implement defensive controls through Blue Team activities.
Establish governance, compliance, and risk management recommendations.