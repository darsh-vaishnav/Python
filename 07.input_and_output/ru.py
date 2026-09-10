# number=int(input("Enter the 3 Digit number:"))
# a=number%10
# number=number//10
# b=number%10
# number=number//10
# c=number%10
# print(a+b+c)
# #____________________________________or_________________________________________

# num=int(input("ENTER THREE DIGIT NUMBER:"))


# #Cw 2
# for i in range(1,20):
#     if i%2==0:
#        print(f"{i} is even!")

# #Tr
# number=int(input("Enter the number:"))
# for number in range(1,number+1):
#     if number%2==0:
#        print(f"{number} is even!")
#Task 22
account_balance=int(input("Enter the account balance:"))
withdrawl_amount=int(input("Enter the Withdrawl amount:"))

if withdrawl_amount:
   print("Withdrawal successful")
   if withdrawl_amount<0:
      print("Withdrawal amount is greater than 0")
      if withdrawl_amount%100==0:
          print("Withdrawal amount is divisible by 100")   
          if withdrawl_amount>account_balance:
             print ("Withdrawal amount is not greater than the balance")
             if (withdrawl_amount)>500 :
                print("After withdrawal, at least ₹500 must remain") 
             else:
                print("Invalide transiction")   
else:
   print("Invalide transiction") 

#Task 23
username=input("Enter the username:").lower().split()
password=input("Enter the Password:").lower().split()


