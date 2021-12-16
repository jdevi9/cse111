"""
Input: user puts width of tire in mm, aspect ratio of tire,
       and diameter of the wheel in inches
Process: program calculates for tire volume
Output: tire volume in liters
"""
#imports
from datetime import datetime
import math

current_date_and_time = datetime.now()

#User input
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = round((math.pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000000, 2)

print(f"The approximate volume is {v:.2f} liters")

buy_decision = input("Would you like a service rep to contact you about purchasing tire? (yes or no)")
if buy_decision.lower() == "yes":
    user_first_name = input("What is first Name? ")
    user_last_name = input("What is your last name? ")
    user_telephone_number = input("What is your telephone number? ")
    user_email = input("What is your email? ")
else:
    print("Thank you")
    exit()

with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, ", file=volumes_file)
    print(f"Dimensions: {w}, {a}, {d}, {v}", file=volumes_file)
    print(f"{user_last_name}, {user_first_name} Phone: {user_telephone_number} Email: {user_email}", file=volumes_file)

print("Thank you, have a good day.")