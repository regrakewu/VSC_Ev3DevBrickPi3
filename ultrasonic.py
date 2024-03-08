#!/usr/bin/env python3

import random
from time import sleep
from ev3dev2.motor import MoveDifferential, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.port import LegoPort
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor, TouchSensor
import vehicleParameter

# Treiber für Sensoren laden
# usf = ultraSonicSensorFront
usf = LegoPort(INPUT_1)
usf.mode = 'ev3-uart'
usf.set_device = 'lego-ev3-us'
# usb = ultraSonicSensorBack
usb = LegoPort(INPUT_2)
usb.mode = 'ev3-uart'
usb.set_device = 'lego-ev3-us'
# ts = TouchSensor - (stopSensor)
ts = LegoPort(INPUT_3)
ts.mode = 'ev3-analog'
ts.set_device = 'lego-ev3-touch'
# gs = GyroSensor
gs = LegoPort(INPUT_4)
gs.mode = 'ev3-uart'
gs.set_device = 'lego-ev3-gyro'

sleep(1)

stopSensor = TouchSensor(INPUT_3)
mediumMotorB = LargeMotor(OUTPUT_A)
tankMotorBC = MoveDifferential(OUTPUT_B, OUTPUT_C, vehicleParameter.Ev3TireBrickPi,
                               vehicleParameter.VehicleParameter.wheelDistance)
ultraSonicSenorFront = UltrasonicSensor(INPUT_1)
ultraSonicSenorBack = UltrasonicSensor(INPUT_2)
modVehicleParameter = vehicleParameter.VehicleParameter()

posUltraSonic = [0, -200, 0, 200, 0]

class UltraSonic:

    def ultra_sonic_motor_scan(self):

        while not stopSensor.is_pressed:

            for i in posUltraSonic:
                mediumMotorB.on_to_position(speed=7, position=i)
                tankMotorBC.on(left_speed=modVehicleParameter.wheel_speed(50),
                               right_speed=modVehicleParameter.wheel_speed(50))

                if ultraSonicSenorFront.distance_centimeters < 25.0:

                    mediumMotorB.stop()
                    tankMotorBC.stop()
                    # todo: tankMotorAC.wait_until_not_moving(timeout=2000) löschen
                    tankMotorBC.on_for_degrees(left_speed=modVehicleParameter.wheel_speed(-40),
                                               right_speed=modVehicleParameter.wheel_speed(-40),
                                               degrees=modVehicleParameter.distance_track(300))
                    randomNum = random.randint(a=0, b=1)
                    if randomNum == 0:
                        tankMotorBC.turn_left(speed=modVehicleParameter.wheel_speed(40), degrees=45)
                    else:
                        tankMotorBC.turn_right(speed=modVehicleParameter.wheel_speed(40), degrees=45)
            else:
                self.motor_stop()

    def ultra_sonic_scan_back(self):
        if ultraSonicSenorBack.distance_centimeters < 15:
            UltraSonic.motor_stop(self)


    def motor_stop(self):
        tankMotorBC.stop()
        mediumMotorB.on_to_position(speed=7, position=0)
        mediumMotorB.stop()
