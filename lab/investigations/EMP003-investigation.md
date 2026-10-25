
# IAM Access Investigation — EMP003

## 1. Case Information

- Organisation: Southern Cross Financial Services (SCFS)
- Case ID: IAM-002
- Employee ID: EMP003
- Job Role: Finance Officer
- Analyst: Cybersecurity Analyst (Simulation)
- Status: Open — Awaiting Stakeholder Validation

## 2. Automated Finding

The IAM access review identified a potential
Role-Based Access Control (RBAC) violation.

| Attribute | Details |
|---|---|
| Employee ID | EMP003 |
| Job Role | Finance Officer |
| Detected Access | HR System — Read/Write |
| Expected HR Access | No Access |
| Finding Type | RBAC Violation |

## 3. Evidence Reviewed

1. Employee role information in employees.csv
2. Assigned permissions in access_permissions.csv
3. Proposed RBAC matrix in docs/rbac-matrix.md
4. Automated findings in iam-review-results.txt

The available evidence confirms an access mismatch.
It does not establish whether the permission was approved.

## 4. Potential Security Risk

HR systems may contain sensitive employee information.

Unnecessary Read/Write access could result in:
- Unauthorised viewing of employee records
- Unauthorised modification of HR information
- Increased exposure if the account is compromised
- Non-compliance with internal access-control policies

## 5. Validation Questions

- Does EMP003 have a legitimate business need for HR access?
- Was the permission approved by the Finance Manager?
- Did the HR System Owner authorise this access?
- Is there a documented exception or temporary assignment?
- When was the permission granted?
- Has the access been reviewed recently?

## 6. Stakeholders

| Stakeholder | Responsibility |
|---|---|
| Finance Manager | Confirm employee duties and business need |
| HR System Owner | Validate access authorisation |
| IAM Team | Review provisioning records and permissions |
| Security Team | Assess risk and recommend treatment |

## 7. Preliminary Analyst Assessment

The assigned HR Read/Write permission conflicts with
the proposed RBAC matrix for a Finance Officer.

The finding requires stakeholder validation before
a final access decision can be made.

## 8. Current Status

- RBAC mismatch: Identified
- Business justification: Pending
- Manager approval: Pending
- HR System Owner approval: Pending
- Remediation decision: Pending
- Access changes: Not performed

## 9. Project Scope

This investigation is part of a fictional IAM lab.
All employee records and stakeholder interactions
are simulated. No production systems are involved.

## 10. Simulated Stakeholder Validation

### Finance Manager Response
"EMP003 works exclusively in Finance and does not require access to the HR System. I have not approved any cross-department access."
### HR System Owner Response
"There is no approved business justification or documented exception for EMP003's HR Read/Write access. The permission should be reviewed for removal through the standard access-management process."
### Analyst Assessment
The simulated stakeholder responses do not establish
a legitimate business requirement for the HR permission.

The access presents a risk of unauthorised viewing
or modification of sensitive HR information.
### Recommended Decision
1. Raise a remediation request with the IAM team.
2. Obtain the required approval to remove HR access.
3. Preserve legitimate Finance System permissions.
4. Verify the access change after implementation.
5. Retain the approval and verification evidence.
### Validation Status

Stakeholder validation completed as a simulation.

Remediation recommended but not yet implemented.
No live accounts or permissions have been changed.


## 11. IAM Risk Assessment

### Risk Identification

Risk ID: IAM-RISK-002

Employee EMP003, a Finance Officer, has Read/Write
access to the HR System, which is not permitted
under the proposed RBAC matrix.

Simulated stakeholder validation did not identify
an approved business justification or exception.

### Risk Scenario

If EMP003's account is misused or compromised,
the excessive HR permission could allow
unauthorised viewing or modification of
sensitive employee information.

Potential consequences include:

- Exposure of confidential employee information
- Unauthorised modification of HR records
- Loss of data integrity
- Privacy and compliance concerns
- Reputational damage to the organisation

### Likelihood Assessment

Likelihood: 3/5 — Possible

Justification:

The HR Read/Write permission exists in the
simulated access dataset and exceeds the
employee's documented role requirements.

Although there is no evidence of actual misuse,
the excessive permission creates an opportunity
for inappropriate access or account compromise.

The likelihood score is an illustrative analyst
judgement for this fictional scenario.

### Impact Assessment

