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
    return quantity * price

print(bill("Pen"))
print(bill("Book", 3, 50))
print(bill(item="Pencil", price=10, quantity=5))

# 100
# 150
# 50

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