import csv


def transform_users_csv(input_filepath: str, output_filepath: str) -> None:
    """
    Reads the original users CSV, applies transformations, and outputs
    a new CSV that strictly matches the PostgreSQL table column order.
    """
    # This list now matches the exact order from your '\d users' output
    db_columns = [
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
        "role",
        "created_at",
        "deleted_at",
        "email_verified_at",
        "name",
        "remember_token",
        "updated_at",
    ]

    with open(input_filepath, mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        with open(output_filepath, mode="w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=db_columns)
            writer.writeheader()

            for row in reader:
                # 1. Transform password
                password_original = row.get("password", "")
                password_modificada = (
                    f"bcrypt${password_original}" if password_original else ""
                )

                # 2. Safely extract names
                full_name = row.get("name", "").strip()
                first_name = full_name.split(" ")[0] if full_name else ""

                # 3. Map data exactly to the db_columns order
                nueva_fila = {
                    "id": row.get("id"),
                    "password": password_modificada,
                    "last_login": None,
                    "is_superuser": "f",
                    "username": row.get("email"),
                    "first_name": first_name,
                    "last_name": " ",
                    "email": row.get("email"),
                    "is_staff": "f",
                    "is_active": "t",
                    "date_joined": row.get("created_at"),
                    "role": row.get("role"),
                    "created_at": row.get("created_at"),
                    "deleted_at": row.get("deleted_at"),
                    "email_verified_at": row.get("email_verified_at"),
                    "name": full_name,
                    "remember_token": row.get("remember_token"),
                    "updated_at": row.get("updated_at"),
                }
                writer.writerow(nueva_fila)


if __name__ == "__main__":
    archivo_origen = "./users.csv"
    archivo_destino = "./users_transformado.csv"

    transform_users_csv(archivo_origen, archivo_destino)
    print(
        f"Success! '{archivo_destino}' generated with the exact database schema order."
    )
