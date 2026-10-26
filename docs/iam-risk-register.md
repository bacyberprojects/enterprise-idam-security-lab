# IAM Risk Register

## Organisation
Southern Cross Financial Services (SCFS)

## Objective
Identify, assess and recommend treatment for identity and access management risks in the fictional SCFS environment.

## Risk Assessment Method
Risk Score = Likelihood × Impact

Likelihood and Impact are scored from 1 (lowest) to 5 (highest).

| Risk Score | Rating |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

## IAM Risk Register

| Risk ID | Risk Description | Likelihood | Impact | Score | Rating | Recommended Control |
|---|---|---|---|---|---|---|
| IAM-001 | Customer Service employee has unnecessary IT Admin privileges | 4 | 5 | 20 | Critical | Validate and remove unapproved privileged access; apply least privilege |
| IAM-002 | Finance employee has access to confidential HR records | 3 | 4 | 12 | High | Verify business need and remediate inappropriate access |
| IAM-003 | Former employee account remains active after departure | 3 | 5 | 15 | High | Enforce timely JML deprovisioning and session revocation |
| IAM-004 | Employee retains old permissions after changing departments | 4 | 4 | 16 | High | Review and update permissions during mover events |
| IAM-005 | Access permissions are not reviewed periodically | 3 | 4 | 12 | High | Conduct quarterly access reviews with documented approvals |
| IAM-006 | Employee account lacks required MFA protection | 3 | 5 | 15 | High | Enforce appropriate MFA policies and monitor exceptions |
| IAM-007 | EMP008: Terminated HR employee retains HR System Read/Write permission | 4 | 5 | 20 | Critical | Revoke retained HR access; verify account disablement, sessions and other entitlements; retain risk open pending additional verification |
### IAM-007 — Post-Remediation Risk Update

**Case:** EMP008 — Terminated HR Employee

**Original Risk Assessment**
- Likelihood: 4/5
- Impact: 5/5
- Score: 20/25
- Rating: Critical

**Simulated Remediation**
- HR System permission removed.
- Identity account disabled.
- Active session revoked.
- Refresh token revoked.
- Automated IAM review completed with no EMP008 findings.

**Proposed Residual Risk Assessment**
- Likelihood: 2/5
- Impact: 5/5
- Score: 10/25
- Rating: High

**Outstanding Verification**
- Application-specific session invalidation.
- Actual token invalidation.
- Identity-provider audit and sign-in logs.
- Other application and device access.
- Independent verification of security controls.

**Risk Status**
- Simulated technical remediation: Completed.
- Automated CSV-based verification: Passed.
- Residual risk: High (provisional).
- Risk-owner approval: Pending.
- Formal risk closure: Pending.

**Supporting Evidence**
- lab/investigations/EMP008-risk-assessment.md
- lab/evidence/EMP008-identity-post-remediation-review.txt
- lab/evidence/EMP008-session-token-post-remediation-review.txt

**Note:** All identities, approvals and remediation actions
are fictional. No production systems were modified.

## Risk Treatment Process
1. Identify the IAM risk and affected systems.
2. Assess likelihood and business impact.
3. Assign a risk owner and prioritise treatment.
4. Validate findings with business and application owners.
5. Implement approved security controls.
6. Verify effectiveness and document evidence.
7. Reassess residual risk and obtain risk-owner acceptance where appropriate.

## Governance Notes
- Risk scores are illustrative and require validation.
- IAM-001 and IAM-002 relate to the simulated access-review findings.
- IAM-003 to IAM-006 are additional hypothetical risk scenarios.
- Recommended controls have not yet been implemented.
- Privileged-access risks require prompt escalation.

## Project Scope
This is a simulated IAM risk assessment using fictional identities and systems. No production environment was assessed.
