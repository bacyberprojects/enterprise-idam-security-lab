
# IAM Security Remediation Report — EMP005

## 1. Case Information

- Organisation: Southern Cross Financial Services (SCFS)
- Case ID: IAM-001
- Employee ID: EMP005
- Employee Name: Liam Taylor
- Department: Customer Service
- Role: Customer Service Officer
- Risk Rating: Critical (20/25)
- Status: Remediation Proposed — Simulation

## 2. Confirmed Finding (Simulated)

The automated IAM access review identified that EMP005 had Admin access to the IT Administration system.

The approved RBAC matrix specifies that a Customer Service Officer requires CRM Read/Write access.

During simulated stakeholder validation:
- The Customer Service Manager confirmed that administrator access was not approved.
- The IT Application Owner found no approved access request or documented exception.

The finding is therefore treated as unauthorised privileged access in this fictional scenario.

## 3. Remediation Actions

1. Escalate the critical finding to the IAM Team and Security Manager.
2. Obtain authorisation to remove the inappropriate administrator permission.
3. Revoke EMP005's Admin access to the IT Administration system.
4. Verify that EMP005 has the correct CRM Read/Write access.
5. Review sign-in and administrative activity logs for potential misuse.
6. Check for other unnecessary privileged permissions.
7. Record the change ticket, approvals and supporting evidence.
8. Update the risk register following verification.

These are proposed simulated actions. No live account permissions have been changed.

## 4. Expected Access After Remediation

| Application | Expected Permission |
|---|---|
| IT Administration | No Access |
| CRM | Read/Write |

## 5. Verification Checklist

- [ ] Removal approved by authorised owner
- [ ] Administrator access revoked in simulation
- [ ] CRM Read/Write access verified
- [ ] Other privileged access reviewed
- [ ] Relevant activity logs assessed
- [ ] Change record documented
- [ ] Risk register updated
- [ ] Closure approved by risk owner

## 6. Current Outcome

Remediation is documented but not yet executed or verified.

The case remains open until simulated corrective actions and verification evidence are completed.

## 7. Project Disclaimer

This is a fictional IAM cybersecurity lab. All identities, stakeholder responses and remediation activities are simulated.
