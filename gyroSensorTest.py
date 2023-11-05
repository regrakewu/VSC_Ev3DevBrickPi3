#!/usr/bin/env python3

from time import sleep
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.motor import MoveDifferential, OUTPUT_B, OUTPUT_C, SpeedPercent
import vehicleParameter

tankMotorBC = MoveDifferential(OUTPUT_B, OUTPUT_C, vehicleParameter.Ev3TireBrickPi,
                               vehicleParameter.VehicleParameter.wheelDistance)

class GyroSensorTest:
    def gyro_brickPi(self):

        stopSensor = TouchSensor(INPUT_3)
        
              
        while not stopSensor.is_pressed:
             
            tankMotorBC.gyro = GyroSensor(INPUT_4)      
            tankMotorBC.turn_degrees(speed=SpeedPercent(30), degrees=45)
            gyroTest = tankMotorBC.gyro.angle
            print(gyroTest)
            sleep(2)
            
        print("Program is stopped")