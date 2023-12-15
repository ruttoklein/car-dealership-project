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
    print(f"Car '{model}' added successfully with ID {car.id}.")

def add_customer(name):
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' added successfully with ID {customer.id}.")

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
    print("\nCar Inventory:")
    for car in cars:
        print(f"{car.id}. {car.model} ({car.year}): In Stock: {car.in_stock}, Sold Out: {car.sold_out}")

def display_customers():
    customers = session.query(Customer).all()
    print("\nCustomers:")
    for customer in customers:
        print(f"{customer.id}. {customer.name}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Car")
        print("2. Add Customer")
        print("3. Make Transaction")
        print("4. Display Inventory")
        print("5. Display Customers")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            model = input("Enter car model: ")
            year = input("Enter car year: ")
            in_stock = int(input("Enter quantity in stock: "))
            sold_out = 0
            add_car(model, year, in_stock, sold_out)
        elif choice == '2':
            name = input("Enter customer name: ")
            add_customer(name)
        elif choice == '3':
            car_id = int(input("Enter car ID: "))
            customer_id = int(input("Enter customer ID: "))
            make_transaction(car_id, customer_id)
        elif choice == '4':
            display_inventory()
        elif choice == '5':
            display_customers()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
