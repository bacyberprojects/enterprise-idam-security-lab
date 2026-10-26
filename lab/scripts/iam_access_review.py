
import csv
from pathlib import Path

# Locate the CSV files relative to this script.
DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"

# Approved permissions from the SCFS RBAC matrix.
RBAC_RULES = {
    "IT Administrator": {
        ("IT Administration", "Admin")
    },
    "Finance Officer": {
        ("Finance System", "Read/Write")
    },
    "HR Officer": {
        ("HR System", "Read/Write")
    },
    "Operations Officer": {
        ("CRM", "Read"),
        ("Operations System", "Read/Write")
    },
    "Customer Service Officer": {
        ("CRM", "Read/Write")
    }
}


def read_csv(filename):
    """Read a CSV file and return its records."""
    filepath = DATA_FOLDER / filename

    with filepath.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def review_access():
    employees = read_csv("employees.csv")
    permissions = read_csv("access_permissions.csv")
    identity_accounts = read_csv("identity_accounts.csv")
    session_records = read_csv("identity_sessions.csv")


    # Match each employee ID to their HR record.
    employee_lookup = {
        employee["Employee_ID"]: employee
        for employee in employees
    }
    # Match each identity account to its employee ID.
    identity_lookup = {
    account["Employee_ID"]: account
    for account in identity_accounts

    }

    findings = []
    # Check identity accounts against HR employment status.
    for employee in employees:
        employee_id = employee["Employee_ID"]
        employment_status = employee["Status"]

        identity = identity_lookup.get(employee_id)

        if employment_status == "Terminated":
            if identity is None:
                findings.append(
                    (employee_id, "IDENTITY VERIFICATION GAP",
                     "Terminated employee has no identity account record")
                )

            elif identity["Account_Status"] == "Enabled":
                findings.append(
                    (employee_id, "LEAVER IDENTITY RISK",
                     "Terminated employee has an enabled identity account")
                )


    # Check sessions and refresh tokens for terminated employees.
    
    
    for session in session_records:
        employee_id = session["Employee_ID"]
        employee = employee_lookup.get(employee_id)

        if employee is None:
            findings.append(
                (employee_id, "UNKNOWN SESSION IDENTITY",
                 "Session belongs to an employee not in the HR register")
            )
            continue

        if employee["Status"] == "Terminated":
            if session["Session_Status"] == "Active":
                findings.append(
                    (employee_id, "LEAVER SESSION RISK",
                     "Terminated employee retains an active session")
                )

            if session["Refresh_Token_Status"] == "Active":
                findings.append(
                    (employee_id, "LEAVER TOKEN RISK",
                     "Terminated employee retains an active refresh token")
                )
    for access in permissions:
        employee_id = access["Employee_ID"]
        application = access["Application"]
        permission = access["Permission"]

        employee = employee_lookup.get(employee_id)

        if employee is None:
            findings.append(
                (employee_id, "UNKNOWN IDENTITY",
                 "Access belongs to an employee not in the HR register")
            )
            continue

        role = employee["Role"]
        status = employee["Status"]
        granted_access = (application, permission)

        if status == "Terminated":
            findings.append(
                (employee_id, "LEAVER RISK",
                 f"Terminated employee retains {application} access")
            )

        elif status == "Transferred":
            findings.append(
                (employee_id, "MOVER REVIEW",
                 f"Validate {application} access against the new role")
            )

        elif granted_access not in RBAC_RULES.get(role, set()):
            findings.append(
                (employee_id, "RBAC VIOLATION",
                 f"{role} has {permission} access to {application}")
            )

    print("SCFS - IAM ACCESS REVIEW")
    print("=" * 60)
    print(f"Employees reviewed: {len(employees)}")
    print(f"Permission assignments reviewed: {len(permissions)}")
    print(f"Findings: {len(findings)}")
    print("=" * 60)

    for employee_id, finding_type, description in findings:
        print(f"{employee_id} | {finding_type} | {description}")

    print("\nReview completed. Findings require analyst validation.")


if __name__ == "__main__":
    review_access()
