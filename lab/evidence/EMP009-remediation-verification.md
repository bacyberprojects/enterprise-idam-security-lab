# EMP009 — IAM Mover Remediation Verification

## Organisation
Southern Cross Financial Services (SCFS)

## Employee Details
- Employee ID: EMP009
- Employee Name: Lucas Martin
- Previous Role: Operations Officer
- New Role: Customer Service Officer
- HR Confirmation: Simulated
- Access Change Approvals: Simulated

## 1. Original Access

Before remediation, EMP009 had:

| Application | Permission |
|---|---|
| CRM | Read |
| Operations System | Read/Write |

Evidence:
lab/evidence/EMP009-access-before-remediation.txt

## 2. Simulated Remediation Performed

The following changes were made to the fictional
access_permissions.csv dataset:

1. Removed Operations System Read/Write access.
2. Changed CRM access from Read to Read/Write.

No production accounts or permissions were modified.

## 3. Post-Remediation Access

| Application | Permission |
|---|---|
| CRM | Read/Write |
| Operations System | No Access |

These permissions match the approved SCFS RBAC matrix
for the Customer Service Officer role.

## 4. Python Access Review Results

The IAM access-review script was executed after remediation.

Results:
- Employees reviewed: 50
- Permission assignments reviewed: 58
- Findings: 1

Remaining finding:
EMP009 | MOVER REVIEW |
Validate CRM access against the new role

Evidence:
lab/evidence/EMP009-post-remediation-review.txt

## 5. Remaining Finding Assessment

The remaining finding is triggered because EMP009's
employment status is recorded as Transferred.

The simulated HR confirmation identifies the new role
as Customer Service Officer.

CRM Read/Write is permitted for this role under
the SCFS RBAC matrix.

Therefore, the remaining finding is assessed as an
administrative mover-review item rather than a
confirmed excessive-access violation.

The HR dataset still records Operations Officer.
Updating the authoritative role record and obtaining
formal analyst sign-off remain outstanding.

## 6. Verification Conclusion

The simulated access changes have been verified
against the fictional permission dataset.

The previous Operations System access has been removed,
and CRM access matches the simulated new role.

This verification does not establish that any real
identity provider or application permissions changed.

## 7. Status

Technical remediation: Completed in simulation.

Administrative review: Pending.

Formal risk closure: Pending risk-owner acceptance.

## Lab Disclaimer

All employees, approvals, permissions, and remediation
activities are fictional and simulated.