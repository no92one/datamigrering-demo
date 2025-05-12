from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ssn = Column(String, nullable=False, unique=True)
    accounts = relationship('Account', back_populates='customer')
    email = Column(String)

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True)
    balance = Column(Numeric, default=0, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="accounts")
