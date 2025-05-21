from db import init_db, SessionLocal
from models import Customer, Account
from sqlalchemy.exc import SQLAlchemyError
import csv
from datetime import datetime

# def main():
#     init_db()
#     db = SessionLocal()
#
#     print(datetime.strptime("2025-06-07 21:00:00", "%y-%m-%d %H:%M:%S").date())
#
#     try:
#         with db.begin():
#             with open('customers.csv', newline='') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for index, row in enumerate(reader):
#                     customer = Customer(name=row["name"], ssn=row["ssn"], email=row["email"])
#                     db.add(customer)
#
#     except SQLAlchemyError as e:
#         db.rollback()
#         print("[ERROR] Något gick fel:", e)
#
#     # try:
#     #     with db.begin():
#     #        customer = Customer(name="Benjamin", ssn="7001092456", email="benjamin@example.com")
#     #         db.add(customer)
#     #
#     #         account = Account(number="8064047892", balance=200, customer_id=customer.id)
#     #         db.add(account)
#     #
#     # except SQLAlchemyError as e:
#     #     db.rollback()
#     #     print("[ERROR] Något gick fel:", e)
#     #
#     # print(f"{customer.name} ({customer.email}) har saldo {account.balance}")
#
#     db.close()
#
# if __name__ == "__main__":
#     main()

from prefect import flow, task
import random


@task
def get_customer_ids() -> list[str]:
    # Fetch customer IDs from a database or API
    return [f"customer{n}" for n in random.choices(range(100), k=10)]


@task
def process_customer(customer_id: str) -> str:
    # Process a single customer
    return f"Processed {customer_id}"


@flow
def main() -> list[str]:
    customer_ids = get_customer_ids()
    # Map the process_customer task across all customer IDs
    results = process_customer.map(customer_ids)
    return results


if __name__ == "__main__":
    main()