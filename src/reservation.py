import json

class Reservation:
    """A class to manage reservation information and operations."""
    reservations = {}

    @staticmethod
    def load_reservations():
        """Load reservations from a file."""
        try:
            with open('reservations.json', 'r') as file:
                Reservation.reservations = json.load(file)
        except FileNotFoundError:
            Reservation.reservations = {}

    @staticmethod
    def save_reservations():
        """Save reservations to a file."""
        with open('reservations.json', 'w') as file:
            json.dump(Reservation.reservations, file, indent=4)

    @classmethod
    def create_reservation(cls, reservation_id: int, hotel_id: int, customer_id: int, check_in: str, check_out: str):
        """Create a new reservation and add it to the reservations dictionary."""
        cls.load_reservations()
        if str(reservation_id) in cls.reservations:
            print(f"Reservation with id {reservation_id} already exists.")
            return
        cls.reservations[str(reservation_id)] = {
            "hotel_id": hotel_id,
            "customer_id": customer_id,
            "check_in": check_in,
            "check_out": check_out
        }
        cls.save_reservations()
        print(f"Reservation {reservation_id} created successfully.")

    @classmethod
    def cancel_reservation(cls, reservation_id: int):
        """Cancel a specific reservation and remove it from the reservations dictionary."""
        cls.load_reservations()
        if str(reservation_id) in cls.reservations:
            del cls.reservations[str(reservation_id)]
            cls.save_reservations()
            print(f"Reservation {reservation_id} canceled successfully.")
        else:
            print(f"Reservation with id {reservation_id} does not exist.")
