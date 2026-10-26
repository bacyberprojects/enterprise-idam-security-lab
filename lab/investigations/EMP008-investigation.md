# IAM Access Investigation — EMP008

## 1. Investigation Overview

- Organisation: Southern Cross Financial Services (fictional)
- Employee ID: EMP008
- Employee Name: Mia Thompson
- Department: HR
- Job Role: HR Officer
- Employment Status: Terminated
- Application: HR System
- Assigned Permission: Read/Write
- Finding Type: Leaver Access Risk

## 2. Issue Identified

The automated IAM access review identified that EMP008 is
recorded as terminated in the employee dataset but still has
Read/Write access to the HR System.

This indicates a potential failure in the
Joiner–Mover–Leaver (JML) deprovisioning process.

## 3. Evidence Reviewed

- lab/data/employees.csv
- lab/data/access_permissions.csv
- lab/evidence/access_permissions-before-EMP008.csv
- Automated IAM access-review finding for EMP008

## 4. Security Risk

A terminated employee retaining HR System access may create
opportunities for unauthorised access, disclosure, or
modification of sensitive employee information.

The dataset confirms a retained permission assignment.
It does not establish whether the account is enabled or
whether access was used after termination.

## 5. Investigation Status

- Employment status verified against synthetic HR records: Yes
- Permission assignment verified: Yes
- Account activation status: Not yet verified
- Simulated HR/IT stakeholder validation: Pending
- Risk assessment: Pending
- Remediation authorisation: Pending
- Permission changes: Not performed

## 6. Project Scope

This investigation is part of a fictional IAM security lab.
All employee records and stakeholder interactions are
simulated. No production systems or real user accounts
are involved.

## 7. Preliminary Risk Assessment

- Risk: Terminated employee retains HR System access
- Likelihood: 4/5 (Likely)
- Impact: 5/5 (Severe)
- Inherent risk score: 20/25
- Risk classification: Pending confirmation against risk matrix

### Likelihood Justification

EMP008 is recorded as terminated but retains a
Read/Write permission assignment to the HR System.

The retained permission indicates a potential
deprovisioning failure. Account status and actual
login capability have not yet been verified.

### Impact Justification

If the account remains usable, unauthorised access
could expose or modify sensitive employee information,
potentially causing privacy, compliance and
operational consequences.

### Recommended Risk Treatment

- Confirm the employee's termination status with HR.
- Verify the account status with IT/IAM.
- Arrange prompt revocation of access through the
  approved deprovisioning process.
- Verify that the permission has been removed.
- Preserve evidence and obtain risk-owner closure.

No access changes have been performed at this stage.

## 8. Simulated Stakeholder Validation

### HR Department

Validation required:
- Confirm EMP008's termination date.
- Confirm whether any approved post-employment access exists.
- Identify the offboarding request or ticket.

Status: Pending simulated validation.

### IT / IAM Team

Validation required:
- Confirm whether EMP008's account is enabled or disabled.
- Verify the assigned HR System permission.
- Check whether the deprovisioning process was completed.
- Review available authentication and access logs.

Status: Pending simulated validation.

### Analyst Assessment

The employee dataset records EMP008 as Terminated.

The access dataset confirms that EMP008 retains
HR System Read/Write permission.

This represents a leaver-access control finding.

The account's ability to authenticate and any
post-termination activity remain unverified.

### Remediation Decision

Recommended action:
Revoke EMP008's HR System access following
authorised stakeholder validation.

Approval status: Pending.
Remediation status: Not started.

All records and stakeholder interactions in
this project are fictional.

## 9. Simulated Stakeholder Responses

### HR Department — Simulated Response

HR confirms that EMP008 (Mia Thompson) is a
terminated employee.

HR confirms that EMP008 has no approved
post-employment requirement for HR System access.

This confirmation is fictional and provided
for the training scenario.

### IT / IAM Team — Simulated Response

The IAM team confirms that EMP008 still has
HR System Read/Write permission assigned.

The account's authentication status and any
post-termination login activity have not been
independently verified.

The IAM team recommends removing the retained
permission through the approved leaver process.

### Analyst Decision

Based on the synthetic employee record, access
dataset and simulated stakeholder confirmations,
the retained HR System permission is not justified.

Recommended treatment:
- Revoke EMP008's HR System Read/Write permission.
- Check for other application permissions.
- Verify account disablement separately.
- Run the automated IAM access review again.
- Preserve before-and-after evidence.

Simulated remediation authorisation: Approved
for the fictional lab exercise.

Actual production approval: Not applicable.

### Case Status

- Investigation: Completed
- Risk assessment: Preliminary
- Simulated stakeholder validation: Completed
- Simulated remediation authorisation: Approved
- Permission revocation: Pending
- Post-remediation verification: Pending
- Formal risk-owner closure: Pending