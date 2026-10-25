
# IAM Remediation Verification — EMP003

## 1. Case Information

- Organisation: Southern Cross Financial Services (SCFS)
- Case ID: IAM-002
- Employee: EMP003
- Role: Finance Officer
- Initial Risk Rating: High (12/25)
- Environment: Simulated IAM Lab

## 2. Original Finding

EMP003 had HR System Read/Write access,
which conflicted with the proposed RBAC matrix.

Simulated stakeholder validation found no
approved business requirement for this access.

## 3. Remediation Performed

Following simulated approval, the following
permission was removed from the synthetic
access permissions dataset:

EMP003,HR System,Read/Write

No other permission records were intentionally
modified during this remediation.

## 4. Verification Results

The Python IAM access review was executed
after the permission change.

| Metric | Before | After |
|---|---|---|
| Permission assignments | 60 | 59 |
| Automated findings | 4 | 3 |
| EMP003 RBAC finding | Present | Not detected |

Verification outcome: PASS

The automated review no longer identifies
EMP003's excessive HR access.

## 5. Remaining Findings

- EMP008: Terminated employee retains HR access
- EMP009: CRM access requires mover review
- EMP009: Operations System access requires mover review

These findings require separate investigation.

## 6. Evidence References

- lab/evidence/access_permissions-before-EMP003.csv
- lab/evidence/EMP003-post-remediation-review.txt
- lab/investigations/EMP003-investigation.md
- lab/remediation/EMP003-remediation.md

## 7. Verification Limitations

The automated review confirms that the excessive
HR permission is no longer detected.

It does not confirm whether EMP003 has all
legitimate Finance System permissions.

A separate access-provisioning review is required
before declaring the employee's overall access
fully compliant.

## 8. Conclusion

The specific EMP003 HR access violation has been
resolved in the synthetic dataset.

The initial High risk has been treated through
simulated permission removal.

Case status: Technical remediation verified.
Final risk-owner closure remains pending.

All actions were performed in a fictional lab.
No production accounts were modified.


## 9. Final RBAC and Finance Access Verification

### Additional Finding

Following removal of EMP003's unauthorised
HR System access, a separate review identified
that EMP003 had no recorded Finance System access.

The RBAC matrix requires Finance Officers to
have Finance System Read/Write access.

### Simulated Provisioning Approval

The Finance Manager confirmed the business
requirement (simulation).

The Finance System Owner approved Read/Write
access for EMP003 (simulation).

### Provisioning Action

The following permission was added to the
synthetic access permissions dataset:

EMP003,Finance System,Read/Write

### Final Access Verification

| Application | Required Access | Verified Access | Result |
|---|---|---|---|
| Finance System | Read/Write | Read/Write | PASS |
| HR System | No Access | No Access | PASS |
| CRM | No Access | No Access | PASS |
| Operations System | No Access | No Access | PASS |
| IT Administration | No Access | No Access | PASS |

### Automated Review Results

- Permission assignments reviewed: 60
- Remaining findings: 3
- EMP003 RBAC violation: Not detected
- Final RBAC verification: PASS

### Supporting Evidence

- lab/evidence/access_permissions-before-EMP003.csv
- lab/evidence/EMP003-post-remediation-review.txt
- lab/evidence/EMP003-final-access-verification.txt
- lab/investigations/EMP003-investigation.md

### Final Technical Conclusion

EMP003's excessive HR System access was removed.

Approved Finance System Read/Write access was
provisioned in the synthetic dataset.

The final recorded permissions align with the
Finance Officer role in the RBAC matrix.

Technical remediation and provisioning: Verified.

Formal risk-owner closure: Pending.

All activities were performed in a fictional IAM
lab. No production accounts were modified.
