def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter number for factorial: "))
print(f"factorial: {num} = {factorial(num)}")