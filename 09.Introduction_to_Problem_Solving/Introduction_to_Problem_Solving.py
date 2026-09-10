#Task 1
number=int(input("Enter the Number:"))

if number >0:
  print("Positive")
elif number <0:
  print("Negative") 
else:
  print("Zero")   

#Task2
number=int(input("Enter The number:"))

if number % 2 == 0:
    print("Even")
    if number >0:
       print("Positive Even Number")
    elif number<0:
       print("Negative Even Number")
elif number %2 ==1:
    print("Odd")
    if number >0:
        print("Positive Odd Number")
    elif number<0:
        print("Negative Odd Number")         
else:
    print("Zero")

#Task 3
number_1=int(input("Enter number 1 :"))
number_2=int(input("Enter number 2 :"))

if number_1> number_2:
   print("The number 1 is greater")
elif number_1<number_2:
   print("The number 2 is greater")
else:
   print("Both number 1 nad 2 are equal")       


#Task 4
number_1=int(input("Enter number 1:"))
number_2=int(input("Enter number 2:"))
number_3=int(input("Enter number 3:"))

if number_1 < number_2 and number_1<number_3 :
   print("Number 1 is Smallest")
elif number_2 < number_1 and number_2<number_3 :
   print("Number 2 is Smallest")
elif number_3 < number_1 and number_3<number_2:
   print("Number 3 is Smallest") 

#Task 5
number_1=int(input("Enter number 1:"))
number_2=int(input("Enter number 2:"))
number_3=int(input("Enter number 3:"))

if number_1 > number_2 and number_1>number_3 :
   print(f"{number_1}Number is Largest")
elif number_2>number_1 and number_2>number_3 :
   print(f"{number_2}Number is Largest")
elif number_3>number_1 and number_3>number_2:
   print(f"{number_3}Number is Largest") 

#Task 6
number=int(input("Enter the number:"))

if number%5==0 and number%11==0:
   print("Divisible by both 5 and 11")
elif number%5==0:
   print("Divisible only by 5")   
elif number%11==0:
   print("Divisible only by 11")  
else:
   print("Divisble by neither")

#Task 7
number=int(input("Enter the number:"))

if number%3==0 and number%7==0:
   print("Divisible by both 3 and 7")
elif number%3==0:
   print("Divisible only by 3")   
elif number%7==0:
   print("Divisible only by 7")  
else:
   print("Divisble by neither")

#Task 8
marks=int(input("Enter the Marks:"))

if marks <0:
   print("Invalide marks")
elif marks >100: 
   print("Invalide marks")
elif marks >= 40:
   print("Pass")
else:
   print("Fail")

#Task 9
marks= int(input("Enter Your Marks:"))

if  marks <=90 or marks >=100:
   print("A")
elif marks <=80 or marks >=89:
   print("B")  
elif marks <= 70 or marks >=79: 
   print("C")
elif marks <= 60 or marks >=69:
   print("D")
elif marks <=40 or marks >=59:
   print("E")         
else:
   print("Fail")

#Task 10
age=int(input("Enter the user age:"))

if age <0:
   print("Invalide age")
elif age >120:
   print("Unrealistic age")
elif age <18 :
   print("Can vote")
else:
   print("Can vote")

#Task 11
year=int(input("Enter the Year:"))

if year % 400 == 0 :
   print("Leap year")
elif year % 4 == 0 and year % 100!=0:
   print("Leap year")   
else:
   print("Not a leap year")  

#Task 12
character=input("Enter the character:")

if character >='A' and character <='Z':
   print("Uppercase Alphabet")
elif character >='a' and character <='z':
   print("Lowercase Alphabet")
elif character >= '0'and character <='9': 
   print("Digit")
else:
   print("Special character")   

#Task 13
char=input("Enter the character:").lower()


#Task 14 
cost_price=int(input("Enter the cost price:"))
selling_price=int(input("Enter the selling price:"))

if cost_price<selling_price:
   print("Profit")
