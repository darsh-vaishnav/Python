n = int(input("Enter a positive integer: "))
if n > 0:
    number = 1
    while number <= n:
        print(number)
        number += 1
else:
    print("Enter a positive integer.")