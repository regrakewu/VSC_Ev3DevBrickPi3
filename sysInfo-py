#!/usr/bin/env python3

from ev3dev2.power import PowerSupply


class SystemInfo:

    batteryPower = PowerSupply()
    batteryVolt = batteryPower.measured_volts

    def volt_brick_pi(self):
        volt = round(float(self.batteryVolt), 2)
        if volt > 9.5:
            print("Die Leistung des Akkus betraegt: " + (str(volt)) + " Volt")
        else:
            print('''Die Leistung des Akkus ist in einem kritischen Bereich!'
                  Der Brick schaltet sich gleich aus!''')


# todo: Hier soll noch Sound eingebaut werden (subprocess)
