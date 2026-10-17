# #Question 1
# def greet(name):
#     print("Hello", name)

# greet("Asha")
# greet("Rahul")

# # Hello Asha
# # Hello Asha

# Question 2
# def subtract(a, b):
#     return a - b

# print(subtract(8, 3))
# print(subtract(3, 8))

# # 5
# #-5

# Question 3
# def calculate(number):
#     return number * 2

# result = calculate(5)
# print(result + 3)
# #13

# Question 4
# def greet(name="Guest"):
#     return "Hello " + name

# print(greet())
# print(greet("Asha"))
# # Hello Guest
# # Hello Asha

# Question 5
# def values():
#     return 10, 20

# a, b = values()
# print(a + b)
# # 30

# Question 6
# def show(a, b=5):
#     print(a, b)

# show(10)
# show(10, 20)
# show(a=7, b=3)
# # (10,5)
# # (10,20)
# # (7,3)

# Question 7
# def demo():
#     print("A")
#     return 5
#     print("B")

# print(demo())
# #A
# # 5


# Question 8
# def total(a, b, c=10):
#     return a + b + c

# print(total(1, c=3, b=2))
# #6




# 1
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()


# Welcome to Python
# Welcome to Python
# Welcome to Python


# 2
def greet(name):
    print("Hello", name)

greet("Darsh")


# Hello Darsh


# 3
def show_number(number):
    print(number)

show_number(25)


# 25


# 4
def add(a, b):
    return a + b

print(add(10, 20))

# 30


# 5
def square(number):
    return number * number

print(square(5))

# 25


# 6
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(8))
print(is_even(7))

# True
# False


# 7
def get_full_name(first_name, last_name):
    return first_name + " " + last_name

print(get_full_name("Darsh", "Vaishnav"))

# Darsh Vaishnav


# 8
def introduce(name, city="Pune"):
    print(name, "lives in", city)

introduce("Darsh")
introduce("Darsh", "Ahmedabad")

# Darsh lives in Pune
# Darsh lives in Ahmedabad


# 9
def subtract(a, b):
    return a - b

print(subtract(10, 5))
print(subtract(5, 10))

# 5
# -5


# 10
def get_min_max(a, b):
    return min(a, b), max(a, b)

print(get_min_max(15, 8))

# (8, 15)==> it is save in tuple


# 11
def calculate(a, b):
    return a + b, a - b, a * b, a / b

print(calculate(10, 2))

# (12, 8, 20, 5.0) ==> it is save in tuple


# 12
def count_digits(number):
    if number == 0:
        return 1

    count = 0

    while number > 0:
        count += 1
        number //= 10

    return count

print(count_digits(12345))
print(count_digits(0))

# 5
# 1


# 13
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(classify_number(10))
print(classify_number(-5))
print(classify_number(0))

# Positive
# Negative
# Zero


# 14
def calculate_total(price, quantity=1):
    return price * quantity

print(calculate_total(100))
print(calculate_total(100, 3))

# 100
# 300


# 15
def create_email(username, domain="example.com"):
    return username + "@" + domain

print(create_email("darsh"))
print(create_email("darsh", "gmail.com"))

# darsh@example.com
# darsh@gmail.com


# 16
def format_name(first, last, uppercase=False):
    full_name = first + " " + last

    if uppercase:
        return full_name.upper()

    return full_name

print(format_name("Darsh", "Vaishnav"))
print(format_name("Darsh", "Vaishnav", True))

# Darsh Vaishnav
# DARSH VAISHNAV


# 17
def percentage(marks, total=100):
    return (marks / total) * 100

print(percentage(80))
print(percentage(45, 50))

# 80.0
# 90.0


# 18
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute

print(convert_minutes(5))
print(convert_minutes(5, 60))

# 300
# 300


# 19
def student_details(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student_details(city="Ahmedabad", name="Darsh", age=18)

# Name: Darsh
# Age: 18
# City: Ahmedabad


# 20
def bill(item, quantity=1, price=100):
    bill=quantity * price
    return item,bill

print(bill("Pen"))
print(bill("Book", 3, 50))
print(bill(item="Pencil", price=10, quantity=5))

# Pen,100
# Book,150
# Pencil,50

# 21
def analyze_number(number):
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number

    if number % 2 == 0:
        even = True
    else:
        even = False

    if number == 0:
        digits = 1
    else:
        digits = 0
        while number != 0:
            digits += 1
            number = number // 10

    return absolute_value, even, digits

print(analyze_number(-123))

# (123, False, 3)


# 22
def calculate_stats(a, b, c):
    smallest = a
    largest = a

    if b < smallest:
        smallest = b
    elif b > largest:
        largest = b

    if c < smallest:
        smallest = c
    elif c > largest:
        largest = c

    total = a + b + c

    return smallest, largest, total

print(calculate_stats(10, 5, 20))

# (5, 20, 35)


# 23
def make_sentence(subject, verb, object):
    return subject + " " + verb + " " + object

print(make_sentence(object="Python", subject="I", verb="love"))

# I love Python

# 24
def apply_discount(price, discount=0):
    final_price = price - (price * discount / 100)
    return final_price

print(apply_discount(1000))
print(apply_discount(1000, 20))

# 1000.0
# 800.0

# Que 25
def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus

print(calculate_pay(40))                # Uses default rate (200) and bonus (0) -> 8000
print(calculate_pay(40, 250))           # Overrides rate -> 10000
print(calculate_pay(40, 250, 500))      # Overrides rate and bonus -> 10500
print(calculate_pay(40, bonus=300))     # Positional for hours, keyword for bonus -> 8300


# Que 26
def get_coordinates(x=0, y=0):
    return x, y


print(get_coordinates())       # Uses defaults -> (0, 0)
print(get_coordinates(x=10))   # Only x specified -> (10, 0)
print(get_coordinates(y=25))   # Only y specified -> (0, 25)

# Que 27
def compare(a, b):
    if a > b:
        status = "A is greater"
        diff = a - b
    elif b > a:
        status = "B is greater"
        diff = b - a
    else:
        status = "Equal"
        diff = 0
    return status, diff

print(compare(10, 4))   # ('A is greater', 6)
print(compare(3, 8))    # ('B is greater', 5)
print(compare(5, 5))    # ('Equal', 0)

# Que 28
def convert_temperature(value, scale="C"):
    if scale == "C":
        return (value * 9/5) + 32   # Celsius to Fahrenheit
    else:
        return (value - 32) * 5/9   # Fahrenheit to Celsius

print(convert_temperature(0, "C"))    # 0°C to °F -> 32.0
print(convert_temperature(100, "C"))  # 100°C to °F -> 212.0
print(convert_temperature(98.6, "F")) # 98.6°F to °C -> 37.0

# Que 29
def calculate_result(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"


print(calculate_result(40))      # Default pass mark 35 -> Pass
print(calculate_result(30))      # Default pass mark 35 -> Fail
print(calculate_result(45, 50))  # Custom pass mark 50 -> Fail

# Que 30
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return (quantity * price) + delivery_fee


print(order_summary("Book", delivery_fee=60))  # (1 * 100) + 60 -> 160