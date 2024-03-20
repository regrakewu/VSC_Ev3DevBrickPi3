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
        tankMotorBC.gyro = gyroSensor
        
        while not stopSensor.is_pressed:
                                   
            tankMotorBC.on_for_distance(speed=SpeedPercent(20), distance_mm=100)  
            tankMotorBC.turn_to_angle(speed=SpeedPercent(20), angle_target_degrees=90, brake=True, block=True, error_margin=2, use_gyro=True)  
            # tankMotorBC.turn_degrees(speed=SpeedPercent(20), degrees=-45, brake=True, block=True, error_margin=2, use_gyro=False)
            GyroSensorTest.gyro_Angle(self)        
                
        tankMotorBC.odometry_stop()         
        print("Program is stopped")
    
    def gyro_Angle(self):
        angel = tankMotorBC.gyro.angle
        """ tankMotorBC.stop()
        gyroSensor.wait_until_angle_changed_by(90, direction_sensitive=False)
        tankMotorBC.on_for_distance(speed=SpeedPercent(40), distance_mm=200)
        tankMotorBC.stop() """
        if angel > 45:
            tankMotorBC.stop()
            print(angel, "Grad")
            
   
            
     
      
        