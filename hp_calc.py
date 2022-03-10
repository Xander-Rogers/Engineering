#!PythonProjects/env python
# Author: Alexander Rogers
# Contact: arogers23@email.davenport.edu

# Program name: hp_calc.py
"""
Example of how a Python programs can use class arguments, and functions to automate heavy, algebraic calculations.
"""

# Import the math module which defines constants such as pi accurately, and has functions for operations such as
# rounding.
import math


# The class Power will store the functions, and user input information such as the bore diameter of a given cylinder,
# the stroke length of a given piston, which is the distance between top dead center (TDC) and bottom dead center (BDC),
# the intake temperature recorded by the user, and the bare metal exhaust temperature after 20 or more minutes of
# moderate driving. The sweet spot is determined by the user, however there are ways to do it by researching performance
# specifications, or determining through means of driving and noticing at what RPM range is the most feeling of power
# being delivered at a given time. Articles for more information/guidance:
# Stroke Length - https://help.summitracing.com/app/answers/detail/a_id/5001/~/engine-stroke-length
# Sweet Spot - https://practicalmotoring.com.au/car-advice/when-should-you-change-gear-for-maximum-acceleration/


class Power:

    def __init__(self, bore, stroke_len, in_temp, ex_temp, sweet_spot):
        self.bore = bore
        self.stroke_len = stroke_len
        self.in_temp = in_temp
        self.ex_temp = ex_temp
        self.sweet_spot = sweet_spot

    def cyl_vol(self):
        # Volume of a single cylinder.
        bore_diam = self.bore
        stroke = self.stroke_len

        # Radius of the bore.
        bore_rad = float(bore_diam / 2)

        # Cross-sectional area of the cylinder.
        crs_area = float((bore_rad ** 2) * math.pi)

        # Cylinder volume in cc since bore measurements were in mm.
        cyl_volume = (crs_area * stroke) / 1000
        return cyl_volume

    def ex_vol(self):
        # Change in volume due to temperature.
        intake_temp = self.in_temp
        exhaust_temp = self.ex_temp

        # Convert temperature in Fahrenheit to the Rankine scale of temperature
        rankine = 459.67
        rankine_in_temp = float(intake_temp + rankine)
        rankine_exhaust_temp = float(exhaust_temp + rankine)

        # Calculate the temperature coefficient which represents the increase in volume.
        temp_coef = float(rankine_exhaust_temp / rankine_in_temp)

        # Change in volume due to chemical reaction, where the octane reaction to create the by products of combustion,
        # CO2 and H2O, the stoichiometric values of 8CO2 +9H20 when octane with a molecular weight of 114 combining with
        # 12.5 moles of oxygen.
        chem_coef = (8 + 9) / 12.5

        # Atmosphere is roughly 20.9 % Oxygen, calculate expansion due to gases
        expansion = ((100 - 20.9) + (20.9 * chem_coef)) / 100

        # Multiply with cylinder volume and temperature coefficient
        cylinder = Power.cyl_vol(self)
        ex_volume = cylinder * temp_coef * expansion
        return round(ex_volume, 2)

    def horsepower(self):
        rpm = self.sweet_spot
        exhaust_volume = Power.ex_vol(self)

        # Calculate pulses, meaning the cycles of the engine in the case of when the exhaust stroke occurs.
        pulses = rpm / 2

        # Calculate exhaust gas exiting per min. Convert from cubic centimeters to cubic meters.
        ex_per_min = pulses * exhaust_volume / 1000000

        # Calculate power in terms of kilowatt hour (constant 10.55), and then convert to horsepower (constant 1.34048).
        kwh = ex_per_min * 10.55
        hp = (kwh * 1.34048)
        return round(hp, 2)


# User input is taken.
cls = Power(
    int(input('Bore Diameter: ')),
    float(input('Engine Stroke Length: ')),
    int(input('Intake Temperature: ')),
    int(input('Exhaust Temperature: ')),  # year, month, day
    int(input('Sweet Spot RPM: ')),
)

# Display the output to the user.
print("Cylinder Volume (cc): ", cls.cyl_vol())
print("Exhaust Volume released per Stroke (cc): ", cls.ex_vol())
print("Horsepower: ", cls.horsepower())

# Test was run with data from a Honda CJ360T, which is a 2 cylinder motorbike:
# Input: 67mm, 50.6mm, 72 degrees F (typically room temp), 1600 degrees F (how hot exhausts can typically get), 6000 RPM
# Output: Horsepower of 31.53, which is approximate to the manufacturer specs of 34.
# https://www.motorcyclespecs.co.za/model/Honda/honda_cj360t.htm


# EOF
