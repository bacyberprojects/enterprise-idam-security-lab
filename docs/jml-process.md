# Joiner–Mover–Leaver (JML) Identity Lifecycle Process

## Organisation
Southern Cross Financial Services (SCFS)

## Objective
Ensure employee access is provisioned, updated and removed securely throughout the employment lifecycle, following least privilege and the approved RBAC matrix.

## 1. Joiner Process
1. HR confirms the new employee's identity, role, department and start date.
2. The department manager submits and approves the required access request.
3. The IAM team creates the employee identity in Microsoft Entra ID or the simulated identity directory.
4. The IAM team assigns approved application access according to the RBAC matrix.
5. MFA is enabled where applicable and onboarding instructions are provided securely.
6. The IAM team verifies access and records the approval and provisioning evidence.

## 2. Mover Process
1. HR notifies the IAM team of the employee's department or role change and effective date.
2. The manager and application owners review existing and required permissions.
3. Unnecessary access from the previous role is removed and approved new access is assigned.
4. Any privileged access is reviewed separately.
5. The IAM team verifies the updated permissions and records the changes.

## 3. Leaver Process
1. HR confirms the employee's departure and authorised access termination time.
2. The IAM team disables sign-in at the approved termination time, or immediately if overdue.
3. Active sessions are revoked and relevant application, VPN and privileged access is removed.
4. Other accounts, credentials and tokens are reviewed for deactivation or revocation.
5. Required business data and records are retained according to policy.
6. The IAM team verifies deprovisioning and records the completion evidence.
7. Any unexpected post-departure access is escalated for investigation.

## Roles and Responsibilities
| Stakeholder | Responsibility |
|---|---|
| HR | Notify joiner, mover and leaver events |
| Department Manager | Confirm business access requirements and approvals |
| Application Owner | Approve access to sensitive applications |
| IAM Team | Provision, modify, disable and verify access |
| Security Team | Monitor exceptions and investigate suspicious activity |

## Security Principles
- Least privilege and role-based access control (RBAC)
- Documented approvals and segregation of duties
- Multi-factor authentication (MFA)
- Timely provisioning and deprovisioning
- Periodic access reviews and audit evidence

## Project Scope
This document describes a proposed JML process for a fictional organisation. It does not represent a live Microsoft Entra ID deployment.
