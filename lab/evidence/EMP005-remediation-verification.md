
# IAM Remediation Verification Evidence — EMP005

## 1. Case Details

- Organisation: Southern Cross Financial Services (SCFS)
- Case ID: IAM-001
- Employee ID: EMP005
- Employee Name: Liam Taylor
- Role: Customer Service Officer
- Risk Rating: Critical (20/25)
- Verification Type: Simulated
- Status: Pending Simulated Verification

## 2. Purpose

This document records the evidence required to verify remediation of excessive privileged access identified during the IAM access review.

All information is part of a fictional cybersecurity laboratory.

## 3. Access Before Remediation

| Application | Detected Access | Approved Access | Finding |
|---|---|---|---|
| IT Administration | Admin | No Access | RBAC Violation |
| CRM | Not yet verified | Read/Write | Verification Required |

## 4. Expected Access After Remediation

| Application | Expected Access | Verification Status |
|---|---|---|
| IT Administration | No Access | Pending |
| CRM | Read/Write | Pending |

## 5. Verification Procedure

1. Obtain confirmation that the access removal was authorised.
2. Review the updated user permissions.
3. Confirm that IT Administration Admin access has been removed.
4. Confirm that CRM Read/Write access is correctly assigned.
5. Review relevant administrative activity logs.
6. Capture simulated evidence of the updated permissions.
7. Record the verification results.
8. Submit the case for risk-owner review and closure.

## 6. Evidence Checklist

- [ ] Authorised change request recorded
- [ ] Updated IT Administration permissions reviewed
- [ ] CRM permissions verified
- [ ] Relevant activity logs reviewed
- [ ] Before-and-after access evidence recorded
- [ ] Risk register updated
- [ ] Risk owner approved closure

## 7. Current Verification Result

## 7. Current Verification Result

**Verification Status:** Passed — Automated RBAC Check

After updating `access_permissions.csv`, the IAM access review script was executed again.

**Results:**
- EMP005's unauthorised IT Administration access was removed from the simulated permissions data.
- EMP005 was assigned CRM Read/Write access according to the RBAC matrix.
- The automated access review no longer reports EMP005 as an RBAC violation.
- Four other findings remain and require separate investigation.

**Conclusion:** The simulated remediation for EMP005 passed automated verification. No live organisation accounts or permissions were changed.

## 8. Disclaimer

This is a simulated IAM cybersecurity project. No real employee accounts, applications or permissions have been modified.
