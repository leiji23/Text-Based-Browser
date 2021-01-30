n = int(input())
denominator = int(input())
try:
    print(int(n / denominator))
except ZeroDivisionError:
    print("Division by zero is not supported")
