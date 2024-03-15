#!/usr/bin/env python3

from time import sleep
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.motor import MoveDifferential, OUTPUT_B, OUTPUT_C, SpeedPercent
import vehicleParameter

tankMotorBC = MoveDifferential(OUTPUT_B, OUTPUT_C, wheel_class=vehicleParameter.Ev3TireBrickPi,
                               wheel_distance_mm=vehicleParameter.VehicleParameter.wheelDistance)

class GyroSensorTest:
    
    def gyro_brickPi(self):

        stopSensor = TouchSensor(INPUT_3)       
        tankMotorBC.odometry_start()  
        gyroSensor = GyroSensor()  
        
        while not stopSensor.is_pressed:
            
            tankMotorBC.gyro = gyroSensor                
            tankMotorBC.on_for_distance(speed=SpeedPercent(20), distance_mm=100)         
            tankMotorBC.turn_degrees(speed=SpeedPercent(20), degrees=-90, brake=True, block=True, error_margin=2, use_gyro=False)
            sleep(1)
            GyroSensorTest.gyro_Angle(self)        
            # tankMotorBC.turn_degrees(speed=SpeedPercent(30), degrees=90)
            # gyroTest = tankMotorBC.gyro.angle
            # print(gyroTest)

                
        tankMotorBC.odometry_stop()         
        print("Program is stopped")
    
    def gyro_Angle(self):
        angel = tankMotorBC.gyro.angle
        print(angel)
     
      
        