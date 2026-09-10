#Que 39
purchase_amount = float(input("Enter purchase amount: ₹"))
membership = input("Are you a member? (yes/no): ").lower()

if membership == "yes":
    if purchase_amount >= 5000:
        discount = 20
    else:
        discount = 10

    print(f"Discount: {discount}%")
else:
    discount = 0
    print("Discount: 0%")
            

#Que 40
marks=int(input("Enter your marks:"))

