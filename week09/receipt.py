import csv
from os import name

#index from products.csv
PRODUCT_KEY_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

#Index from request.csv
PRODUCT_NUM_INDEX = 0
PRODUCT_QUANTITY_INDEX = 1

def main():
    products = read_products("products.csv")
    print("Products")
    for key in products: 
        print (key, ':', products[key])
    print()
    print("Requested Items")
    
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)
        
        for row in reader:
            product_num = row[PRODUCT_NUM_INDEX]
            quantity = int(row[PRODUCT_QUANTITY_INDEX])
            product_info = products[product_num]
            product_name = product_info[0]
            price = float(product_info[1])
            actual_price = round(price, 2)
           
            print(f'{product_name}: {quantity} @ {actual_price}')


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
