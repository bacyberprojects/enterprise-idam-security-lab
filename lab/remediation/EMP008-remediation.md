
# IAM Remediation Plan — EMP008

## 1. Case Information

- Employee ID: EMP008
- Employee Name: Mia Thompson
- Department: HR
- Role: HR Officer
- Employment Status: Terminated
- Application: HR System
- Existing Permission: Read/Write
- Preliminary Risk Score: 20/25
- Risk Classification: Pending risk matrix confirmation

## 2. Security Finding

EMP008 is recorded as terminated but still
has HR System Read/Write permission assigned.

This indicates a potential failure in the
Joiner-Mover-Leaver (JML) process.

## 3. Remediation Objective

Ensure that the terminated employee no longer
has assigned access to the HR System.

## 4. Simulated Authorisation

- HR validation: Completed (Simulation)
- IAM validation: Completed (Simulation)
- Remediation approval: Approved (Simulation)

No real employees or production systems are involved.

## 5. Planned Remediation Steps

1. Preserve the original access permissions.
2. Identify all permissions assigned to EMP008.
3. Remove the HR System Read/Write permission.
4. Run the automated IAM access review.
5. Confirm EMP008 is no longer flagged for
   retained HR System access.
6. Preserve post-remediation evidence.
7. Document the verification results.

## 6. Additional Controls

In a real organisation, the IAM team would also:

- Disable the employee's identity account.
- Revoke active sessions and tokens.
- Remove remaining application permissions.
- Review authentication logs.
- Confirm completion of the leaver process.

These controls are outside the current CSV
remediation scope and remain unverified.

## 7. Remediation Status

- Investigation: Completed
- Simulated authorisation: Approved
- Original evidence: Preserved
- Permission removal: Pending
- Automated verification: Pending
- Formal risk-owner closure: Pending
## 8. Identity Account Remediation

### Additional Security Finding

The automated IAM review identified that EMP008
is terminated but has an enabled identity account
in the simulated Microsoft Entra ID dataset.

Finding: LEAVER IDENTITY RISK

### Risk Assessment

Risk reference: IAM-007

Inherent risk: 20/25 — Critical

An enabled identity account belonging to a
terminated employee may permit unauthorised
authentication if other security controls
do not prevent access.

### Simulated Authorisation

HR confirmation: Completed (Simulation)

IAM team validation: Completed (Simulation)

Proposed action: Disable EMP008's identity account.

Simulated IAM approval: Approved for lab exercise.

Production approval: Not applicable.

### Planned Technical Remediation

1. Preserve the original identity account record.
2. Change EMP008's Account_Status to Disabled.
3. Run the automated IAM review.
4. Confirm the identity-risk finding disappears.
5. Preserve post-remediation evidence.
6. Investigate active sessions and tokens separately.

### Current Status

Identity account disablement: Pending

Session revocation: Not verified

Token revocation: Not verified

Residual risk assessment: Pending

Formal risk-owner closure: Pending

All account records and approvals are simulated.
## 9. Session and Refresh Token Remediation

### Security Findings

The automated IAM review identified two additional risks:

- LEAVER SESSION RISK: EMP008 retains an active session.
- LEAVER TOKEN RISK: EMP008 retains an active refresh token.

These findings are based on synthetic lab data.

### Risk Reference

IAM-007 — Terminated employee retains access.

The original inherent risk assessment is Critical (20/25).

### Proposed Remediation

1. Confirm EMP008's employment termination.
2. Obtain IAM and application-owner authorisation.
3. Revoke EMP008's active sign-in sessions.
4. Invalidate EMP008's refresh tokens.
5. Verify that the employee cannot establish new sessions.
6. Check for remaining application-specific sessions.
7. Preserve post-remediation evidence.
8. Reassess residual risk.

### Authorisation Status

### Simulated Authorisation Decision

Scenario: EMP008 is a terminated HR employee with an
active session and refresh token in the fictional dataset.

Decision: Approved for simulated revocation.

Approving role: IAM Security Manager (fictional).

Reason: Terminated employees must not retain active
authentication sessions or refresh tokens.

Scope: EMP008 only.

Production approval: Not applicable.

Note: This is a fictional approval for a training exercise,
not evidence of an actual stakeholder decision.

Production approval: Not applicable.

### Current Remediation Status

Identity account: Disabled (simulated)

HR application permission: Removed (simulated)

Session revocation: Pending

Refresh token revocation: Pending

Application-specific session verification: Pending

Formal risk-owner closure: Pending

### Important Limitation

This project uses fictional identities and simulated
session records. Changing CSV values does not revoke
real Microsoft Entra ID sessions or tokens.