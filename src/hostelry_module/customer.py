""" Customer mdoule"""
import json


class Customer:
    """A class to manage customer information and operations."""
    customers = {}

    @staticmethod
    def load_customers():
        """Load customers from a file."""
        try:
            with open('customers.json', 'r', encoding="utf8") as file:
                Customer.customers = json.load(file)
        except FileNotFoundError:
            Customer.customers = {}

    @staticmethod
    def save_customers():
        """Save customers to a file."""
        with open('customers.json', 'w', encoding="utf8") as file:
            json.dump(Customer.customers, file, indent=4)

    @classmethod
    def create_customer(cls, customer_id: int, name: str, email: str):
        """Create a new customer and add them to the customers dictionary."""
        cls.load_customers()
        if str(customer_id) in cls.customers:
            print(f"Customer with id {customer_id} already exists.")
            return
        cls.customers[str(customer_id)] = {"name": name, "email": email}
        cls.save_customers()
        print(f"Customer {name} created successfully.")

    @classmethod
    def delete_customer(cls, customer_id: int):
        """Delete a customer from the customers dictionary."""
        cls.load_customers()
        if str(customer_id) in cls.customers:
            del cls.customers[str(customer_id)]
            cls.save_customers()
            print(f"Customer {customer_id} deleted successfully.")
        else:
            print(f"Customer with id {customer_id} does not exist.")

    @classmethod
    def show_customer_info(cls, customer_id: int):
        """Print information of a specific customer."""
        cls.load_customers()
        if str(customer_id) in cls.customers:
            customer = cls.customers[str(customer_id)]
            print(
                f"Customer ID: {customer_id},",
                f"Name: {customer['name']}, Email: {customer['email']}")
        else:
            print(f"Customer with id {customer_id} does not exist.")

    @classmethod
    def update_customer_info(cls, customer_id: int,
                             name: str = None, email: str = None):
        """Update information of a specific customer."""
        cls.load_customers()
        if str(customer_id) in cls.customers:
            if name:
                cls.customers[str(customer_id)]["name"] = name
            if email:
                cls.customers[str(customer_id)]["email"] = email
            cls.save_customers()
            print(f"Customer {customer_id} updated successfully.")
        else:
            print(f"Customer with id {customer_id} does not exist.")
