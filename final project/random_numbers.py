#creates a list of numbers, appends more numbers onto the list 
#prints the list

import random

randnums = []

randwords = []

def main():
    i = 0
    while i < 4:
        i += 1
        random_number = round(random.uniform(0, 100), 1)
        randnums.append(random_number)
    print(f"randnums {randnums}")

    #requirement d
    append_random_numbers(randnums)
    print(f"randnums {randnums}")

    #requirement f
    append_random_numbers(randnums, 3)
    print(f"randnums {randnums}")

    #Stretch
    append_random_words(randwords)
    print(f"randwords {randwords}")

    append_random_words(randwords, 3)
    print("Study the following subjects:")
    print(f"{randwords}")

def append_random_numbers(numbers_list, quantity=1):
    """adds random number to a number list.
    Parameters: 
        numbers_list: a list of numbers that will appended
        quantity: the number of times this will repeat
    return: no return
    """
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)

def append_random_words(words_list, quantity=1):
    """adds random word to a word list.
    Parameters: 
        word_list: a list of numbers that will appended
        quantity: the number of times this will repeat
    return: no return
    """
    random_words = ['math', 'science', 'computer science', 
    'biology', 'history', 'literature']
    for _ in range(quantity):
        random_word = random.choice(random_words)
        words_list.append(random_word)


#execute main
if __name__ == "__main__":
    main()