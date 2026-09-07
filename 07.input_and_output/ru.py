# #Que 8                
# number=int(input("Enter a number:"))
# if number%2==0:
#    print("Number is even ")
# else:
#    print("Number is odd")
# marks=int(input("Enter the marks:"))
# if marks >= 90:
#    print("A")
# elif marks  >= 75:
#    print("B")
# elif marks  >= 60 :
#    print("C")   
# elif marks  >= 40:
#    print("D")
# elif marks  <= 40:
#    print("F")   
# number=int(input("Enter number:"))
# if number >= 1:
#    print("Positive")
# elif number == 0 :
#    print("Zero")
# elif number <=-1 :
#    print("Negative")      
# age=int(input("Enter Your Age:").split()[0])
# Gender=input("Enter your Gender:")
# Gender=Gender.lower().strip()
# print(age ,Gender)
# # if age>=18:
# #     if Gender=="female":
# #         print("Seat is available for you!!")
# #     if Gender!="female":
# #             print("Seat is not available for you!!")    
# #Que 17
# marks=int(input("Enter the marks:"))

# if marks >= 40:
#    if marks >=75:
#       print("Good")
#    else:
#       print("Passed")
# else:
#    print("Failed")      
#Que 23
#Que 28
# 
#cw 2
first_number=int(input("Enter the First number:"))
second_number=int(input("Enter the Second number:"))
operations=int(input("Operations you can perform: \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Divison \n 5.Floor Divison \n Enter the Operation you Want to") )

if operations == 1:
    print(f"Addition is:{first_number+second_number}")
elif operations == 2:
    print(f"Substraction is:{first_number-second_number}")
elif operations == 3:
    print(f"Multiplication is:{first_number*second_number}")
elif operations == 4:
    print(f"Divison is:{first_number/second_number}")
elif operations == 5:
   print(f"Floor Divison is:{first_number//second_number}")
