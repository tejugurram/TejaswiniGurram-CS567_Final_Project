import unittest
import coverage
from test_hotel_reservation_system import TestHotelReservationSystem

test_suite = unittest.TestLoader().loadTestsFromTestCase(TestHotelReservationSystem)

test_runner = unittest.TextTestRunner()

cov = coverage.Coverage()
cov.start()

result = test_runner.run(test_suite)

cov.stop()

cov.report()
