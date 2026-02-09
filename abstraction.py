from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def brakes(self):
        print("brakes are applied")


class car(vehicle):
    def start_engine(self):
        print("car engine started")


class bus(vehicle):
    def start_engine(self):
        print("bus engine started")


class bike(vehicle):
    def start_engine(self):
        print("bike engine started")


# Creating objects
c = car()
b = bike()

# Calling methods
b.start_engine()
b.brakes()
