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


class Vehicle:
    pass

#Vehicle is base class
class FlightVehicle(Vehicle):
    pass

#Flightvehicle is base class
class Starship(FlightVehicle):
    pass

#Flightvehicle is base class
class Airplane(FlightVehicle):
    pass

#Vehicle base class
class GroundVehicle(Vehicle):
    pass

#Groundvehicle base class
class Motorcycle(GroundVehicle):
    pass

#Groundvehicle base class
class Car(GroundVehicle):
    pass