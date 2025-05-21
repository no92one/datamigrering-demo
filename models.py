from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ssn = Column(String, nullable=False, unique=True)
    email = Column(String)

    accounts = relationship('Account', back_populates='customer')

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True)
    balance = Column(Numeric, default=0, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    __table_args__ = (
        CheckConstraint("balance >= 0", name="balance_not_negative_check"),
        CheckConstraint("balance <= 5000000", name="max_balance_check"),
    )

    customer = relationship("Customer", back_populates="accounts")
