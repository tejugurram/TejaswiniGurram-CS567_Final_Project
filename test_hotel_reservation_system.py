import unittest
from datetime import datetime
from hotel_reservation_system import HotelReservationSystem

class TestHotelReservationSystem(unittest.TestCase):
    def setUp(self):
        self.system = HotelReservationSystem('test_bookings.json')

    def tearDown(self):
        self.system = None

    def test_check_availability(self):
        self.assertTrue(self.system.check_availability('2024-06-01', '2024-06-05'))

        self.system.book_room('101', '2024-06-10', '2024-06-15')
        self.assertFalse(self.system.check_availability('2024-06-12', '2024-06-14'))

    def test_book_room(self):
        self.assertTrue(self.system.book_room('102', '2024-07-01', '2024-07-05'))

        self.assertFalse(self.system.book_room('101', '2024-07-03', '2024-07-08'))

    def test_modify_reservation(self):
        self.system.book_room('103', '2024-08-01', '2024-08-05')
        self.assertTrue(self.system.modify_reservation('103', '2024-08-02', '2024-08-06'))

        self.assertFalse(self.system.modify_reservation('105', '2024-08-02', '2024-08-06'))

    def test_cancel_reservation(self):
        self.system.book_room('104', '2024-09-01', '2024-09-05')
        self.assertTrue(self.system.cancel_reservation('104'))

        self.assertFalse(self.system.cancel_reservation('106'))

    def test_calculate_total_cost(self):
        self.assertEqual(self.system.calculate_total_cost('2024-10-01', '2024-10-05', 'standard'), 400)

        self.assertEqual(self.system.calculate_total_cost('2024-10-05', '2024-10-01', 'standard'), 0)

if __name__ == '__main__':
    unittest.main()
