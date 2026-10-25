
# IAM Remediation Plan — EMP003

## 1. Case Information

- Organisation: Southern Cross Financial Services (SCFS)
- Case ID: IAM-002
- Employee ID: EMP003
- Role: Finance Officer
- Risk Rating: High (12/25)
- Status: Proposed — Awaiting Remediation Approval

## 2. Identified Security Issue

The automated IAM access review identified
HR System Read/Write access assigned to EMP003.

According to the proposed RBAC matrix,
Finance Officers should not have HR System access.

Simulated stakeholder validation found no
legitimate business requirement or approved exception.

## 3. Remediation Objective

Remove unnecessary HR System access while
preserving legitimate Finance System permissions.

## 4. Proposed Remediation Actions

1. Raise an IAM remediation request.
2. Obtain approval from the authorised access owner.
3. Confirm EMP003's current job responsibilities.
4. Record the original permission assignment.
5. Remove HR System Read/Write access from the
   synthetic permissions dataset.
6. Preserve any authorised Finance System access.
7. Re-run the automated IAM access review.
8. Verify that the EMP003 finding is resolved.
9. Retain approval and verification evidence.

## 5. Simulated Responsibilities

| Stakeholder | Responsibility |
|---|---|
| Finance Manager | Confirm legitimate business access |
| HR System Owner | Authorise removal of HR access |
| IAM Team | Implement approved permission change |
| Cybersecurity Analyst | Verify and document remediation |

## 6. Change Control

- Change Type: Removal of excessive access
- Target: EMP003 — HR System — Read/Write
- Environment: Fictional CSV-based IAM lab
- Approval Status: Pending
- Implementation Status: Not Started
- Verification Status: Pending

## 7. Expected Outcome

After authorised simulated remediation:

- EMP003 should no longer have HR System access.
- Legitimate Finance System access should remain.
- The automated review should no longer flag
  EMP003 for the same RBAC violation.
- Other outstanding findings should remain
  available for separate investigation.

## 8. Evidence Requirements

- Original access-review finding
- Simulated stakeholder validation
- Documented remediation approval
- Before-and-after permission records
- Updated automated access-review output
- Analyst verification conclusion

## 9. Current Status


## 9. Current Status

- Simulated remediation approval: Completed
- Permission removal: Completed
- Automated verification: Passed
- EMP003 RBAC violation: No longer detected
- Initial risk rating: High (12/25)
- Technical remediation status: Verified
- Final risk-owner closure: Pending

The unauthorised HR System Read/Write permission
was removed from the synthetic permissions dataset.

The automated IAM review confirmed that the
EMP003 finding was no longer detected.

Verification evidence is recorded in:
lab/evidence/EMP003-remediation-verification.md

A separate review is required to determine
whether EMP003 needs Finance System access.

No production accounts were modified.s

## 10. Simulated Remediation Approval

### Approval Record

- Case ID: IAM-002
- Employee ID: EMP003
- Approver: HR System Owner (Simulated)
- Decision: Approved (Simulation)
- Approved Change: Remove HR System Read/Write access
- Business Justification: Access is not required for the Finance Officer role
- Environment: Synthetic IAM laboratory

### Approval Conditions

1. Remove only the unauthorised HR System permission.
2. Preserve all legitimate Finance System permissions.
3. Record the original permission before modification.
4. Run the automated access review after remediation.
5. Retain evidence of the change and verification.

### Change Status

- Approval: Completed (Simulation)
- Implementation: Pending
- Verification: Pending

This approval is fictional and is recorded
solely for cybersecurity training purposes.
No real system owner was contacted.

