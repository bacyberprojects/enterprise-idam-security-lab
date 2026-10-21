# IAM Risk Treatment and Remediation Plan

## Organisation
Southern Cross Financial Services (SCFS)

## Purpose
Document a proposed remediation process for excessive privileged access identified during a simulated user access review.

## Finding Details
- **Finding ID:** IAM-001
- **Employee ID:** EMP005
- **Job Role:** Customer Service Officer
- **Identified Access:** IT Administration — Admin
- **Expected Access:** CRM — Read/Write
- **Risk Rating:** Critical (20/25, illustrative)
- **Status:** Open — awaiting validation and remediation

## Problem
EMP005 has IT administrative privileges that do not match the proposed RBAC permissions for a Customer Service Officer.

## Security Risk
Unnecessary administrative access increases the potential impact of account compromise or misuse. An attacker could potentially modify IT settings or disrupt business systems.

## Proposed Remediation Actions
1. **Escalate:** Notify the security and IAM teams promptly due to the privileged-access exposure.
2. **Validate:** Confirm the employee's current role, permissions and business requirements with the department manager and IT application owner.
3. **Authorise:** Obtain approval for the proposed access changes under the organisation's access management procedure.
4. **Contain:** If the access is confirmed unauthorised and presents immediate risk, follow the approved urgent-access removal procedure.
5. **Remediate:** Remove unnecessary IT administrative privileges and ensure the employee has only approved CRM access.
6. **Verify:** Confirm that the employee no longer has IT Admin privileges and can still perform authorised Customer Service tasks.
7. **Document:** Record the request, approval, change record, timestamps and verification evidence.
8. **Review:** Reassess residual risk and investigate why the excessive access was originally granted.

## Roles and Responsibilities
| Role | Responsibility |
|---|---|
| Department Manager | Confirm employee responsibilities and access requirements |
| IT Application Owner | Validate privileged access and approve appropriate changes |
| IAM Team | Implement and verify authorised access changes |
| Security Analyst | Assess risk, coordinate escalation and document findings |
| Risk Owner | Review residual risk and accept or escalate it as appropriate |

## Remediation Evidence Checklist
- [ ] Current permissions captured before changes
- [ ] Business requirement validated
- [ ] Required approval recorded
- [ ] Privileged access removed
- [ ] Appropriate CRM access verified
- [ ] Updated permissions captured after changes
- [ ] Change ticket and timestamps recorded
- [ ] Residual risk reassessed
- [ ] Finding formally closed by an authorised owner

## Expected Security Outcome
Removal of unjustified administrative privileges would reduce the potential impact of account compromise and strengthen least-privilege enforcement.

## Current Project Status
This document is a proposed remediation plan. No live permissions have been changed, no actual remediation evidence has been collected, and the finding remains open.

## Project Scope
This exercise uses fictional employee identities and simulated IAM findings for cybersecurity portfolio development.
