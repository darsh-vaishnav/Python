#cw
age=int(input("Enter Your Age:").split()[0])
Gender=input("Enter your Gender:")
Gender=Gender.lower().strip()
print(age ,Gender)
if age>=18:
    if Gender=="female":
        print("Seat is available for you!!")
    if Gender!="female":
            print("Seat is not available for you!!") 



#Que 1
number=int(input("Enter the Number:"))
if number >= 10:
   print("Greater than 10.")

#Que 2
age=int(input("Enter persons age:"))
if age >= 18:
   print("Adults")

#Que 3
number=int(input("Enter the number from user:"))
if number >=0:
   print("Number is Positive")

#Que 4
marks=int(input("Enter the marks of student:"))
if marks >= 40:
   print("Then Student is Pass")

#Que 5   
num = int(input("Enter a number: "))
if num == 0:
    print("Zero")

#Que 6
number=int(input("Enter a number:"))
if number >=0:
   print("Number is positive")
else:
   print("Number is Not positive")

#Que 7
age=int(input("Enter persons age:"))
if age >= 18:
   print("Adult")
else:
   print("Minor")

#Que 8                
number=int(input("Enter a number:"))
if number%2==0:
   print("Number is even ")
else : 
   print("Number is odd")

#Que 9   
marks=int(input("Enter the marks of student:"))
if marks >= 40:
   print("Pass")
else:
   print("Fail")

#Que  10
number=int(input("Enter the marks of student:"))
if number >= 10:
   print("Number is Greater")
else:
   print("Number is Smaller") 

#Que 11
marks=int(input("Enter the marks:"))
if marks >= 90:
   print("A")
elif marks  >= 75:
   print("B")
elif marks  >= 60 :
   print("C")   
elif marks  >= 40:
   print("D")
elif marks  <= 40:
   print("F")   

#Que 12
number=int(input("Enter the number :"))
if number >= 1:
   print("Positive")
elif number == 0 :
   print("Zero")
else:
   print("Negative")

#Que13
number=int(input("Enter the number :"))
if number == 1:
   print("Monday")
elif number ==2 :
   print("Tuesday")
elif number ==3 :
   print("Wednesday")
elif number ==4 :
   print("Thursday")
elif number ==5 :
   print("Friday")
else:
   print("Other")

#Que 14
marks=int(input("Enter your age:"))
if marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#Que 15
number=int(input("Enter the number :"))
if number == 1:
   print("1")
elif number ==2 :
   print("2")
elif number ==3 :
   print("3")
else:
   print("Other")

#Que 16
age=int(input("Enter your age:"))

if age >= 18:
   if age <=60:
      print("Age is Between 18 and 60")

#Que 17
marks=int(input("Enter the marks:"))

if marks >= 40:
   if marks >=75:
      print("Good")
   else:
      print("Passed")
else:
   print("Failed")       
   
#Que 18
number=int(input("Enter the number:"))

if number >= 0:
   if number >=100:
      print("Number is Greater then 100")
   else:
      print("Number is positve")   
else:
   print("Number is negative")

#Que 19
age=int(input("Enter the age :"))

if age >= 18:
   if marks >=60:
      print("")
   else:
      print("Passed")
else:
   print("Failed")

#Que 20
number=int(input("Enter the number:"))

if number != 0:
   if number >0:
      print("Positive")
   else:
      print("Negative")   
else:
   print("Zero")

#Que 21
age=int(input("Enter the age:"))
marks=int(input("Enter the marks: "))

if age >=18 and marks >=40:
   print("Eligible")
else :
   print("Not Eligible")

#Que 22
number=int(input("Enter the number:"))

if number <10 or number>100:
   print("Special")
else:
   print("not special")

#Que 23
user_age=int(input("Enter the age:"))
has_id=bool(input("Enter the user id (True/False):")) =="True"

if age >= 18 :
   if has_id is True:
      print("Allowed")
   else:
      print("Not Allowed")

#Que 24
first_number=int(input("Enter the first_number:"))
second_number=int(input("Enter the second number:"))

if first_number>10 and second_number>10 :
   print("Both are greater than 10")

#Que 25
number=int(input("Enter the number:"))

if number <0 or number>100:
    print("Special")

#Que 26
is_closed=input("Is the door closed? (True/False):")

if not (is_closed=="True"):
   print("OPen")
else:
   print("Closed")

#Que 27
number=("Enter the number:")

if number >=10 and number<=50:
   print("Between the 10 and 50")
else:
   print("Not between 10 and 50")

#Que 28
number = int(input("Enter the number: "))

if number >= 10 and number <= 50:
    print("Number is between 10 and 50")

#Que 29
is_student = True
has_id = True
has_ticket = True

if is_student and has_id and has_ticket:
    print("Allowed")

 # Que 30
age=int(input("Enter the age:"))   
marks=int(input("Enter the marks:"))
has_id=input("Do you have an ID? (True/False):") =="True"

if age >=18 and marks >=40 and has_id:
   print("Eligible")
else:
   print("Not eligible")   