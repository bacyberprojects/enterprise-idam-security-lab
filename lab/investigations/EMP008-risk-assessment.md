
# EMP008 — IAM Security Risk Assessment

## 1. Risk Identification

Risk ID: IAM-007
Risk register reference: docs/iam-risk-register.md

Risk owner: HR System Owner (proposed)

Inherent risk: 20/25 — Critical

Residual risk: Pending further verification

Risk status: Technical remediation completed;
formal risk closure pending.

Employee: EMP008 — Mia Thompson

Employment status: Terminated

Affected asset: HR System

Finding: Terminated employee retains Read/Write permission.

Risk statement:

There is a risk that a terminated employee
could gain unauthorised access to sensitive
HR information because their application
permission was not removed during offboarding.

## 2. Business Impact

### Confidentiality

Potential exposure of sensitive employee
and organisational information.

### Integrity

Potential unauthorised modification or
deletion of HR records.

### Availability

Potential disruption to HR operations
if the retained permission is misused.

## 3. Preliminary Inherent Risk Assessment

Likelihood: 4/5 — Likely

Justification:
The retained permission creates an access
control weakness. However, account status,
authentication capability and actual misuse
have not been confirmed.

Impact: 5/5 — Severe

Justification:
If the permission remains usable, misuse
could cause serious privacy, legal,
operational and reputational consequences.

Risk score: 4 x 5 = 20/25

Risk classification:
Risk classification: Critical

Risk matrix reference:
docs/iam-risk-register.md

The organisation's risk matrix classifies
scores of 17-25 as Critical.

EMP008's preliminary inherent risk score
is 20/25 (Likelihood 4 x Impact 5).

This is an illustrative inherent risk rating.
Account authentication status and actual
post-termination activity remain unverified.

## 4. Control Gap

Control area: Identity and Access Management

Process: Joiner-Mover-Leaver (JML)

Control weakness:
The synthetic permission record was not
removed when the employee became terminated.

Relevant frameworks:

- NIST CSF 2.0 — PR.AA
- ACSC Essential Eight — Restrict Administrative
  Privileges (where privileged access applies)
- ISO/IEC 27001:2022 Annex A — 5.18 Access Rights

## 5. Risk Treatment

Treatment option: Mitigate

Actions:

1. Confirm termination with HR.
2. Verify account status with IAM.
3. Revoke unnecessary application access.
4. Disable the identity account if still active.
5. Revoke active sessions and tokens.
6. Review authentication and access logs.
7. Verify completion of deprovisioning.
8. Investigate the JML process failure.

## 6. Remediation Evidence

The HR System Read/Write permission was
removed from the synthetic dataset.

Automated IAM review results:

- Permission assignments before: 60
- Permission assignments after: 59
- Findings before: 3
- Findings after: 2
- EMP008 finding: No longer detected

Evidence:
lab/evidence/EMP008-post-remediation-review.txt

## 7. Residual Risk Assessment

Residual likelihood: Pending

Residual impact: Pending

Residual risk score: Pending

Reason:
The automated review verifies removal
of the permission assignment only.

Account disablement, active sessions,
other access paths and authentication
activity remain unverified.

A lower residual risk rating cannot yet
be justified using the available evidence.
### Control Effectiveness Assessment

Implemented control:
Removal of EMP008's HR System Read/Write
permission from the synthetic dataset.

Verification result:
PASS — EMP008 is no longer flagged by
the automated IAM access review.

Control effectiveness:
Effective for the permission assignment
represented in the CSV dataset.

Limitations:
- Identity account status not verified.
- Active sessions and tokens not checked.
- Authentication logs not reviewed.
- External application access not verified.

Residual risk rating:
Pending additional validation.

Risk acceptance:
Pending simulated risk-owner review.

Conclusion:
The identified permission assignment has
been remediated successfully.

The broader leaver-access risk cannot yet
be considered fully resolved.

## 8. Risk Ownership and Closure

Proposed risk owner: HR System Owner

Simulated remediation approval: Recorded

Technical permission remediation: Completed

Automated verification: Passed

Formal risk acceptance or closure: Pending

## 9. Simulation Disclaimer

This assessment is based on fictional
employee records and a synthetic IAM lab.

No real employee, production account,
security incident or stakeholder approval
is represented.
## 10. Outstanding Verification Requirements

The following controls require additional evidence
before formal risk closure can be recommended.

| Control | Evidence Required | Status |
|---|---|---|
| Identity account disabled | IAM account status record | Not verified |
| Active sessions revoked | Session revocation record | Not verified |
| Authentication activity reviewed | Sign-in audit logs | Not verified |
| Other application access removed | Complete entitlement review | Not verified |
| HR permission removed | Automated IAM review output | Verified |

## 11. Risk Closure Recommendation

Recommendation:
Keep the broader leaver-access risk open
pending verification of outstanding controls.

Completed:
- Synthetic HR permission removal
- Automated permission verification
- Preservation of remediation evidence

Outstanding:
- Additional identity control verification
- Residual risk scoring
- Simulated risk-owner acceptance

Final status:
Technical permission remediation completed.
Formal risk closure pending.

## 10. Post-Remediation Residual Risk Assessment

### Risk Reference
IAM-007 — Terminated Employee Retains Access

### Original Risk
Likelihood: 4/5
Impact: 5/5
Inherent Risk Score: 20/25
Rating: Critical

### Simulated Controls Implemented
1. Removed unauthorised HR System permission.
2. Disabled the employee's identity account.
3. Revoked the simulated active session.
4. Revoked the simulated refresh token.
5. Re-ran the automated IAM security review.

### Verification Results
The automated review reports no remaining
EMP008 findings in the synthetic datasets.

Evidence:
- EMP008-post-remediation-review.txt
- EMP008-identity-post-remediation-review.txt
- EMP008-session-token-post-remediation-review.txt

### Outstanding Verification
- Application-specific session invalidation.
- Actual token invalidation and expiry behaviour.
- Identity-provider audit and sign-in logs.
- Other application and device access.
- Independent security validation.

### Residual Risk Assessment
Proposed likelihood: 2/5
Impact: 5/5
Proposed residual score: 10/25

The proposed score reflects reduced likelihood
after simulated remediation. Business impact
remains high because HR information is sensitive.

Residual Risk Rating: High (10/25)

Risk Matrix Reference:
- Low: 1–4
- Medium: 5–9
- High: 10–16
- Critical: 17–25

Risk Rating Justification:

The proposed likelihood has decreased from 4 to 2
following simulated application permission removal,
identity account disablement, and session and refresh
token revocation.

The impact remains 5 because unauthorised access
to sensitive HR information could have serious
business and privacy consequences.

The residual risk remains High because application-
specific sessions, actual token invalidation, and
identity-provider audit logs have not been independently
verified.

The proposed residual rating requires risk-owner
review and approval.

Formal Risk Closure: Pending

### Risk Decision
Technical remediation: Verified in simulation.
Residual risk: Provisionally assessed.
Formal risk-owner acceptance: Pending.
Case closure: Pending.

This is a fictional IAM lab assessment.
No production identity or application was modified.