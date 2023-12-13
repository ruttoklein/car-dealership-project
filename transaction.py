from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    car = relationship('Car', back_populates='transactions')
    customer = relationship('Customer', back_populates='transactions')
