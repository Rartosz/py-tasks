def count_the_list():
    num_list = [1, 30, 100]
    sum_numbers = 1
    for item in num_list:
        sum_numbers = sum_numbers * item

    return sum_numbers

print(count_the_list())