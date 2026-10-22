
# IAM Security Investigation Report — EMP005

## 1. Investigation Details

- Organisation: Southern Cross Financial Services (SCFS)
- Case ID: IAM-001
- Employee ID: EMP005
- Employee Name: Liam Taylor
- Department: Customer Service
- Role: Customer Service Officer
- Investigation Status: Open — Pending Validation
- Risk Rating: Critical (20/25) — Preliminary

## 2. Security Finding

The automated IAM access review identified that EMP005 has Admin access to the IT Administration system.

According to the approved RBAC matrix, a Customer Service Officer should have Read/Write access to the CRM system.

The assigned administrator privileges do not match the employee's standard business role.

## 3. Security Risk

Excessive administrator privileges may allow:

- Unauthorised changes to IT systems
- Access to sensitive organisational information
- Misuse of privileged accounts
- Increased damage if the employee's account is compromised

This finding represents a potential violation of the principle of least privilege.

## 4. Investigation Actions

The cybersecurity analyst should:

1. Verify the employee's current access assignments.
2. Compare the permissions against the approved RBAC matrix.
3. Check whether an approved exception or temporary access request exists.
4. Contact the employee's manager to confirm business requirements.
5. Consult the IT application owner to validate the need for administrator privileges.
6. Review available access logs for suspicious activity, if authorised and available.
7. Document findings and escalate according to organisational procedures.

## 5. Risk Assessment

- Likelihood: 4/5
- Impact: 5/5
- Risk Score: 20/25
- Risk Rating: Critical

This is a preliminary simulated risk assessment based on the organisation's IAM risk register. The rating should be reviewed after validation.

## 6. Recommended Remediation

If administrator privileges are not justified:

1. Obtain the required authorisation for the access change.
2. Coordinate with the IAM team to remove unnecessary administrator privileges.
3. Confirm the employee retains approved CRM access.
4. Verify the updated permissions.
5. Record the change ticket, approvals and supporting evidence.
6. Update the risk register and close the finding once remediation is verified.

Urgent containment should follow the organisation's incident response or privileged-access procedures if immediate risk is identified.

## 7. Evidence

- Automated access review: `../evidence/iam-review-results.txt`
- Approved RBAC matrix: `../../docs/rbac-matrix.md`
- IAM risk register: `../../docs/iam-risk-register.md`

Additional evidence to collect:

- [ ] Current access assignment screenshot or export
- [ ] Manager confirmation
- [ ] Application owner confirmation
- [ ] Access request or exception record
- [ ] Change approval and implementation record
- [ ] Post-remediation access verification

## 8. Investigation Outcome

Status: Open — Awaiting Validation

The automated review has identified a potential access control violation. No live employee permissions have been changed.

The finding must be validated before a final remediation decision is made.

---

**Project Note:** This investigation is based on fictional employee data and simulated IAM access permissions. It demonstrates a cybersecurity analyst's investigation and risk management workflow.
