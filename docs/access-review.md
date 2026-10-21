# User Access Review Report

## Organisation
Southern Cross Financial Services (SCFS)

## Review Details
- **Review Type:** Simulated quarterly user access review
- **Scope:** Finance, HR, Operations,
  Customer Service and IT
- **Reference:** [RBAC Matrix](rbac-matrix.md)
- **Status:** Proposed findings awaiting validation

## Objective
Identify permissions that do not match
approved job responsibilities and recommend
remediation following least privilege.

## Access Review Findings

| Employee ID | Job Role | Current Access | Expected Access | Finding | Recommended Action |
|---|---|---|---|---|---|
| EMP001 | Finance Officer | Finance: Read/Write | Finance: Read/Write | Compliant | Retain |
| EMP002 | HR Officer | HR: Read/Write | HR: Read/Write | Compliant | Retain |
| EMP003 | Finance Officer | HR: Read/Write | Finance: Read/Write | Potential mismatch | Validate and correct |
| EMP004 | Operations Officer | CRM: Read | CRM: Read; Operations: Read/Write | Operations access unverified | Investigate |
| EMP005 | Customer Service Officer | IT Admin: Admin | CRM: Read/Write | Excessive privilege | Escalate and remediate |

## Key Security Risks
1. Excessive privileges increase potential impact.
2. Cross-department access may expose data.
3. Missing access may disrupt operations.
4. Unapproved Admin access creates elevated risk.

## Remediation Procedure
1. Confirm roles and existing permissions.
2. Compare access with the RBAC matrix.
3. Obtain manager and application-owner approval.
4. Prioritise privileged-access findings.
5. Coordinate approved changes with IAM.
6. Verify remediation.
7. Record approvals and evidence.

## Governance Notes
- Validate discrepancies before concluding misuse.
- Escalate urgent privileged-access risks.
- Document approved exceptions.
- No live accounts were assessed.

## Review Outcome
Two potential excessive-access findings and
one possible missing-access issue were identified.
Remediation is proposed, not implemented.

## Project Scope
All identities and findings are fictional.
