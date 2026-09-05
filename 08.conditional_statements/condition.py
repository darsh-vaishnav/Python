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
