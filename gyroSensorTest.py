#!/usr/bin/env python3

from time import sleep
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.motor import MoveDifferential, OUTPUT_B, OUTPUT_C, SpeedPercent
import vehicleParameter
import sys


tankMotorBC = MoveDifferential(OUTPUT_B, OUTPUT_C, wheel_class=vehicleParameter.Ev3TireBrickPi,
                               wheel_distance_mm=vehicleParameter.VehicleParameter.wheelDistance)

class GyroSensorTest:
    
    def gyro_brickPi(self):
        
        stopSensor = TouchSensor(INPUT_3)       
        tankMotorBC.odometry_start()  
        gyroSensor = GyroSensor() 
        tankMotorBC.gyro = gyroSensor
     
       
        
        while not stopSensor.is_pressed:
             
                tankMotorBC.on_for_distance(speed=SpeedPercent(40), distance_mm=300)
                sleep(1) 
                tankMotorBC.turn_right(speed=SpeedPercent(20), degrees=90, brake=True, block=True, error_margin=2, use_gyro=True)
                sleep(1)
                GyroSensorTest.gyro_Angle(self)
           
        print("Program is stopped")
    
    def gyro_Angle(self):
        
        angel = tankMotorBC.gyro.angle
        
        if angel > 358:
            
            tankMotorBC.stop()  
            angel = 0      
            print(angel, "Grad")       
            print("GyroSensor is reset")
            print(angel, "Grad")
            sys.exit()
        
        print(angel, "Grad")
            
     
      
        