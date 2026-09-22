# Q1. Take two numbers and print their sum
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum =", a + b)


# Q2. Take two numbers and print their difference
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Difference =", a - b)


# Q3. Take two numbers and print their product
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Product =", a * b)


# Q4. Take length and width of a rectangle and calculate its area
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)


# Q5. Take the side of a square and calculate its area
side = float(input("Enter side of square: "))
area = side * side
print("Area of square =", area)


# Q6. Take the radius of a circle and calculate its area
radius = float(input("Enter radius of circle: "))
area = 3.14 * radius * radius
print("Area of circle =", area)


# Q7. Take three subject marks and calculate the total
mark1 = float(input("Enter marks of subject 1: "))
mark2 = float(input("Enter marks of subject 2: "))
mark3 = float(input("Enter marks of subject 3: "))
total = mark1 + mark2 + mark3
print("Total marks =", total)


# Q8. Take three subject marks and calculate the average
mark1 = float(input("Enter marks of subject 1: "))
mark2 = float(input("Enter marks of subject 2: "))
mark3 = float(input("Enter marks of subject 3: "))
average = (mark1 + mark2 + mark3) / 3
print("Average marks =", average)


# Q9. Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit =", fahrenheit)


# Q10. Calculate simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

# Q11. Check whether a number is positive or negative
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Negative")


# Q12. Check whether a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q13. Check whether a student has passed or failed
marks = float(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")


# Q14. Check whether a person is eligible to vote based on age
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Q15. Find the larger of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Larger number =", a)
else:
    print("Larger number =", b)


# Q16. Check whether a number is divisible by 5
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


# Q17. Check whether a number is zero or non-zero
num = float(input("Enter a number: "))

if num == 0:
    print("Zero")
else:
    print("Non-zero")


# Q18. Apply a 10% discount if the total price is at least 1000
price = float(input("Enter total price: "))

if price >= 1000:
    discount = price * 10 / 100
    final_price = price - discount
    print("Discount =", discount)
    print("Final price =", final_price)
else:
    print("No discount")
    print("Final price =", price)


# Q19. Check whether a password matches a fixed password
password = input("Enter password: ")

if password == "python123":
    print("Password matched")
else:
    print("Incorrect password")


# Q20. Check whether temperature is above or below 30°C
temperature = float(input("Enter temperature in Celsius: "))

if temperature > 30:
    print("Temperature is above 30°C")
else:
    print("Temperature is 30°C or below")

# Q21. Take three numbers and print the largest
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)


# Q22. Take marks and assign a grade using multiple conditions
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Grade F")


# Q23. Take 5 numbers and calculate their sum
total = 0

for i in range(5):
    num = float(input("Enter a number: "))
    total = total + num

print("Sum =", total)


# Q24. Take 5 numbers and count how many are positive
count = 0

for i in range(5):
    num = float(input("Enter a number: "))

    if num > 0:
        count = count + 1

print("Positive numbers =", count)


# Q25. Take 10 numbers and count how many are even
count = 0

for i in range(10):
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        count = count + 1

print("Even numbers =", count)


# Q26. Take 5 numbers and find the largest number
largest = None

for i in range(5):
    num = float(input("Enter a number: "))

    if largest is None or num > largest:
        largest = num

print("Largest number =", largest)


# Q27. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# Q28. Print even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)


# Q29. Print the multiplication table of a number
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Q30. Take 5 numbers and calculate their average
total = 0

for i in range(5):
    num = float(input("Enter a number: "))
    total = total + num

average = total / 5

print("Average =", average)    