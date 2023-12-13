from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from car import Base, Car
from customer import Customer
from transaction import Transaction

engine = create_engine('sqlite:///dealership.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

def add_car(model, year, in_stock, sold_out):
    car = Car(model=model, year=year, in_stock=in_stock, sold_out=sold_out)
    session.add(car)
    session.commit()
    print(f"Car '{model}' added successfully.")

def add_customer(name):
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' added successfully.")

def make_transaction(car_id, customer_id):
    car = session.query(Car).filter_by(id=car_id).first()
    customer = session.query(Customer).filter_by(id=customer_id).first()

    if car and customer:
        transaction = Transaction(car_id=car_id, customer_id=customer_id)
        session.add(transaction)
        car.in_stock -= 1
        car.sold_out += 1
        session.commit()
        print(f"Transaction successful: {customer.name} bought {car.model}.")
    else:
        print("Invalid car or customer ID.")

def display_inventory():
    cars = session.query(Car).all()
    print("Car Inventory:")
    for car in cars:
        print(f"{car.id}. {car.model} ({car.year}): In Stock: {car.in_stock}, Sold Out: {car.sold_out}")

def display_customers():
    customers = session.query(Customer).all()
    print("Customers:")
    for customer in customers:
        print(f"{customer.id}. {customer.name}")

if __name__ == "__main__":
    print("done")
