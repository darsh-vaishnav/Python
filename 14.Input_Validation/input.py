
# Que 1
marks = int(input("Enter your marks: "))
while marks<=0 or marks>=100:
    marks = int(input("Enter your marks: "))
print("Accepted marks:", marks)    

# Que 2
integer = int(input ("Enter your marks:"))
while integer<=0:
    integer = int(input ("Enter your marks:"))
print("Accepted marks:", integer)    

# Que 3
age= int(input ("Enter your age:"))
while age<=0 or age>=120:
    print("This is invalid input")
    age = int(input ("Enter your age:"))
print("Accepted age:", age)  

# Que 4
while True:
    print("1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            print("View profile")
            break
        case 2:
            print("Edit profile")
            break
        case 3:
            print("Settings")
            break
        case 4:
            print("Exit")
            break
        case _:
            print("Invalid choice. Try again.")

# Que 5
password= input ("Enter your password:").strip() 
while len(password)<8:
    print("Password must contain at least 8 characters")
    password = input("Enter password: ").strip()
  
print("Password accepted")           

# Que 6
temp= float(input ("Enter your Temperature:"))
while temp<=-20 or temp>=45:
    print("This is invalid input")
    temp = float(input ("Enter your temperature:"))
print("Valid temperature")  

# Que 7
balance = 5000

amount = float(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance:
    print("Invalid amount. Try again.")
    amount = float(input("Enter withdrawal amount: "))

balance = balance - amount

print("Remaining balance: ", balance)

# Que 8
username = input("Enter username: ").strip()

while len(username) < 5 or " " in username:
    print("Invalid username. Try again.")
    username = input("Enter username: ").strip()

print("Accepted username:", username)

# Que 9
number = int(input("Enter a positive integer: "))

while number <= 0 or number % 3 != 0 or number % 5 != 0:
    print("Invalid number. Try again.")
    number = int(input("Enter a positive integer: "))

print("Accepted number:", number)

# Que 10
pin = 2468
attempts = 1

while attempts <= 3:
    entered_pin = int(input("Enter PIN: "))

    if entered_pin == pin:
        print("Access granted")
        break
    else:
        print("Incorrect PIN")
        attempts = attempts + 1

if attempts > 3:
    print("Access denied")

# Que 11    
number = int(input("Enter a number between 10 and 50: "))

while number < 10 or number > 50:
    print("Invalid number. Try again.")
    number = int(input("Enter a number between 10 and 50: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Que 12  
balance = 2000

amount = float(input("Enter deposit amount: "))

while amount <= 0:
    print("Invalid amount. Enter a positive amount.")
    amount = float(input("Enter deposit amount: "))

balance = balance + amount

print("New balance: ", balance)     

# Que 13
number = int(input("Enter an integer between 1 and 100: "))

while number < 1 or number > 100:
    print("Invalid number. Try again.")
    number = int(input("Enter an integer between 1 and 100: "))

print("Accepted number:", number)

# Que 14
marks = int(input("Enter marks (0-100): "))

while marks < 0 or marks > 100:
    print("Invalid marks. Try again.")
    marks = int(input("Enter marks (0-100): "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

# Que 15    
username = input("Enter username: ").strip()
password = input("Enter password: ")

while len(username) < 5 or " " in username or len(password) < 8 or password.strip() == "":
    print("Invalid username or password. Try again.")

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

print("Registration successful!")
# Que 16
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")

while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operator. Try again.")
    operator = input("Enter operator (+, -, *, /): ")

num2 = float(input("Enter second number: "))

while operator == "/" and num2 == 0:
    print("Division by zero is not allowed.")
    num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2

print("Result:", result) 