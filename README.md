# Secure Cloud SSO Lab

A FastAPI service that signs users in with Microsoft Entra ID using OpenID Connect, deployed to AWS with Terraform and monitored with CloudWatch.

## The problem

Enterprises adopting AI tools need single sign-on, controlled user provisioning, audit logs and repeatable infrastructure before anything goes live. This lab builds that foundation end to end.

## Status

| Milestone | State |
|---|---|
| Repository, tests and CI | Done |
| OIDC login with Entra ID | Planned |
| Docker and AWS ECS Fargate via Terraform | Planned |
| CloudWatch logs and alarms | Planned |
| SCIM provisioning endpoint | Planned |
| SAML | Stretch goal |

## Planned stack

Python, FastAPI, Authlib, Microsoft Entra ID, Docker, AWS (ECS Fargate, ALB, ECR, RDS PostgreSQL, CloudWatch), Terraform, GitHub Actions, pytest.

## Run locally

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.txt
    python -m pytest -q
    uvicorn app.main:app --reload

## Author

Temi, [LinkedIn](https://www.linkedin.com/in/temi-oke/)