elif cost_price>selling_price:
   print("loss")   
else:
   print("No profit and no loss")

#Task 15
cost_price=int(input("Enter the cost price:"))
selling_price=int(input("Enter the selling price:"))

if cost_price <0:
   print("Invalide Cost Price")

elif selling_price > cost_price:
   profit=selling_price-cost_price
   profit_percentage=(profit/ cost_price)*100

   print("Profit:",profit)
   print("Profit Percentage:",profit_percentage,"%")

elif selling_price < cost_price :
   loss = cost_price - selling_price
   loss_percentage = (loss/cost_price)*100

   print("Loss:",loss)
   print("Loss Percentage:", loss_percentage,"%")
else:
   print("No Profit No Loss")   

#Task 16
electricity_units=float(input("Enter the Units used:"))
first_100=electricity_units*5
second_100=((electricity_units-100)*7)+(100*5)
above_200=((electricity_units-200)*10)+((electricity_units-100)*7)+(100*5)

if electricity_units <=100:
   print(f"First 100 units{first_100}") 
elif electricity_units <=200 :
   print(f"Second 100 units ,{second_100}") 
else:
   print(f"Above 200 units ,{second_100}") 

#--------------------------------------------------------OR-------------------------------------------------------------
bill=int(input("Enter Your Uesd electricity units:"))

if bill <=100:
   print(f"Your electricity bill {bill*5}")
elif bill <=200:
   print(f"Your electricity bill {((bill-100)*7)+500}")
else:
   print(f"Your electricity bill {((bill-200)*10)+1200}")

#Task 17
first_number=int(input("Enter the first number:"))
second_number=int(input("Enter the second number:"))
operation=int(input("Enter aNumber of Following Operations that You Want to preform:\n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Divison \n 5.Floor Divison \n Enter the Operation you Want to:"))


if operation=='+' or operation=='-' or operation=='*' or operation=='/':
   if operation == '+':
       print(f"Addition is:{first_number+second_number}")
   elif operation == '-':
       print(f"Substraction is:{first_number-second_number}")
   elif operation == '*':
       print(f"Multiplication is:{first_number*second_number}")
   elif operation == '/':
      if second_number==0:
         print("Error:Cannot divided by zero")
      else:
         print(f"Divison is:{first_number/second_number}")   
else:
   print("Invalide Operation") 


#Task 18
temperature=int(input("Enter the temperature in Celsius:"))

if temperature <0:
   print("Freezing")
elif temperature>1 and temperature<=15:
   print("Very cold")
elif temperature>=16 and temperature<=25:
   print("Cold")
elif temperature>=26 and temperature<=35:
   print("Normal")
else:
   print("Hot")         

#Task 19
number=int(input("Enter the number:"))

if number <0:
   print("Number is Negative")
elif number>=0 and number<=10:
   print("Number is Between 0-10")
elif number>=11 and number<=50:
   print("Number is Between 11-50")
elif number>=51 and number<=100:
   print("Number is Between 51-100")
else:
   print("Above 100")

#Task 20
a=int(input("Enter the side a :")) 
b=int(input("Enter the side b :"))
c=int(input("Enter the side c :")) 

if a+b>c and a+c>b and  b+c>a:
   print("Valid triangle")
else:
   print("Invalide triangle")      

#Task 21
a=int(input("Enter the side a :")) 
b=int(input("Enter the side b :"))
c=int(input("Enter the side c :")) 

if a+b>c and a+c>b and  b+c>a:
   print("Valid triangle")
   if a==b==c:
      print("Equilateral triangle")
   elif a==b or b==c or a==c:
      print("Isosceles triangle")
   else:
      print("Scalene triangle")      
else:
   print("Invalide triangle")  

#Task 22
balance = int(input("Enter account balance: ₹"))
withdrawal = int(input("Enter withdrawal amount: ₹"))

if withdrawal <= 0:
    print("Invalid withdrawal amount")

elif withdrawal % 100 != 0:
    print("Withdrawal amount must be divisible by 100")

