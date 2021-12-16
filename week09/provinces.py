def main():
    province_list = read_list('provinces.txt')
    #shows the list 
    print(province_list)
    #requisite #4 removing of first element
    province_list.pop(0)
    #requisite #5 removing the last element
    province_list.pop()
    #replace occurances of "AB" to "Alberta"
    for i in range(len(province_list)):
        if province_list[i] == "AB":
            province_list[i] = "Alberta"
    count_total = province_list.count("Alberta")
    
    print()
    print(f"Alberta occurs {count_total} times in the modified list.")

def read_list(filename):
    text_lines = []

    #open the text file for reading 
    with open(filename, "rt") as text_file:

        #go line by line
        for line in text_file:
            clean_line = line.strip()
            #adds each line into the list
            text_lines.append(clean_line)
    #returns the list with the appended items        
    return text_lines

if __name__ == "__main__":
    main()