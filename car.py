from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    in_stock = Column(Integer)
    sold_out = Column(Integer)

    transactions = relationship('Transaction', back_populates='car')
