#datetime used to calculate person's age
from datetime import datetime

def main ():
    #input 
    gender = input("Please enter your gender (M or F): ")
    birth_date = input("Please enter your birthdate (YYYY-MM-DD): ")
    weight = float(input("Enter your weight in US pounds: "))
    height = float(input("Enter your height in US inches: "))

    #calculate
    age = compute_age(birth_date)
    weight_in_kg = kg_from_lb(weight)
    height_in_cm = cm_from_in(height)
    bmi = body_mass_index(weight_in_kg, height_in_cm)
    bmr = basal_metabolic_rate(gender, weight_in_kg, height_in_cm, age)

    #display results
    print(f"Age (years): {age}")
    print(f"Weight (kg): {weight_in_kg:.1f}")
    print(f"Height (cm): {height_in_cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthday.year
    if birthday.month > today.month or (birthday.month == today.month and birthday.day > today.day):
        years -= 1
    
    return years

def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    kg = lb * 0.45359237
    return kg

def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    cm = inch * 2.54
    return cm

def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / (height ** 2) * 10000
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr

#execution starts here
main()

