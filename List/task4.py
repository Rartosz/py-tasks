def the_smallest_num():
    numbers_list = [1,30,3,50,1,0,70,-5]
    min = numbers_list[0]

    for item in numbers_list:
        if item < min:
            min = item

    return min 

print(the_smallest_num())