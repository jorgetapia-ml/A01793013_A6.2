"""Hotel module"""
import json

class Hotel:
    """A class to manage hotel information and operations."""
    hotels = {}

    @staticmethod
    def load_hotels():
        """Load hotels from a file."""
        try:
            with open('hotels.json', 'r', encoding="utf8") as file:
                Hotel.hotels = json.load(file)
        except FileNotFoundError:
            Hotel.hotels = {}

    @staticmethod
    def save_hotels():
        """Save hotels to a file."""
        with open('hotels.json', 'w', encoding="utf8") as file:
            json.dump(Hotel.hotels, file, indent=4)

    @classmethod
    def create_hotel(cls, hotel_id: int, name: str, location: str):
        """Create a new hotel and add it to the hotels dictionary."""
        cls.load_hotels()
        if str(hotel_id) in cls.hotels:
            print(f"Hotel with id {hotel_id} already exists.")
            return
        cls.hotels[str(hotel_id)] = {"name": name, "location": location}
        cls.save_hotels()
        print(f"Hotel {name} created successfully.")

    @classmethod
    def delete_hotel(cls, hotel_id: int):
        """Delete a hotel from the hotels dictionary."""
        cls.load_hotels()
        if str(hotel_id) in cls.hotels:
            del cls.hotels[str(hotel_id)]
            cls.save_hotels()
            print(f"Hotel {hotel_id} deleted successfully.")
        else:
            print(f"Hotel with id {hotel_id} does not exist.")

    @classmethod
    def show_hotel_info(cls, hotel_id: int):
        """Print information of a specific hotel."""
        cls.load_hotels()
        if str(hotel_id) in cls.hotels:
            hotel = cls.hotels[str(hotel_id)]
            print(f"Hotel ID: {hotel_id}, Name: {hotel['name']}, Location: {hotel['location']}")
        else:
            print(f"Hotel with id {hotel_id} does not exist.")

    @classmethod
    def update_hotel_info(cls, hotel_id: int, name: str = None, location: str = None):
        """Update information of a specific hotel."""
        cls.load_hotels()
        if str(hotel_id) in cls.hotels:
            if name:
                cls.hotels[str(hotel_id)]["name"] = name
            if location:
                cls.hotels[str(hotel_id)]["location"] = location
            cls.save_hotels()
            print(f"Hotel {hotel_id} updated successfully.")
        else:
            print(f"Hotel with id {hotel_id} does not exist.")
