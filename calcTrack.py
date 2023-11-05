#!/usr/bin/env python3
# todo: GyroSensor löschen und MoveTank in MoveDifferential ändern
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import GyroSensor
tankMotorBC = MoveTank(OUTPUT_B, OUTPUT_C)
positionSensor = GyroSensor(INPUT_4)
#positionSensor.calibrate()
tankMotorBC.gyro = positionSensor


class CalcTrack:

    def track_straight_ahead(self, speedStraightAhead, track):
        trackStraightAhead = tankMotorBC.on_for_degrees(left_speed=speedStraightAhead, right_speed=speedStraightAhead,
                                                        degrees=track)
        return trackStraightAhead
