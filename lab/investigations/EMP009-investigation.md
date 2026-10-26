# EMP009 — IAM Mover Access Investigation

## Organisation
Southern Cross Financial Services (SCFS)

## Investigation Type
Joiner-Mover-Leaver (JML) — Mover Access Review

## Employee Details
- Employee ID: EMP009
- Employee Name: Lucas Martin
- Previous Role: Operations Officer
- New Role: Customer Service Officer
- Employment Status: Transferred

## HR Confirmation
For this fictional lab, HR has confirmed that Lucas Martin
transferred from Operations Officer to Customer Service Officer.

This confirmation is simulated and does not represent
a real HR approval.

## Current Access
- CRM: Read
- Operations System: Read/Write

## Required Access — New Role
According to the SCFS RBAC matrix:
- CRM: Read/Write
- Operations System: No Access

## Security Findings

### Finding 1 — Excessive Access
EMP009 retains Read/Write access to the Operations System,
which is not authorised for the Customer Service Officer role.

### Finding 2 — Insufficient Access
EMP009 currently has CRM Read access but requires
Read/Write access for the new role.

## Initial Recommendation
1. Obtain simulated manager and application-owner approvals.
2. Revoke the previous Operations System access.
3. Update CRM access to Read/Write.
4. Verify the resulting permissions against the RBAC matrix.
5. Record evidence of the simulated remediation.

## Investigation Status
Open — Awaiting simulated access-change approvals.

## Lab Disclaimer
All employees, permissions, approvals, and remediation
activities in this investigation are fictional and simulated.
No production identity systems are modified.