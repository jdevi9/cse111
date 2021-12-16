"""
Input: user puts width of tire in mm, aspect ratio of tire,
       and diameter of the wheel in inches
Process: program calculates for tire volume
Output: tire volume in liters
"""
#import for PI constant
import math
#User input
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000000

print(f"The approximate volume is {v:.2f} liters")



