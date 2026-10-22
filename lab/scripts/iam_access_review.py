
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

    # Match each employee ID to their HR record.
    employee_lookup = {
        employee["Employee_ID"]: employee
        for employee in employees
    }

    findings = []

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
