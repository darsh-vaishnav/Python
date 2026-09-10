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
first_number=int(input("Enter First number"))
second_number
      