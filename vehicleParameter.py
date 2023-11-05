#!/usr/bin/env python3

from math import pi
from ev3dev2.wheel import Wheel


class VehicleParameter:

    # Parameter vom Fahrzeug in MM!
    # Raddurchmesser
    diaWheel = 39
    # Übersetzung
    gearing = 1
    # Breite von Mitte linkes Rad bis Mitte rechtes Rad
    wheelDistance = 185
    # 100 % = 175 U/min - (Bei 360 Schritten pro Umdrehung = 1050 Schritte bei 100 % = 2,916 U/sec)
    motorMaxSpeed = 175
    # Motorschritte bei einer Umdrehung
    motorDegrees = 360
    # Streckenkorrektur
    routeError = 30

    def __int__(self, diaWheel, gearing, trackWidth, wheelBase, motorMaxSpeed, wheelSpeed,
                motorDegrees, routeError):
        self.diaWheel = diaWheel
        self.gearing = gearing
        self.trackWidth = trackWidth
        self.motorMaxSpeed = motorMaxSpeed
        self.wheelBase = wheelBase
        self.motorDegrees = motorDegrees
        self.routeError = routeError

    # Verfahrweg (MM) in Motorschritte umrechnen. Radumfang (MM); Übersetzung und Streckenkorrektur in Formel.
    def distance_track(self, distanceTrack):
        driveMotorDegrees = (((float(distanceTrack) + self.routeError) * self.motorDegrees) /
                             (float(self.diaWheel) * pi)) * self.gearing
        return driveMotorDegrees

    # Geschwindigkeit am Rad berechnen in %; Input ist U/min; max. 175 U/min
    def wheel_speed(self, wheelSpeed):
        speedWheel = float(wheelSpeed) * 100/(self.motorMaxSpeed/self.gearing)
        return speedWheel

    def home_route(self, xValue, yValue):
        xyValue = xValue + yValue
        return xyValue


class Ev3TireBrickPi(Wheel):
    def __init__(self):

        Wheel. __init__(self, diameter_mm=VehicleParameter.diaWheel, width_mm=VehicleParameter.wheelDistance)
