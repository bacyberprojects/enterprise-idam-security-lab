# EMP009 — IAM Mover Risk Assessment

## Organisation
Southern Cross Financial Services (SCFS)

## Employee
Lucas Martin (EMP009)

## Scenario
Lucas Martin has transferred from Operations Officer
to Customer Service Officer.

The role transfer and HR confirmation are simulated.

## Risk Identification
EMP009 retains Read/Write access to the Operations System,
which is not authorised for the new role.

This creates a privilege creep and least-privilege risk.

EMP009 also has insufficient CRM access for the new role.

## Potential Business Impact
- Unauthorised access to operational information
- Unauthorised modification of operational records
- Increased risk of accidental or deliberate misuse
- Failure to enforce least privilege
- Potential audit and compliance findings

No actual misuse has been identified in this simulation.

## Inherent Risk Assessment
Likelihood: 4 — Likely
Impact: 4 — Major

Risk Score: 4 x 4 = 16
Risk Rating: High

These ratings are illustrative and require risk-owner validation.

## Recommended Controls
1. Obtain simulated manager and application-owner approvals.
2. Remove Operations System access.
3. Change CRM access from Read to Read/Write.
4. Verify permissions against the approved RBAC matrix.
5. Record remediation evidence.
6. Obtain risk-owner acceptance before formal closure.

## Proposed Residual Risk
Likelihood: 2 — Unlikely
Impact: 4 — Major

Residual Risk Score: 2 x 4 = 8
Residual Risk Rating: Medium

The residual rating is a forecast, not a verified outcome.

## Current Status
Open — Awaiting simulated approvals and remediation.

## Lab Disclaimer
This assessment uses fictional employee records,
simulated permissions, and hypothetical risk ratings.
No production systems are accessed or modified.