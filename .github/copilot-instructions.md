# Copilot instructions

## Project model

This repository is a fictional Southern Cross Financial Services (SCFS) IAM security lab. It models RBAC, least privilege, access reviews, and joiner-mover-leaver processes; it does not connect to or modify production systems or real employee accounts.

The Python access-review script reads four CSV datasets under
lab/data/: employees.csv, access_permissions.csv,
identity_accounts.csv, and identity_sessions.csv.

It checks role-based permissions, employee status,
identity account status, active sessions, and refresh tokens.

Findings require analyst validation, matches permission assignments to employee roles and statuses, and prints findings for analyst validation. The approved role-to-application permissions are represented both in `lab/scripts/iam_access_review.py` (`RBAC_RULES`) and in `docs/rbac-matrix.md`; keep these in sync when changing the model. The process and governance documents in `docs/` describe the intended controls, while `lab/investigations/`, `lab/remediation/`, and `lab/evidence/` hold simulated case records and evidence.

## Build, test, and lint

There is no build system, dependency manifest, configured test suite, or linter in this repository. The script uses only the Python standard library.

Run the access review from the repository root:

```sh
python3 lab/scripts/iam_access_review.py
```

There is currently no single-test command because no automated tests are configured. With the current simulated data, the review should report
50 employees, 59 permission assignments, and 2 findings
relating to EMP009 mover access.

These expected results should be updated whenever
the synthetic dataset or review logic changes.

## Data and review conventions

- Preserve the CSV column names and values: the script accesses fields by their exact headers, and role, status, application, and permission strings must match the model.
- Employee statuses are `Active`, `Transferred`, and `Terminated`. The review reports leavers and movers for validation rather than treating those records as ordinary RBAC comparisons.
- Findings are potential issues for analyst or stakeholder validation, not proof of misuse. Keep proposed actions, completed simulated remediation, and verified evidence clearly distinguished in case documents.
- Keep examples and evidence explicitly fictional and simulated. Do not introduce real credentials, personal data, or integrations that change live identities or permissions.
