from prefect import flow, task
from db import init_db, SessionLocal
from models import Customer, Account
from sqlalchemy.exc import SQLAlchemyError
import csv

@task
def read_csv(filname):
    with open(filname, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


@task
def create_customers(data):
    db = SessionLocal()
    try:
        with db.begin():
            for row in data:
                customer = Customer(name=row['name'], ssn=row['ssn'], email=row['email'])
                db.add(customer)
    except SQLAlchemyError as e:
        db.rollback()
        print("[ERROR] Import misslyckades och har rullats tillbaka:", e)
    finally:
        db.close()

@task
def create_account_and_customer():
    db = SessionLocal()
    try:
        with db.begin():
            customer = Customer(name="Benjamin", ssn="7001090000", email="benjamin@example.com")
            db.add(customer)

            account = Account(number="8064047892", balance=200, customer_id=customer.id)
            db.add(account)

    except SQLAlchemyError as e:
        db.rollback()
        print("[ERROR] Något gick fel:", e)
    finally:
        db.close()


@flow
def main() -> list[str]:
    init_db()
    create_account_and_customer()
    data = read_csv("customers.csv")
    create_customers(data)


if __name__ == "__main__":
    main()
