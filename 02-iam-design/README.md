Project 2 — Build and Secure the Auth0-Backed AI Application
1. Project Overview
This project focuses on building and securing an AI-powered application using Auth0 for identity and access management.

The objective is to implement secure authentication, authorization, token lifecycle management, Multi-Factor Authentication (MFA), and attack protection for human users and AI agents.

The application uses OAuth 2.0, JWT-based authentication, Auth0 Actions, and identity-aware access controls.

2. Objectives
Configure Auth0 applications for web and machine-to-machine communication.
Implement OAuth 2.0-based authentication and authorization.
Define custom API scopes for user-level and admin-level access.
Implement an AI agent identity using a custom agent_id JWT claim.
Configure TOTP-based Multi-Factor Authentication.
Enable brute-force protection and suspicious IP throttling.
Demonstrate short-lived token validation and credential rotation.
Configure Single Sign-On (SSO) between registered applications.
3. Implementation Details
3.1 Auth0 Tenant and Application Setup
Configured an Auth0 tenant.
Registered a Regular Web Application.
Registered a Machine-to-Machine (M2M) application.
Configured application authentication settings.
Registered the API used by the AI application.
3.2 OAuth 2.0 and Authorization
Implemented OAuth 2.0-based authentication and API authorization.

The project uses two custom authorization scopes:

read:ai-data — User-level access to AI data.
write:admin — Admin-level access to administrative operations.
JWT tokens are decoded and inspected to verify relevant claims, including:

aud
iss
exp
scope
agent_id
3.3 AI Agent Identity Using Auth0 Actions
Created an Auth0 post-login Action.
Added a custom agent_id claim to the authentication token.
Verified the custom claim in the decoded JWT.
Used identity information to support agent-aware authorization.
3.4 Multi-Factor Authentication (MFA)
Configured TOTP-based MFA.
Demonstrated MFA enrollment.
Tested the TOTP authentication challenge.
Applied additional authentication protection to user sign-in.
3.5 Attack Protection
Configured Auth0 security protections:

Brute-Force Protection.
Suspicious IP Throttling.
These controls help protect authentication endpoints against repeated login attempts and suspicious access patterns.

3.6 Credential Rotation and Token Validation
Implemented a Python-based token validation and credential rotation workflow.

The test demonstrates:

Obtaining an access token.
Making an authorized API request.
Receiving a successful 200 OK response.
Replaying an expired or invalidated token.
Receiving a 401 Unauthorized response.
Timestamped terminal output is maintained as supporting evidence.

3.7 Single Sign-On (SSO)
Configured two registered applications.
Tested successful authentication through the configured SSO flow.
Verified that the authenticated user could access the second application without repeating the full login process.
4. Technology Stack
Auth0
OAuth 2.0
OpenID Connect (OIDC)
JSON Web Tokens (JWT)
Python
TOTP-based MFA
Auth0 Actions
Google Social Login
REST APIs
5. Repository Structure
02-iam-design/
├── app/
├── scripts/
├── screenshots/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
6. Evidence and Screenshots
The screenshots/ directory contains implementation evidence covering:

Auth0 Applications dashboard showing Web and M2M applications.
Auth0 APIs page showing custom authorization scopes.
Decoded JWT displaying the agent_id claim.
Auth0 Universal Login custom branding.
MFA enrollment and TOTP challenge.
Auth0 Actions editor showing custom claim configuration.
Attack Protection settings showing Brute-Force Protection and Suspicious IP Throttling.
Terminal output showing successful 200 OK followed by 401 Unauthorized.
Additional SSO and authentication evidence.
7. Security Considerations
Sensitive credentials must not be committed to GitHub.
Environment-specific configuration should be maintained using environment variables.
.env.example should contain placeholders only.
Access tokens should be validated before protected API operations.
Application permissions should follow the principle of least privilege.
8. Project Outcome
This project demonstrates an Auth0-backed AI application with authentication, authorization, AI agent identity claims, MFA, attack protection, token validation, and SSO.

It establishes the identity and access management foundation for the subsequent Red Team and Blue Team security assessments in this capstone.