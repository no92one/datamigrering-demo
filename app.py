from db import init_db, SessionLocal
from models import Customer, Account

def main():
    init_db()
    db = SessionLocal()

    customer = Customer(name="Benjamin", ssn="7001092456", email="benjamin@example.com")
    db.add(customer)
    db.commit()

    account = Account(number="8064047892", balance=200, customer_id=customer.id)
    db.add(account)
    db.commit()

    print(f"{customer.name} ({customer.email}) har saldo {account.balance}")

    db.close()

if __name__ == "__main__":
    main()