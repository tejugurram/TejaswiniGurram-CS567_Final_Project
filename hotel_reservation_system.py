import json
from datetime import datetime

class HotelReservationSystem:
    def __init__(self, filename='bookings.json'):
        self.filename = filename
        self.bookings = self.load_bookings()
        self.room_rates = {'standard': 100}  # Define room rates here

    def load_bookings(self):
        try:
            with open(self.filename, 'r') as file:
                bookings = json.load(file)
                return {key: {k: datetime.strptime(bookings[key][k], "%Y-%m-%d") for k in bookings[key]} for key in bookings}
        except FileNotFoundError:
            return {}

    def save_bookings(self):
        with open(self.filename, 'w') as file:
            bookings = {key: {k: self.bookings[key][k].strftime("%Y-%m-%d") for k in self.bookings[key]} for key in self.bookings}
            json.dump(bookings, file, indent=4)

    def check_availability(self, check_in_date, check_out_date):
        check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
        for dates in self.bookings.values():
            if check_in <= dates['check_out'] and check_out >= dates['check_in']:
                print("Room is not available for the selected dates.")
                return False
        print("Room is available.")
        return True

    def calculate_total_cost(self, check_in_date, check_out_date, room_type='standard'):
        check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
        duration = (check_out - check_in).days
        if duration <= 0:
            return 0
        return duration * self.room_rates.get(room_type, 0)

    def book_room(self, room_number, check_in_date, check_out_date):
        if self.check_availability(check_in_date, check_out_date):
            self.bookings[room_number] = {
                'check_in': datetime.strptime(check_in_date, "%Y-%m-%d"),
                'check_out': datetime.strptime(check_out_date, "%Y-%m-%d")
            }
            self.save_bookings()
            print(f"Room {room_number} booked from {check_in_date} to {check_out_date}.")
            return True
        return False

    def modify_reservation(self, room_number, new_check_in_date, new_check_out_date):
        if room_number in self.bookings:
            if self.check_availability(new_check_in_date, new_check_out_date):
                self.bookings[room_number]['check_in'] = datetime.strptime(new_check_in_date, "%Y-%m-%d")
                self.bookings[room_number]['check_out'] = datetime.strptime(new_check_out_date, "%Y-%m-%d")
                self.save_bookings()
                print(f"Reservation for room {room_number} has been modified.")
                return True
            else:
                print("Room is not available for the selected dates.")
                return False
        else:
            print("No reservation found for the specified room.")
            return False

    def cancel_reservation(self, room_number):
        if room_number in self.bookings:
            del self.bookings[room_number]
            self.save_bookings()
            print(f"Reservation for room {room_number} has been cancelled.")
            return True
        print("No reservation found for the specified room.")
        return False

    def list_bookings(self):
        if not self.bookings:
            print("No bookings found.")
            return
        for room, dates in self.bookings.items():
            print(f"Room {room} is booked from {dates['check_in'].strftime('%Y-%m-%d')} to {dates['check_out'].strftime('%Y-%m-%d')}")

def main():
    system = HotelReservationSystem()
    while True:
        print("\nHotel Reservation System Options:")
        print("1. Check Room Availability")
        print("2. Book Room")
        print("3. Modify Reservation")
        print("4. Cancel Reservation")
        print("5. List All Bookings")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            system.check_availability(check_in_date, check_out_date)
        elif choice == '2':
            room_number = input("Enter room number to book: ")
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            system.book_room(room_number, check_in_date, check_out_date)
        elif choice == '3':
            room_number = input("Enter room number to modify reservation: ")
            new_check_in_date = input("Enter new check-in date (YYYY-MM-DD): ")
            new_check_out_date = input("Enter new check-out date (YYYY-MM-DD): ")
            system.modify_reservation(room_number, new_check_in_date, new_check_out_date)
        elif choice == '4':
            room_number = input("Enter room number to cancel reservation: ")
            system.cancel_reservation(room_number)
        elif choice == '5':
            system.list_bookings()
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
