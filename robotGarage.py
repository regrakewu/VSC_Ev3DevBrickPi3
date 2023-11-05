#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import MoveDifferential, OUTPUT_B, OUTPUT_C, SpeedRPM
from ev3dev2.port import LegoPort
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor


# import ultrasonic
import vehicleParameter

# Treiber für Sensoren laden
# gs = GyroSensor
gs = LegoPort(INPUT_4)
gs.mode = "ev3-uart"
gs.set_device = "lego-ev3-gyro"

# ts = TouchSensor -(stopSensor)
ts = LegoPort(INPUT_3)
ts.mode = "ev3-analog"
ts.set_device = "lego-ev3-touch"

sleep(4)

modVehicleParameter = vehicleParameter.VehicleParameter()
tankMotorBC = MoveDifferential(
    OUTPUT_B,
    OUTPUT_C,
    wheel_class=vehicleParameter.Ev3TireBrickPi,
    wheel_distance_mm=modVehicleParameter.wheelDistance)


class RobotGarage:
    def drive_out_garage(self):

        tankMotorBC.odometry_start()
        RobotGarage.test(self)
        tankMotorBC.on_to_coordinates(SpeedRPM(40), 0, 300)
        RobotGarage.test(self)
        tankMotorBC.on_to_coordinates(SpeedRPM(40), 300, 300)
        RobotGarage.test(self)
        tankMotorBC.odometry_stop()

    def drive_in_garage(self):

        tankMotorBC.on_to_coordinates(SpeedRPM(40), 0, 300)
        RobotGarage.test(self)
        tankMotorBC.turn_to_angle(SpeedRPM(40), 90)
        RobotGarage.test(self)
        tankMotorBC.odometry_stop()
        tankMotorBC.on_for_distance(SpeedRPM(-40), 300)
        RobotGarage.test(self)
        tankMotorBC.stop()

    def test(self):

        gyroTest = GyroSensor(INPUT_4)
        print(gyroTest.angle)

    def gyro_reset(self):
        gyroTest = GyroSensor(INPUT_4)
        gyroTest.calibrate()
