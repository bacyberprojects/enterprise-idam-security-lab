# Enterprise Identity and Access Management (IAM) Security Lab

## Project Overview

This project simulates Identity and Access Management (IAM) security operations for a fictional Australian financial services organisation, **Southern Cross Financial Services (SCFS)**.

The objective is to demonstrate how a cybersecurity analyst identifies, investigates, assesses and remediates identity-related security risks using role-based access control (RBAC), least privilege and joiner-mover-leaver (JML) processes.

The lab uses fictional employee records, simulated identity accounts, application permissions and Python-based access reviews.

## Security Capabilities Demonstrated

- Identity and Access Management (IAM/IDAM)
- Role-Based Access Control (RBAC)
- Principle of Least Privilege
- Joiner-Mover-Leaver (JML) lifecycle management
- Access reviews and privilege creep detection
- Identity account and session risk assessment
- Risk assessment and risk registers
- Simulated access remediation and verification
- Security investigation documentation and audit evidence

## Lab Environment

| Component | Purpose |
|---|---|
| Python | Automated IAM access-review checks |
| CSV datasets | Fictional HR, permissions, identity account and session records |
| RBAC matrix | Defines approved application permissions by job role |
| Risk register | Documents identified IAM security risks |
| Investigation reports | Records findings, analysis and recommended controls |
| Evidence files | Preserves before-and-after simulated remediation results |
| GitHub | Version control and project documentation |

## IAM Security Investigations

### EMP005 — Excessive Privileged Access

Investigated an employee with excessive administrative permissions.

Demonstrated RBAC validation, least-privilege assessment, simulated remediation and verification.

### EMP008 — Terminated Employee Retaining Access

Investigated a terminated employee who retained application access and an enabled identity account with active session and refresh-token records.

Demonstrated leaver risk assessment, simulated account disablement, session and token revocation, and post-remediation verification.

### EMP009 — Employee Role Transfer

Investigated an employee transferring from Operations Officer to Customer Service Officer.

Identified unnecessary Operations System access and insufficient CRM permissions.

Simulated removal of previous-role access, adjustment of CRM permissions, HR record reconciliation and RBAC verification.

## Running the IAM Access Review

From the repository root, execute:

```bash
python3 lab/scripts/iam_access_review.py
```

The script reviews fictional employee and access datasets and produces findings requiring analyst validation.

The latest simulated review reported 50 employees, 58 permission assignments and one remaining EMP009 mover-review finding.

## Project Structure

- `docs/` — IAM governance documents, RBAC matrix and risk register
- `lab/data/` — Fictional employee, permission, account and session datasets
- `lab/scripts/` — Python access-review script
- `lab/investigations/` — IAM security investigation records
- `lab/remediation/` — Simulated remediation documentation
- `lab/evidence/` — Verification outputs and audit evidence

## Security Governance

The project demonstrates risk-based decision-making and evidence-based access reviews.

Technical remediation, analyst validation and formal risk-owner acceptance are treated as separate activities.

Some investigation closure and residual-risk acceptance steps remain pending in the simulated scenarios.

## Important Disclaimer

**This is a fictional cybersecurity training and portfolio project.**

All employee identities, permissions, HR confirmations, approvals, identity sessions and remediation actions are simulated.

The project does not connect to Microsoft Entra ID or any production identity provider, and no real employee accounts or systems are modified.

The Python review results validate the fictional datasets; they do not prove enforcement of access changes in a live environment.
