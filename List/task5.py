def calc_strings():
    list_of_strings = ['cat', '1245', 'poop', 'dog', '532', '2002', 'e', 'ellllllllle']

    numbers_of_string = 0

    for item in list_of_strings: 
        if len(item) >= 2 and item[0] == item[-1]:
            numbers_of_string+=1

    return numbers_of_string 

print(calc_strings())