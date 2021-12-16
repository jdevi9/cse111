import math

numItems = int(input("Enter the number of items: "))
numItemsPerBox = int(input("Enter the number of items per box: "))

boxes = math.ceil(numItems / numItemsPerBox)

print(f"For {numItems}, packing {numItemsPerBox} items in each box, you will need {boxes} boxes.")



