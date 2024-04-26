
def the_bigges_num():
    numbers_list = [1,30,3,50,1,0,70,-5]
    max = numbers_list[0]

    for item in numbers_list:
        if item > max:
            max = item

    return max 

print(the_bigges_num())