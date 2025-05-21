from db import init_db, SessionLocal
from models import Customer, Account
from sqlalchemy.exc import SQLAlchemyError
import csv

def main():
    init_db()
    db = SessionLocal()

    #try:
        #with db.begin():
            #with open('customers.csv', newline='') as csvfile:
                #reader = csv.DictReader(csvfile)
                #for index, row in enumerate(reader):
                    #customer = Customer(name=row["name"], ssn=row["ssn"], email=row["email"])
                    #db.add(customer)

    #except SQLAlchemyError as e:
        #db.rollback()
        #print("[ERROR] Något gick fel:", e)

    #try:
        #with db.begin():
           #customer = Customer(name="Benjamin", ssn="7001092456", email="benjamin@example.com")
            #db.add(customer)

            #account = Account(number="8064047892", balance=200, customer_id=customer.id)
            #db.add(account)

    #except SQLAlchemyError as e:
        #db.rollback()
        #print("[ERROR] Något gick fel:", e)

    #print(f"{customer.name} ({customer.email}) har saldo {account.balance}")

    db.close()

if __name__ == "__main__":
    main()