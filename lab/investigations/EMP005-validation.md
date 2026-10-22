
# IAM Access Validation Report — EMP005

## 1. Case Information

- Organisation: Southern Cross Financial Services (SCFS)
- Case ID: IAM-001
- Employee ID: EMP005
- Employee Name: Liam Taylor
- Department: Customer Service
- Job Role: Customer Service Officer
- Analyst: Cybersecurity Analyst (Simulation)
- Status: Open — Awaiting Validation

## 2. Automated Finding

The IAM access review script identified the following discrepancy:

| Attribute | Access Details |
|---|---|
| Employee | EMP005 — Liam Taylor |
| Assigned Role | Customer Service Officer |
| Expected Access | CRM — Read/Write |
| Detected Access | IT Administration — Admin |
| Finding Type | RBAC Violation |
| Preliminary Risk | Critical (20/25) |

The detected permission does not match the approved RBAC matrix.

## 3. Evidence Reviewed

The following simulated evidence is available:

1. Employee record in employees.csv
2. Current access record in access_permissions.csv
3. Approved role permissions in docs/rbac-matrix.md
4. Automated review output in lab/evidence/iam-review-results.txt

These records establish an access mismatch but do not prove how or why the access was granted.

## 4. Validation Questions

Before deciding on remediation, the analyst must investigate:

- Does Liam Taylor have a legitimate business need for administrator access?
- Was the access approved by the employee's manager?
- Is there an access request or change ticket?
- Was the access granted temporarily?
- Has the account recently changed roles?
- When was administrator access granted?
- Has the privileged account been used recently?
- Are there any suspicious sign-in or audit events?

## 5. Stakeholders to Contact

| Stakeholder | Reason |
|---|---|
| Customer Service Manager | Confirm employee duties and business need |
| IT Application Owner | Verify administrator access requirements |
| IAM Team | Check permission assignments and provisioning history |
| Security Operations Team | Review relevant sign-in and audit logs |
| Risk Owner | Review and accept any justified residual risk |

## 6. Preliminary Risk Assessment

Risk: A Customer Service Officer has administrator access to an IT system without a documented justification in the available evidence.

Potential consequences include:

- Unauthorised system configuration changes
- Exposure of sensitive information
- Privilege misuse
- Increased impact if the account is compromised

Preliminary rating: Critical (20/25), subject to validation.

## 7. Recommended Actions

1. Raise the finding with the IAM team and relevant system owner.
2. Request the original access approval and provisioning records.
3. Confirm whether the permission is required for the employee's current duties.
4. Review relevant sign-in and administrative activity.
5. Escalate promptly if evidence suggests active misuse or immediate risk.
6. If the access is unjustified, obtain the required authorisation and remove the administrator permission.
7. Confirm that legitimate CRM access remains available.
8. Re-run the access review and retain evidence of the outcome.

## 8. Validation Status

| Validation Item | Status |
|---|---|
| RBAC mismatch identified | Confirmed in simulated dataset |
| Manager approval checked | Pending |
| Application owner consulted | Pending |
| Provisioning history reviewed | Pending |
| Privileged activity reviewed | Pending |
| Business justification established | Pending |
| Remediation authorised | Pending |
| Remediation implemented | Not performed |
| Access revalidated | Pending |

## 9. Analyst Conclusion

The automated IAM review identified a discrepancy between EMP005's assigned business role and detected administrator permission.

The finding requires further investigation to establish whether the access is authorised.

No live accounts or permissions have been changed.

This report forms part of a fictional cybersecurity laboratory designed to demonstrate IAM access validation, least privilege, RBAC, and risk-based investigation.

## 10. Simulated Stakeholder Validation

### Customer Service Manager Response

The manager confirmed that EMP005 requires CRM Read/Write access for normal duties.

The manager did not approve administrator access to the IT Administration system.

### IT Application Owner Response

The application owner reported that no approved access request or documented exception was found for EMP005's administrator permission.

### Analyst Assessment

The simulated stakeholder responses do not establish a legitimate business justification for the administrator permission.

Recommended decision: Escalate the finding and request authorised removal of the excessive privilege while preserving legitimate CRM access.

### Current Status

Validation exercise completed using fictional stakeholder responses.

Remediation recommended but not implemented.

Provisioning history, privileged activity, and post-remediation verification remain outstanding.
