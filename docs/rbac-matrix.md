# Role-Based Access Control (RBAC) Matrix

## Organisation
Southern Cross Financial Services (SCFS)

## Objective
Ensure employees receive only the access
permissions required for their job
responsibilities, following the principle
of least privilege.

## Access Levels
- **No Access:** Access is not permitted.
- **Read:** View authorised information.
- **Read/Write:** View and modify authorised data.
- **Admin:** Manage designated application settings.

## Proposed RBAC Matrix

| Job Role | Finance System | HR System | CRM | Operations System | IT Administration |
|---|---|---|---|---|---|
| IT Administrator | No Access | No Access | No Access | No Access | Admin |
| Finance Officer | Read/Write | No Access | No Access | No Access | No Access |
| HR Officer | No Access | Read/Write | No Access | No Access | No Access |
| Operations Officer | No Access | No Access | Read | Read/Write | No Access |
| Customer Service Officer | No Access | No Access | Read/Write | No Access | No Access |

## Security Principles
1. Apply least privilege.
2. Assign access based on job responsibilities.
3. Require approval for access changes.
4. Review access periodically.
5. Remove unnecessary access during JML.
6. Separate privileged administrative accounts.

## Assumptions
This is a proposed model for a fictional
organisation. Permissions require validation
by application owners before implementation.
