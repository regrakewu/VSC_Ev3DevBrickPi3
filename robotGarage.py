#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import MoveDifferential, OUTPUT_B, OUTPUT_C, SpeedRPM
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import GyroSensor

# import ultrasonic
import vehicleParameter

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
        RobotGarage.gyro_reset(self)
        RobotGarage.test(self)
        tankMotorBC.on_to_coordinates(SpeedRPM(40), 0, 300)
        RobotGarage.test(self)
        tankMotorBC.on_to_coordinates(SpeedRPM(40), 300, 300)
        RobotGarage.test(self)
        

    def drive_in_garage(self):

        tankMotorBC.gyro = GyroSensor()
        tankMotorBC.on_to_coordinates(SpeedRPM(40), 0, 300)
        RobotGarage.test(self)
        tankMotorBC.turn_degrees(speed=40, degrees=90, brake=True, block=True, error_margin=2, use_gyro=True)
        # tankMotorBC.turn_to_angle(SpeedRPM(40), 90)
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
