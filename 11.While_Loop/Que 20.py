n = int(input("Enter n: "))
product = 1
number = 1
while number <= n:
    product *= number
    number += 1
print("Product:", product)