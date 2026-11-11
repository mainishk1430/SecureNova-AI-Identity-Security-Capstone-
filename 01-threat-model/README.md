Project 1 – Threat Model of the AI Identity System
Organization: SecureNova Inc.
Capstone: QC_AI Identity Security
Project: 1 – Threat Model the AI Identity System
Assessment Area: AI Identity Security and Threat Modelling

1. Project Overview
This project focuses on identifying and analysing security risks within the SecureNova AI platform. The main objective is to understand how human and non-human identities interact with the platform, identify potential attack paths, and assess the risks associated with those interactions.

The assessment uses OWASP Threat Dragon, STRIDE threat modelling, attack tree analysis, risk scoring, and MITRE ATLAS mapping to create a structured view of the platform's security risks.

2. Identity Inventory
The SecureNova AI platform includes six identity types:

Identity	Description
Human User	A user accessing the AI customer service platform
AI Agent	An automated agent performing AI-related tasks
OAuth M2M Client	A machine-to-machine client requesting API access
LLM API Key	A credential used to authenticate with the LLM service
RAG Pipeline Service Identity	A service identity used by the retrieval-augmented generation pipeline
MCP Server Identity	An identity associated with the Model Context Protocol server
For each identity, the threat modelling exercise considers its authentication mechanism, access permissions, and privilege level.

3. Data-Flow Diagram and Trust Boundaries
An AI identity data-flow diagram was created using OWASP Threat Dragon.

The diagram represents the main components and interactions within the SecureNova AI platform, including:

Human User

AI Agent

OAuth M2M Client

RAG Processing Service

Vector Store

Internal API Service

Trust boundaries are used to distinguish the user, agent, and internal service layers. The diagram helps identify where sensitive information and identity credentials move between components.

Evidence: screenshots/01_Threat_Dragon_Data_Flow.png

4. STRIDE Threat Analysis
The STRIDE methodology is used to identify potential threats across the platform's identity flows.

The six STRIDE categories are:

Spoofing: Impersonation of a legitimate user, agent, or service.

Tampering: Unauthorized modification of data or requests.

Repudiation: Lack of reliable evidence to establish accountability.

Information Disclosure: Exposure of sensitive information or credentials.

Denial of Service: Disruption of platform or service availability.

Elevation of Privilege: Gaining access beyond the permissions assigned to an identity.

Potential threats and recommended mitigations are documented in the STRIDE analysis.

Evidence:

screenshots/02_Threat_Dragon_Stride_Threats.png

screenshots/06_Stride_Threat_Matrix.png

5. Attack Tree Analysis
Three attack trees were developed to examine how an attacker could target the AI identity ecosystem.

5.1 Attack Tree 1 – LLM API Key Exfiltration
This attack tree examines how an attacker could use prompt injection to influence an AI agent and expose an LLM API key.

Risk assessment: Likelihood 4 × Impact 5 = 20 (Critical)

5.2 Attack Tree 2 – Agent Identity Spoofing
This scenario explores how an attacker could impersonate an AI agent, exploit identity-related weaknesses, and obtain unauthorized API access or elevated permissions.

Risk assessment: Likelihood 4 × Impact 5 = 20 (Critical)

5.3 Attack Tree 3 – RAG Chunk Poisoning
This attack tree examines how malicious or manipulated content could be introduced into the RAG knowledge source and influence the AI agent's behaviour.

Risk assessment: Likelihood 3 × Impact 5 = 15 (High)

The attack trees use a structured sequence of steps to show how each attack objective could be achieved.

Evidence:

diagrams/Attack Tree 1 - LLM API Key Exfiltration.drawio

diagrams/Attack Tree 2 - Agent Identity Spoofing.drawio

diagrams/Attack Tree 3 - RAG Chunk Poisoning.drawio

screenshots/03_Attack_Tree_key_Exfiltration.png

screenshots/04_Attack_Tree_Agent_Identity_Spoofing.png

screenshots/05_Attack_Tree_RAG_Chunk_Poisoning.png

6. Risk Register
A risk register was prepared to record and prioritize the identified threats.

The register includes:

Risk register ID

Threat description

Likelihood

Impact

Risk score

Risk level

Assigned owner

Risk ranking

The risk score is calculated using:

Risk Score = Likelihood × Impact

Ten threats are included in the risk register and ranked according to their calculated risk scores. This helps identify which security issues require the most attention.

Evidence: screenshots/07_Risk_Register.png

7. MITRE ATLAS Mapping
The identified attack scenarios are related to relevant techniques in the MITRE ATLAS knowledge base.

The mapping helps connect the project's attack paths with documented adversarial techniques targeting AI and machine learning systems.

The submitted evidence includes the MITRE ATLAS LLM Prompt Injection technique page.

Mapped technique shown in evidence: AML.T0051 – LLM Prompt Injection

Evidence: screenshots/08_MITRE_ATLAS_Technique.png

8. Project Artifacts
Diagrams
SecureNova AI Identity Threat Model.json

Attack Tree 1 - LLM API Key Exfiltration.drawio

Attack Tree 2 - Agent Identity Spoofing.drawio

Attack Tree 3 - RAG Chunk Poisoning.drawio

Screenshots
The screenshots/ directory contains the following evidence in the sequence specified by the capstone instructions:

OWASP Threat Dragon – Complete Data-Flow Diagram

Threat Dragon – STRIDE Threat Panel

Attack Tree 1 – LLM API Key Exfiltration

Attack Tree 2 – Agent Identity Spoofing

Attack Tree 3 – RAG Chunk Poisoning

STRIDE Threat Matrix

Risk Register

MITRE ATLAS Technique Mapping

9. Project Outcome
This project establishes a structured understanding of the identity-related risks affecting the SecureNova AI platform.

The data-flow diagram, STRIDE analysis, attack trees, and risk register provide a foundation for the subsequent projects covering IAM implementation, red team testing, blue team security controls, and compliance assessment.

Project Status: Threat modelling artifacts and evidence prepared.