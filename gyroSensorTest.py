#!/usr/bin/env python3
from time import sleep
from ev3dev2.port import LegoPort
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, SpeedPercent

# Treiber für Sensoren laden
# gs = GyroSensor
gs = LegoPort(INPUT_4)
gs.mode = "ev3-uart"
gs.set_device = "lego-ev3-gyro"

# ts = TouchSensor - (stopSensor)
ts = LegoPort(INPUT_3)
ts.mode = "ev3-analog"
ts.set_device = "lego-ev3-touch"

tankMotorBC = MoveTank(OUTPUT_B, OUTPUT_C)


class GyroSensorTest:
    def gyro_brickPi(self):

        stopSensor = TouchSensor(INPUT_3)
        gyroTest = GyroSensor(INPUT_4)
        tankMotorBC.gyro = GyroSensor()
        tankMotorBC.stop()
        while not stopSensor.is_pressed:

            tankMotorBC.turn_degrees(speed=SpeedPercent(30), target_angle=45)
            print(gyroTest)
            sleep(2)
        print("Program is stopped")