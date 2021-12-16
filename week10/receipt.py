import csv
from os import name
from datetime import datetime

current_date_and_time = datetime.now()

#index from products.csv
PRODUCT_KEY_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

#Index from request.csv
PRODUCT_NUM_INDEX = 0
PRODUCT_QUANTITY_INDEX = 1

def main():
    try:
        products = read_products("products.csv")

        #print("Products")
        #for key in products: 
            #print (key, ':', products[key])

        print("Inkom Emporium")
        print()

        #print("Requested Items")

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            total_price = 0
            total_quantity = 0
            subtotal = 0
            for row in reader:
            
                product_num = row[PRODUCT_NUM_INDEX]
                quantity = int(row[PRODUCT_QUANTITY_INDEX])
                product_info = products[product_num]
                product_name = product_info[0]
                price = float(product_info[1])
                actual_price = round(price, 2)

                print(f'{product_name}: {quantity} @ {actual_price}')

                total_quantity += quantity
                subtotal += price * quantity
                sales_tax = subtotal * .06
                total_price = sales_tax + subtotal

            print()
            print(f"Number of Items: {total_quantity}")
            print(f"Subtotal: {round(subtotal, 2)}")
            print(f"Sales Tax: {round(sales_tax, 2)}")
            print(f"Total: {round(total_price, 2)}")

            print()
            print("Thank you for shopping at the Inkom Emporium")
            print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
    
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    
    except PermissionError as perm_err:
        print(perm_err)
    
    except KeyError as key_err:
        print(type(key_err.__name__, key_err))



def read_products(filename):
    products_dict = {}

    with open(filename, "rt") as text_file:
        reader = csv.reader(text_file)

        # skips header
        next(reader)

        for row in reader:
            key = row[PRODUCT_KEY_INDEX]
            row1 = row[PRODUCT_NAME_INDEX]
            row2 = float(row[PRODUCT_PRICE_INDEX])
            products_dict[key] = [row1, row2]
    return products_dict


if __name__ == "__main__":
    main()
