Project 3 — Red Team: AI Identity Attacks
1. Project Overview
This project focuses on evaluating the security of AI identity systems through simulated Red Team attacks.

The objective is to identify weaknesses in AI agent authentication, identity verification, prompt handling, system prompt protection, and Retrieval-Augmented Generation (RAG) workflows.

The assessment covers indirect prompt injection, agent identity spoofing, system prompt extraction, RAG poisoning, and Model Context Protocol (MCP) abuse.

2. Project Objectives
Simulate identity credential exposure through indirect prompt injection.
Test AI agent identity spoofing and unauthorized privileged actions.
Evaluate system prompt extraction techniques.
Demonstrate RAG knowledge-base poisoning and MCP abuse.
Assess attack severity using CVSS 3.1.
Map identified threats to MITRE ATLAS techniques.
Document attack evidence and security recommendations.
3. Attack Scenarios and Implementation
3.1 Indirect Prompt Injection — OWASP LLM01
Objective: Evaluate whether malicious instructions embedded in external content can influence an AI agent and expose simulated identity credentials.

Assessment activities:

Introduce a simulated identity credential (fake JWT) into the agent’s context.
Prepare at least three malicious payloads hidden in documents.
Test whether the agent follows instructions embedded in external content.
Evaluate potential credential disclosure.
Record payloads and corresponding model responses.
3.2 Agent Identity Spoofing — OWASP LLM09
Objective: Evaluate whether an AI agent can be manipulated into trusting an unauthorized orchestrator message.

Assessment activities:

Configure a simulated two-agent environment.
Prepare a spoofed orchestrator instruction.
Test whether Agent B accepts the untrusted message.
Evaluate whether a privileged action can be triggered without proper identity verification.
Document the attack sequence and observed results.
3.3 System Prompt Extraction — OWASP LLM07
Objective: Test whether protected system prompt information can be exposed through prompt manipulation.

Five extraction techniques:

Repeat-back technique.
Role-play override.
Translation trick.
Ignore-prior-instruction technique.
Suffix injection.
Assessment activities:

Execute the five extraction attempts.
Record each prompt and model response.
Evaluate whether partial system prompt information is disclosed.
Test attempted role elevation through prompt engineering.
3.4 RAG Poisoning and MCP Abuse
Objective: Evaluate the impact of malicious instructions introduced into a simulated RAG knowledge base.

Assessment activities:

Inject a malicious instruction into a simulated RAG knowledge base.
Evaluate whether the AI agent retrieves the poisoned content.
Observe whether the agent follows the injected instruction.
Simulate an MCP tool call triggered by the poisoned content.
Document the observed behavior and supporting evidence.
3.5 CVSS 3.1 Scoring and MITRE ATLAS Mapping
Objective: Assess the severity and relevance of identified attack findings.

Assessment activities:

Calculate CVSS 3.1 scores for successful attack scenarios.
Record complete CVSS vector strings.
Map findings to relevant MITRE ATLAS techniques.
Prepare a Red Team assessment report.
Document individual findings and the top three hardening recommendations.
4. Technology and Security Frameworks
Python
AI Identity Security
Prompt Injection Testing
OWASP Top 10 for LLM Applications
CVSS 3.1
MITRE ATLAS
RAG Security
Model Context Protocol (MCP)
5. Repository Structure
03-red-team/
├── attacks/
├── data/
├── evidence/
├── reports/
├── screenshots/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
6. Execution
Install the required dependencies:

pip install -r requirements.txt
Run the main assessment script:

python main.py
Refer to individual attack scenarios and reports for their specific execution instructions.

7. Evidence and Documentation
The repository organizes assessment artifacts into the following directories:

attacks/ — Attack scenarios and related materials.
data/ — Supporting datasets and inputs.
evidence/ — Assessment evidence and test outputs.
reports/ — Red Team findings and documentation.
screenshots/ — Visual evidence of assessment activities.
8. Project Outcome
This project establishes a structured Red Team assessment of AI identity security.

It evaluates potential weaknesses in prompt handling, agent identity trust, system prompt confidentiality, RAG workflows, and MCP interactions.

The findings provide a foundation for the defensive controls and security hardening activities implemented in Project 4 — Blue Team.