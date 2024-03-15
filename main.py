#!/usr/bin/env python3

# Input Belegung
# S1 = Ultraschall Senor Front
# S2 = Ultraschall Senor Back
# S3 = Touch Sensor
# S4 = Gyro Senor

# Output Belegung
# MA = Middle Motor
# MB = Large Motor Left
# MC = Large Motor Right
# MD = Free

# import robotGarage
import gyroSensorTest
import sysInfo
import ultrasonic
import vehicleParameter


# Batterieleistung ausgeben
modSysInfo = sysInfo.SystemInfo()
modSysInfo.volt_brick_pi()

#TODO: Von Zeile 25 bis 38 ist auskommentiert! Nur für Testzwecke.

# modUltraSonic = ultrasonic.UltraSonic()

# Aus Parkposition fahren
# modVehicleParameter = vehicleParameter.VehicleParameter()
# modRobotGarage = robotGarage.RobotGarage()
# modRobotGarage.drive_out_garage()
# modRobotGarage.drive_in_garage()
# modUltraSonic.ultra_sonic_motor_scan()


modGyroSensorTest = gyroSensorTest.GyroSensorTest()
modGyroSensorTest.gyro_brickPi()


