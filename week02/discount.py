from datetime import datetime

discount_rate = .10
sales_tax_rate = .06

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

#print(day_of_week)

#subtotal = float(input("Please enter the subtotal: "))
print("Please enter the price of the item and how many you are purchasing. Type 'done' to get total.")

text = ""
subtotal = 0

while text.lower() != "done":

    text = input("Please enter a price for item: ")
    if text.lower() != "done":
        price = float(text)
        quantity = float(input("How many: "))
        subtotal += price * quantity

subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal}")

if day_of_week == 1 or day_of_week == 2:
    if subtotal < 50:
        difference = 50 - subtotal
        print(f"To receive the discount, add {difference} to your order")
    else:   
        discount = round(subtotal * discount_rate, 2)
        print(f"Discount amount: {discount}")
        subtotal -= discount


sales_tax = round(subtotal * sales_tax_rate, 2)
print(f"Sales tax amount: {sales_tax}")

total = subtotal + sales_tax
print(f"Total: {total:.2f}")