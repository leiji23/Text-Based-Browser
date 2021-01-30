def range_sum(numbers, start, end):
    my_sum = 0
    for num in numbers:
        my_sum += int(num) if int(start) <= int(num) <= int(end) else 0
    return my_sum


input_numbers = input().split()
a, b = input().split()
print(range_sum(input_numbers, a, b))
