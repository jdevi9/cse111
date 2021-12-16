def main():
    fruit_list = ['pear', 'banana', 'apple', 'mango']
    print(f'original: {fruit_list}')
    #3. reverse the list
    fruit_list.reverse()
    print(f'reverse: {fruit_list}')
    #4. append orange
    fruit_list.append('orange')
    print(f'add orange: {fruit_list}')
    #5. insert cherry after apple
    fruit_list.insert(1, 'cherry')
    print(f'insert cherry: {fruit_list}')
    #6. remove banana
    fruit_list.remove('banana')
    print(f'remove banana: {fruit_list}')
    #7. pop the last element (orange)
    orange = fruit_list.pop()
    print(f'pop {orange}: {fruit_list}')
    #8 sort the list
    fruit_list.sort()
    print(f'sorted: {fruit_list}')
    #9 clear the list
    fruit_list.clear()
    print(f'cleared: {fruit_list}')

if __name__ == '__main__':
    main()