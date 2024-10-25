import unittest
from source.code import Trip, Driver, Passenger, TRIP_STATUS_ASSIGNED, TRIP_STATUS_PENDING


class AssignDriversSuitCase(unittest.TestCase):
    def test_find_driver_with_id_one_when_multiple_drivers_available(self):
        passenger = Passenger(passenger_id="jose", coordinates=(1, 1))

        trip = Trip(passenger)

        drivers = [Driver("one", (0, 1)),
                   Driver("two", (10, 9)),
                   Driver("three", (25, 25))]

        driver = trip.findNearestDriver(available_drivers=drivers)

        self.assertTrue(driver.driver_id == "one")

    def test_when_no_drivers_available_finds_no_driver_then_returns_none(self):
        passenger = Passenger(passenger_id="jose", coordinates=(1, 1))

        trip = Trip(passenger)

        drivers = []

        driver = trip.findNearestDriver(available_drivers=drivers)

        self.assertEquals(driver, None)

    def test_find_driver_with_id_one_when_multiple_drivers_are_available_with_equal_distance_to_the_passenger(self):
        passenger = Passenger(passenger_id="jose", coordinates=(1, 1))

        trip = Trip(passenger)

        drivers = [Driver("one", (0, 1)),
                   Driver("two", (0, 1)),
                   Driver("three", (0, 1))]

        driver = trip.findNearestDriver(available_drivers=drivers)

        self.assertTrue(driver.driver_id == "one")

    def test_assigned_driver_with_id_one_to_trip_and_status_is_changed_to_assigned(self):
        passenger = Passenger(passenger_id="jose", coordinates=(1, 1))

        trip = Trip(passenger)

        drivers = [Driver("one", (0, 1)),
                   Driver("two", (10, 9)),
                   Driver("three", (25, 25))]

        driver = trip.assign_driver(drivers)

        self.assertTrue(driver.driver_id == "one")
        self.assertTrue(trip.status == TRIP_STATUS_ASSIGNED)

    def test_does_not_assign_a_driver_when_no_drivers_are_available_status_remains_pending(self):
        passenger = Passenger(passenger_id="jose", coordinates=(1, 1))

        trip = Trip(passenger)

        drivers = []

        driver = trip.assign_driver(drivers)

        self.assertEqual(driver, None)
        self.assertTrue(trip.status == TRIP_STATUS_PENDING)


if __name__ == '__main__':
    unittest.main()
