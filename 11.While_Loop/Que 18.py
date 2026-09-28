n = int(input("Enter n: "))
total = 0
number = 1
while number <= n:
    if number % 2 != 0:
        total += number
    number += 1
print("Sum of odd numbers:", total)