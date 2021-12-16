# Example 2

import csv


def main():
    # Indexes of some of the columns
    # in the dentists.csv file.
    COMPANY_NAME_INDEX = 0
    ADDRESS_INDEX = 1
    PHONE_NUMBER_INDEX = 2

    # Read the contents of a CSV file named dentists.csv
    # into a dictionary named dentists. Use the phone
    # numbers as the keys in the dictionary.
    dentists = read_dict("dentists.csv", PHONE_NUMBER_INDEX)

    # Print the dentists dictionary.
    print(dentists)


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a dictionary
    and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()