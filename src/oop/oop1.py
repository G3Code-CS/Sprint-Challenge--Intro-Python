# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#   BASE CLASS - VEHICLE
class Vehicle:
    pass

#   FLIGHTVEHICLE IS A SUBCLASS OF VEHICLE
class FlightVehicle(Vehicle):
    pass

#   STARSHIP IS A SUBCLASS OF FLIGHT VEHICLE
class Starship(FlightVehicle):
    pass

#   GROUNDVEHICLE IS A SUBCLASS OF VEHICLE
class GroundVehicle(Vehicle):
    pass

#   AIRPLANE IS A SUBCLASS OF FLIGHTVEHICLE
class Airplane(FlightVehicle):
    pass

#   CAR IS A SUBCLASS OF GROUNDVEHICLE
class Car(GroundVehicle):
    pass

#   MOTORCYCLE IS A SUBCLASS OF GROUNDVEHICLE
class Motorcycle(GroundVehicle):
    pass