Impact: 4/5 — Major

Justification:

HR systems may contain sensitive employee
information, including personal details,
employment records and confidential documents.

Unauthorised viewing or modification could
cause significant privacy, operational and
compliance consequences.

The actual impact would depend on the data
accessible and the controls in place.

### Risk Calculation

Risk Score = Likelihood x Impact

Risk Score = 3 x 4 = 12/25

Risk Rating: HIGH

### Risk Treatment Recommendation

Recommended treatment: Mitigate

1. Request formal approval for access removal.
2. Remove unnecessary HR Read/Write permission
   through the simulated IAM remediation process.
3. Preserve legitimate Finance System access.
4. Re-run the automated access review.
5. Verify that the EMP003 RBAC violation is resolved.
6. Retain remediation and verification evidence.

### Risk Status

- Risk identified: Yes
- Risk assessed: Yes
- Initial risk rating: High (12/25)
- Stakeholder validation: Completed (simulation)
- Risk treatment: Recommended
- Remediation approval: Pending
- Remediation implemented: No
- Post-remediation verification: Pending

All assessments and stakeholder responses are
fictional and intended for cybersecurity training.

## 12. Final Investigation Update

### Remediation Outcome

Following simulated approval, the excessive
HR System Read/Write permission assigned to
EMP003 was removed from the synthetic dataset.

### Verification Results

- Original permission assignments: 60
- Updated permission assignments: 59
- Original automated findings: 4
- Updated automated findings: 3
- EMP003 RBAC violation: No longer detected
- Verification result: PASS

### Final Case Status

- Investigation: Completed
- Risk assessment: High (12/25)
- Stakeholder validation: Completed (simulation)
- Remediation: Implemented (simulation)
- Technical verification: Passed
- Risk-owner closure: Pending

### Outstanding Consideration

The automated review does not establish whether
EMP003 has all required Finance System permissions.

This requires a separate access-provisioning review.

### Evidence

- lab/evidence/access_permissions-before-EMP003.csv
- lab/evidence/EMP003-post-remediation-review.txt
- lab/evidence/EMP003-remediation-verification.md

All activities were conducted in a fictional IAM lab.
No production accounts were modified.


## 13. Additional Finding — Missing Finance System Access

### Finding Identification

During post-remediation review, EMP003 was found
to have no recorded Finance System permissions.

Employee Role: Finance Officer

RBAC Policy Requirement:
- Finance System: Read/Write
- HR System: No Access

Current Access:
- Finance System: No recorded access
- HR System: No Access

### Security and Business Impact

The excessive HR System access has been removed.

However, the absence of Finance System access
may prevent EMP003 from performing authorised
Finance Officer responsibilities.

This is a potential under-provisioning issue.

### Required Validation

1. Confirm EMP003's Finance Officer role.
2. Validate the business need with the Finance Manager.
3. Obtain simulated approval from the Finance System Owner.
4. Provision only the approved Finance System access.
5. Re-run the IAM access review.
6. Verify the final permissions against the RBAC matrix.
7. Record the outcome and supporting evidence.

### Current Status

- Missing access identified: Yes
- RBAC requirement confirmed: Yes
- Business validation: Pending
- Finance System Owner approval: Pending
- Finance access provisioning: Not performed
- Final verification: Pending

This finding relates to a fictional IAM lab.
No production accounts are involved.


## 14. Simulated Finance Access Validation and Approval

### Business Validation

- Employee ID: EMP003
- Role: Finance Officer
- Business Stakeholder: Finance Manager (Simulated)
- Validation Result: Finance System access required
- Business Justification: Employee requires access to perform authorised finance duties.

### System Owner Approval

- Approver: Finance System Owner (Simulated)
- Decision: Approved (Simulation)
- Application: Finance System
- Permission Level: Read/Write
- Access Type: Role-based access
- Approval Scope: EMP003 only

### Approval Conditions

1. Provision only Finance System Read/Write access.
2. Do not restore HR System access.
3. Preserve the original access evidence.
4. Verify the updated permissions against the RBAC matrix.
5. Document the provisioning and verification results.

### Current Status

- Business validation: Completed (Simulation)
- System owner approval: Completed (Simulation)
- Finance access provisioning: Pending
- Post-provisioning verification: Pending

All stakeholder decisions are fictional and
were created for cybersecurity training.
No real business owner was contacted.
