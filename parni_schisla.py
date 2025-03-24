def even_numbers_reverse(n):
    print(" ".join(str(i) for i in range(n, 0, -1) if i % 2 == 0))
n = int(input("Enter 'n': "))
even_numbers_reverse(n)