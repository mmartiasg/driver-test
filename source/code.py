import math
TRIP_STATUS_ASSIGNED = "en curso"
TRIP_STATUS_COMPLETED = "completo"
TRIP_STATUS_PENDING = "solicitado"


class Driver:
    def __init__(self, driver_id, coordinates):
        if coordinates[0] < 0 or coordinates[1] < 0:
            raise Exception("Coordinates should be positive")

        self.driver_id = driver_id
        self.coordinates = coordinates

    def distance_to_passenger(self, passenger):
        if passenger.coordinates[0] < 0 or passenger.coordinates[1] < 0:
            raise Exception("Coordinates should be positive")

        return ((passenger.coordinates[0] - self.coordinates[0])**2
                + (passenger.coordinates[1] - self.coordinates[1])**2)**0.5


class Trip:
    def __init__(self, passenger):
        self.passenger = passenger
        self.driver = None
        self.status = TRIP_STATUS_ASSIGNED

    def findNearestDriver(self, available_drivers):
        """
        This method finds the driver closes in Euclidean distance to the passenger.
        It does not have into account the distance based on the real distance;
        based on the possible path between the passenger and the driver.

        This result is not correct but an approximation of the distance between the passenger and the driver
        This should take into account the possible route and corrected by the curvature of the Earth.

        This method has a O(n) time complexity.

        :param available_drivers: all drivers available at that time.
        :return: Closes driver
        """

        min_distance = math.inf
        selected_driver = None

        if available_drivers is None or len(available_drivers) == 0:
            return None

        for driver in available_drivers:
            distance = driver.distance_to_passenger(self.passenger)
            if distance < min_distance:
                min_distance = distance
                selected_driver = driver

        return selected_driver

    def assign_driver(self, available_drivers):
        """
        This method assigns the driver to the trip based on the distance between the driver and the passenger.
        if a driver is found the state is changed to ASSIGNED.

        :param available_drivers: all available drivers available at that time.
        :return: selected driver
        """
        self.driver = self.findNearestDriver(available_drivers)

        if self.driver is None:
            self.status = TRIP_STATUS_ASSIGNED

        return self.driver


class Passenger:
    def __init__(self, passenger_id, coordinates):
        self.passenger_id = passenger_id
        self.coordinates = coordinates
