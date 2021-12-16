import csv

def main():
    I_NUMBER_INDEX = 0
    NAME = 1
    students = read_dict("students.csv", I_NUMBER_INDEX)
    
    #i-number from user
    inumber_input = str(input("Please enter an I-Number (xx-xxx-xxxx): "))
    #remove dashes from user input
    inumber_input = inumber_input.replace("-", "")

    if inumber_input not in students:
        print("No such student")
    else:
        value = students[inumber_input]
        name = value[NAME]
        print(name)



def read_dict(filename, key_column_index):
    dictionary = {}

    with open(filename, "rt") as text_file:

        reader = csv.reader(text_file)
        next(reader)

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary

if __name__ == "__main__":
    main()