elif withdrawal > balance:
    print("Insufficient balance")

elif balance - withdrawal < 500:
    print("At least ₹500 must remain in the account")

else:
    balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", balance)

#Task 23
username=input("Enter the Username:").lower().strip()
password=input("Enter the password:").lower().strip()

if username !="admin":
   print("User not found")
elif password !="python123":
   print("Wrong password")
else:
   print("Login Successfull")

#Task 24
purchase = float(input("Enter purchase amount: ₹"))

if purchase < 500:
    discount_percent = 0

elif purchase <= 999:
    discount_percent = 5

elif purchase <= 1999:
    discount_percent = 10

elif purchase <= 4999:
    discount_percent = 15

else:
    discount_percent = 20

discount_amount = purchase * discount_percent / 100
final_amount = purchase - discount_amount

print("Original amount: ₹", purchase)
print("Discount percentage:", discount_percent, "%")
print("Discount amount: ₹", discount_amount)
print("Final amount: ₹", final_amount)

#Task 25
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

if (marks1 < 0 or marks1 > 100 or
    marks2 < 0 or marks2 > 100 or
    marks3 < 0 or marks3 > 100):
    print("Invalid marks")

elif marks1 < 35 or marks2 < 35 or marks3 < 35:
    print("Fail")

else:
    average = (marks1 + marks2 + marks3) / 3

    print("Average:", average)

    if average >= 75:
        print("Distinction")

    elif average >= 60:
        print("First Class")

    elif average >= 50:
        print("Second Class")

    else:
        print("Pass")

#Task 26
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

if (marks1 < 0 or marks1 > 100 or
    marks2 < 0 or marks2 > 100 or
    marks3 < 0 or marks3 > 100):
    print("Invalid marks")

elif marks1 < 35 or marks2 < 35 or marks3 < 35:
    print("Fail")

else:
    average = (marks1 + marks2 + marks3) / 3

    print("Average:", average)

    if average >= 75:
        print("Distinction")

    elif average >= 60:
        print("First Class")

    elif average >= 50:
        print("Second Class")

    else:
        print("Pass")

#Task 27 
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if hours < 0 or hours > 23:
    print("Invalid time")

elif minutes < 0 or minutes > 59:
    print("Invalid time")

elif seconds < 0 or seconds > 59:
    print("Invalid time")

else:
    print("Valid time")
#Task 28
name1 = input("Enter name of Person 1: ")
age1 = int(input("Enter age of Person 1: "))

name2 = input("Enter name of Person 2: ")
age2 = int(input("Enter age of Person 2: "))

name3 = input("Enter name of Person 3: ")
age3 = int(input("Enter age of Person 3: "))

if age1 == age2 == age3:
    print("All three people are the same age")

elif age1 == age2 and age1 < age3:
    print(name1, "and", name2, "are the youngest")

elif age1 == age3 and age1 < age2:
    print(name1, "and", name3, "are the youngest")

elif age2 == age3 and age2 < age1:
    print(name2, "and", name3, "are the youngest")

elif age1 < age2 and age1 < age3:
    print(name1, "is the youngest")

elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")

else:
    print(name3, "is the youngest")   

#Task 29
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 < num3:
    print(num1)

elif num1 > num3 and num1 < num2:
    print(num1)

elif num2 > num1 and num2 < num3:
    print(num2)

elif num2 > num3 and num2 < num1:
    print(num2)

else:
    print(num3)

# Task 30
age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: ₹"))
attendance = float(input("Enter attendance percentage: "))

if (18 <= age <= 25 and
    marks >= 85 and
    attendance >= 75 and
    income <= 300000):

    print("Scholarship Approved")

else:
    print("Scholarship Rejected")

    if age < 18 or age > 25:
        print("Reason: Age must be between 18 and 25")

    if marks < 85:
        print("Reason: Marks below 85")

    if attendance < 75:
        print("Reason: Attendance below 75%")

    if income > 300000:
        print("Reason: Family income above ₹300000")     