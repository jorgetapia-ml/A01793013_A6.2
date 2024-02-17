"""unittest module"""
import unittest
import os
import io
from hostelry_module import Hotel, Customer, Reservation
from unittest.mock import patch

class TestHotelManagementSystem(unittest.TestCase):
    """
    Test cases for the hotel management system, including Hotel, Customer,
    and Reservation classes.

    """

    @classmethod
    def setUpClass(cls):
        """Prepares the environment for tests, cleaning up JSON files."""
        if os.path.exists('hotels.json'):
            os.remove('hotels.json')
        if os.path.exists('customers.json'):
            os.remove('customers.json')
        if os.path.exists('reservations.json'):
            os.remove('reservations.json')

    @classmethod
    def tearDownClass(cls):
        """Cleans up the environment after tests, removing JSON files."""
        if os.path.exists('hotels.json'):
            os.remove('hotels.json')
        if os.path.exists('customers.json'):
            os.remove('customers.json')
        if os.path.exists('reservations.json'):
            os.remove('reservations.json')

    def test_create_hotel(self):
        """Test creating a new hotel and verifying it exists in the system."""
        Hotel.create_hotel(1, "Test Hotel", "Test Location")
        Hotel.load_hotels()
        self.assertIn('1', Hotel.hotels)

    def test_delete_hotel(self):
        """Test deleting an existing hotel from the system."""
        Hotel.create_hotel(2, "Delete Hotel", "Delete Location")
        Hotel.delete_hotel(2)
        Hotel.load_hotels()
        self.assertNotIn('2', Hotel.hotels)

    def test_show_hotel(self):
        """Test that show_hotel_info prints the correct information."""
        Hotel.create_hotel(3, "Grand Plaza", "Downtown")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            Hotel.show_hotel_info(3)
            Hotel.show_hotel_info(4)
            self.assertIn("Grand Plaza", fake_out.getvalue())
            self.assertIn("Downtown", fake_out.getvalue())
            self.assertIn("does not exist.", fake_out.getvalue())
        Hotel.delete_hotel(3)

    def test_create_customer(self):
        """Test creating a new customer and verifying it exists in the system."""
        Customer.create_customer(1, "Test Customer", "test@customer.com")
        Customer.load_customers()
        self.assertIn('1', Customer.customers)

    def test_delete_customer(self):
        """Test deleting an existing customer from the system."""
        Customer.create_customer(2, "Delete Customer", "delete@customer.com")
        Customer.delete_customer(2)
        Customer.delete_customer(3)
        Customer.load_customers()
        self.assertNotIn('2', Customer.customers)

    def test_create_reservation(self):
        """Test creating a new reservation and verifying it exists in the system."""
        Hotel.create_hotel(1, "Reservation Hotel", "Reservation Location")
        Customer.create_customer(1, "Reservation Customer", "reservation@customer.com")
        Reservation.create_reservation(1, 1, 1, "2024-01-01", "2024-01-05")
        Reservation.load_reservations()
        self.assertIn('1', Reservation.reservations)

    def test_cancel_reservation(self):
        """Test canceling an existing reservation in the system."""
        Reservation.cancel_reservation(1)
        Reservation.load_reservations()
        self.assertNotIn('1', Reservation.reservations)

if __name__ == '__main__':
    unittest.main()
