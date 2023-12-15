from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True,autoincrement=True )
    car_id = Column(Integer, ForeignKey('cars.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    