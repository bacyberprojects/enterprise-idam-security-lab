
# EMP008 — IAM Remediation Verification Report

## 1. Case Overview

- Employee ID: EMP008
- Employee Name: Mia Thompson
- Department: HR
- Employment Status: Terminated
- Finding: Retained HR System Read/Write access
- Environment: Fictional IAM Security Lab

## 2. Remediation Performed

The HR System Read/Write permission assigned
to EMP008 was removed from the synthetic
access_permissions.csv dataset.

The original permissions were preserved
before the simulated remediation.

## 3. Automated Verification

The IAM access review script was executed
after the permission change.

### Results

- Employees reviewed: 50
- Permission assignments before: 60
- Permission assignments after: 59
- IAM findings before: 3
- IAM findings after: 2
- EMP008 finding: No longer detected

The two remaining findings relate to EMP009
and require separate investigation.

## 4. Evidence Files

- lab/evidence/access_permissions-before-EMP008.csv
- lab/evidence/EMP008-post-remediation-review.txt
- lab/investigations/EMP008-investigation.md
- lab/remediation/EMP008-remediation.md

## 5. Verification Outcome

PASS — The automated IAM review no longer
detects retained HR System access for EMP008.

This confirms the synthetic permission removal.

Account disablement, session revocation and
authentication activity remain unverified.

## 6. Case Status

- Investigation: Completed
- Simulated remediation: Completed
- Automated verification: Passed
- Evidence: Preserved
- Formal risk-owner closure: Pending

All employee records and approvals in this
project are fictional and simulated.
