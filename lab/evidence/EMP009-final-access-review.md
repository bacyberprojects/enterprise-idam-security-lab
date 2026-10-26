# EMP009 — Final IAM Mover Access Review

## Organisation
Southern Cross Financial Services (SCFS)

## Employee Details
- Employee ID: EMP009
- Employee Name: Lucas Martin
- Previous Role: Operations Officer
- New Role: Customer Service Officer
- Employment Status: Transferred
- HR Confirmation: Simulated

## 1. Investigation Summary

EMP009 was identified during the automated IAM access review
because the employee had transferred roles.

The investigation identified two access issues:

1. Operations System Read/Write access was no longer required.
2. CRM Read access was insufficient for the new role.

## 2. Simulated Remediation

The following changes were completed in the fictional dataset:

- Removed Operations System Read/Write access.
- Updated CRM access to Read/Write.
- Updated the HR dataset to reflect the Customer Service Officer role.

All access-change approvals were simulated.

## 3. Verification Results

The Python IAM access-review script reported:

- Employees reviewed: 50
- Permission assignments reviewed: 58
- Remaining findings: 1

Remaining finding:

EMP009 | MOVER REVIEW |
Validate CRM access against the new role

## 4. Analyst Assessment

The remaining CRM Read/Write permission matches the approved
RBAC matrix for the Customer Service Officer role.

The automated finding remains because EMP009's employment
status is recorded as Transferred.

Based on the simulated HR confirmation and RBAC matrix,
no excessive application permission was identified in
the current fictional access dataset.

## 5. Outstanding Actions

- Obtain formal IAM analyst sign-off.
- Obtain application-owner confirmation where required.
- Obtain risk-owner acceptance of the residual risk.
- Confirm that the mover review can be formally closed.

These approvals and sign-offs have not yet been completed.

## 6. Investigation Status

Technical remediation: Completed in simulation.

RBAC validation: Completed against the fictional dataset.

Administrative mover review: Pending formal sign-off.

Risk closure: Pending risk-owner acceptance.

## 7. Evidence References

- lab/evidence/EMP009-access-before-remediation.txt
- lab/evidence/EMP009-post-remediation-review.txt
- lab/evidence/EMP009-remediation-verification.md
- lab/investigations/EMP009-investigation.md
- lab/investigations/EMP009-risk-assessment.md
- lab/investigations/EMP009-access-change-approval.md

## Lab Disclaimer

This investigation is entirely fictional.
All employee records, approvals, permissions, and
remediation activities are simulated.

No production identity systems or employee accounts
were accessed or modified.