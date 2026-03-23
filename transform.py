import csv
from pathlib import Path
from typing import Any, Dict

# Define paths using pathlib for OS-agnostic compatibility
SOURCE_FILE = Path("./users.csv")
DESTINATION_FILE = Path("./users_transformado.csv")

FIELDNAMES = [
    "id",
    "password",
    "last_login",
    "is_superuser",
    "username",
    "first_name",
    "last_name",
    "email",
    "is_staff",
    "is_active",
    "date_joined",
    "name",
    "email_verified_at",
    "role",
    "remember_token",
    "created_at",
    "updated_at",
    "deleted_at",
]


def format_datetime_to_utc(date_str: str) -> str:
    """
    Appends the UTC offset to a naive datetime string.
    Returns an empty string if the input is empty or None.
    """
    if not date_str:
        return ""

    # Defensive check: if it already has an offset, return it as is
    if "+" in date_str or "Z" in date_str:
        return date_str

    return f"{date_str}+00:00"


def transform_user_row(row: Dict[str, Any]) -> Dict[str, Any]:
    """
    Applies business rules to transform a single Laravel user row
    into a Django-compatible user row.
    """
    password_original = row.get("password", "")
    password_modified = f"bcrypt${password_original}" if password_original else ""

    # Process dates once to use in multiple places
    created_at_utc = format_datetime_to_utc(row.get("created_at", ""))

    return {
        "id": row.get("id"),
        "password": password_modified,
        "last_login": None,
        "is_superuser": "f",
        "username": row.get("email"),
        "first_name": row.get("name", "").split(" ")[0] if row.get("name") else "",
        "last_name": " ",
        "email": row.get("email"),
        "is_staff": "f",
        "is_active": "t",
        "date_joined": created_at_utc,
        "name": row.get("name"),
        "email_verified_at": format_datetime_to_utc(row.get("email_verified_at", "")),
        "role": row.get("role"),
        "remember_token": row.get("remember_token"),
        "created_at": created_at_utc,
        "updated_at": format_datetime_to_utc(row.get("updated_at", "")),
        "deleted_at": format_datetime_to_utc(row.get("deleted_at", "")),
    }


def main() -> None:
    """Main execution function to handle file I/O."""
    with SOURCE_FILE.open(mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        with DESTINATION_FILE.open(mode="w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=FIELDNAMES)
            writer.writeheader()

            for row in reader:
                transformed_row = transform_user_row(row)
                writer.writerow(transformed_row)

    print(
        f"¡Éxito! Se ha generado '{DESTINATION_FILE}' con las contraseñas y fechas actualizadas."
    )


if __name__ == "__main__":
    main()
