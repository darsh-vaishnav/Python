

# #Q1]

print("""Our Menu 
         1.Pizza 
         2. Burger 
         3. Pasta 
         4. Sandwich""")
num = int(input("Enter your choice: "))

match num:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")
    case 4:
        print("You selected Sandwich")
    case _ :
        print("Invalid Input")

# #Q2]

print("""Mobile Setting
         1.Wi-Fi
         2.Bluetooth
         3.Mobile Data
         4.Airplane Mode 
          Exit""")
numb = int(input("Enter your choice: "))

match numb:
    case 1:
        print("Wi - Fi selected")
    case 2:
        print("Bluetooth selected")
    case 3:
        print("Mobile data selected")
    case 4:
        print("airplane mode selected")
    case 5:
        print("Exited!")
    case _:
        print("Invalid Input")

# #Q3]

print("""ATM menu
         1. Check Balance 
         2. Withdraw Money  
         3. Deposit Money
         4. Change PIN 
         5.  Exit""")
bank = int(input("Enter your choice: "))

match bank:
    case 1:
        print("Checking Balance")
    case 2:
        print("Withdrawing Money")
    case 3:
        print("Depositing Money")
    case 4:
        print("Changing PIN")
    case 5:
        print("Exited!")
    case _:
        print("Inavlid Input")

# #Q4]
light = input("""Enter the colour of Ligth at signal: 
                  red
                  yellow
                  green""").lower()

match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _ :
        print("Invalid Input")

# #Q5]
portal = 1
while portal != 5:

    print("""Student portal menu
             1. View Profile 
             2. View Courses  
             3. View Marks 
             4. View Attendance 
             5. Logout""")

    portal = int(input("Enter your choice: "))

    match portal:
        case 1:
            print("Your Profile:")
        case 2:
            print("Courses:")
        case 3:
            print("Your Marks:")
        case 4:
            print("Your Attendance")
        case 5:
            print("Logged Out")
        case _ :
            print("Invalid Input")

# #Q6]

print("""Online shopping menu:
         1 .Electronics 
         2 .Clothing
         3 .Books 
         4 .Grocery
         5 .Exit""")
items = int(input("Enter your choice: "))

match items:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exited!")

# #Q7]
service = 1
while service != 6:

    print("""A banking application provides:
             1 .Account Balance
             2 .Mini Statement 
             3 .Fund Transfer
             4 .Bill Payment
             5 .Customer Support
             6 .Exit""")

    service = int(input("Enter your choice: "))

    match service:
        case 1:
            print("Balance:")
        case 2:
            print("Mini Statement:")
        case 3:
            print("Fund Transfer:")
        case 4:
            print("Bill Payments")
        case 5:
            print("Customer Support")
        case 6:
            print("Exited!")
        case _ :
            print("Invalid Input")

# #Q8]
movie = 1
while movie!= 5:

    print("""movie booking menu:
             1 .Morning Show
             2 .Afternoon Show 
             3 .Evening Show
             4 .Nigth Show
             5 .Exit""")

    movie = int(input("Enter your choice: "))

    match movie:
        case 1:
            print("Morning Show Details are as follows:")
        case 2:
            print("Afternoon Show Details are as follows:")
        case 3:
            print("Evening Show Details are as follows:")
        case 4:
            print("Night Show Details are as follows:")
        case 5:
            print("Exited!")
        case _ :
            print("Invalid Input")

# #Q9]

print(""" The weather condition :
          1 .Sunny
          2 .Rainy
          3 .Cloudy
          4 .Snowy""")
weather = int(input("Enter your Weather: "))

match weather:
    case 1:
        print("Wear Sunglasses")
    case 2:
        print("Carry an Umbrella")
    case 3:
        print("Weather may Change")
    case 4:
        print("Wear warm clothes")
    case _:
        print("Unkown Weather")

# #Q10]

print(""" An online store accepts:
          1 . UPI 
          2 . Card
          3 . Cash
          4 . Wallet""")
payment = int(input("Enter your Payment method: "))

match payment:
    case 1:
        print("UPI Payment selected")
    case 2:
        print("Card Payment selected")
    case 3:
        print("Cash Payment selected")
    case 4:
        print("Wallet Payment selected")
    case _:
        print("Invalid Payment method ")

# #Q11]

print("""Take a file extension as input:
          1 . pdf -> Document 
          2 . jpg -> Image
          3 . png -> Image
          4 . mp3 -> Audio
          5 . mp4 -> Video""")
file = int(input("Enter Extension: "))

match file:
    case 1:
        print("Document File")
    case 2:
        print("Image File")
    case 3:
        print("Image File")
    case 4:
        print("Audio File")
    case 5:
        print("Video File")
    case _:
        print("Unknown File Type")

# #Q12]

print("""A system supports these roles:
         1 . Admin 
         2 . Teacher
         3 . Student
         4 . Guest""")
roles = int(input("Enter your role: "))

match roles:
    case 1:
        print("Full Access")
    case 2:
        print("Teacher Dashboard")
    case 3:
        print("Student Dashboard")
    case 4:
        print("Limited Access")
    case _:
        print("Unkown Role")

#Q13]

day_number=int(input("Enter the Day Number: "))

match day_number:
    case 1 | 2 | 3 | 4 | 5 :
        print("Weekday")
    case 6 | 7 :
        print("Weekend")
    case _ :
        print("Invalid Day")

# #Q14]

print("""A support system receives priority numbers:
         1 . Low 
         2 . Medium
         3 . High
         4 . Critical""")
priority = int(input("Enter priority number: "))

match priority:
    case 1 | 2:
        print("Normal")
    case 3 | 4:
        print("Urgent")
    case _:
        print("Unkown Priority number")

#Q15]

print("""A store uses membership levels:
         1 . Bronze 
         2 . Silver
         3 . Gold
         4 . Platinium""")
membership = int(input("Enter Your Membership Level: "))

match membership:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("Unkown Membership Level")   


# Q16]

account = input("""Enter your account type:-
                     Student
                     Teacher""").strip().lower()
student_choice = int(input("""Enter your choice number:-
                              1 . View Courses
                              2 . View Marks
                              3 . View Attendance"""))
teacher_choice = int(input("""Enter your choice number:-
                              1 . View Students
                              2 . Enter Marks
                              3 . View Attendance"""))

match account:

    case "student":

        match student_choice:
            case 1:
                print("View Courses")
            case 2:
                print("View Marks")
            case 3:
                print("View Attendance")
            case _:
                print("Invalid Choice")

    case "teacher":

        match teacher_choice:
            case 1:
                print("View Students")
            case 2:
                print("Enter Marks")
            case _:
                print("Invalid Choice")

    case _:
        print("Invalid Account Type")


# Q17]

account = input("""Enter your account type:-
                    Savings
                    Current""").strip().lower()
choice=int(input("""Enter your choice number:-
                     1 . Check Balance
                     2 . Deposit
                     3 . Withdraw"""))

match account:
    case "savings":


        match choice:
            case 1: 
                print("Check Balance")
            case 2:
                print("Deposit")
            case 3:
                print("Withdraw")


    case "current":


        match choice:
            case 1:
                print("Check Balance")
            case 2:
                print("Deposit")
            case 3:
                print("Withdraw")

    case _:
        print("Invalid Account type")                                            


# Q18]

category = input("""Enter your category:-
                    Electronics
                    Clothing""").strip().lower()
electronics_choice=int(input("""Enter your choice number:-
                                 1.Mobile
                                 2.Laptop
                                 3.Headphones"""))
clothing_choice=int(input("""Enter your choice number:-
                                 1.Shirt
                                 2.Jeans
                                 3.Shoes"""))
match category:
    case "electronics":
        match electronics_choice:
            case 1:
                print("Mobile")
            case 2:
                print("Laptop")
            case 3:
                print("Headphones")
    case "clothing":
        match clothing_choice:
            case 1:
                print("Shirt")
            case 2:
                print("Jeans")
            case 3:
                print("Shoes")
    case _:
        print("Invalid category")   

#Q19]


category = int(input("""Enter category:-
                         Vegetarian
                         Non-Vegetarian"""))
veg_food = int(input("""Enter food:-
                         1.Paneer
                         2.Dal
                         3.Veg Biryani """))
non_veg_food = int(input("""Enter food:-
                         1.Chicken Biryani
                         2.Chicken Curry
                         3.Fish Fry """))

match category:
    case 1:
        match veg_food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")

    case 2:
        match non_veg_food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")

    case _:
        print("Invalid Category")  

#Q20]
print("""Take two numbers and an operator:
         1 . Addition 
         2 . Subtraction
         3 . Multiplication 
         4 . Division
         5 . Floor Division""")
number=int(input("Enter your choice number:-"))
a=int(input("Enter your first integer:-"))
b=int(input("Enter your second integer:-")) 
match number:
    case 1:
        print(f"Addition is {a+b}")
    case 2:
        print(f"Subtraction is {a-b}")          
    case 3:
        print(f"Multiplication is {a*b}")
    case 4:
        print(f"Division is {a/b}")
    case 5:
        print(f"Floor Division is {a//b}")
    case _:
        print("Invalid choice number")




#Q21]


print("""a converter:
         1 .Celcius to Fahrenheit 
         2 .Fahrenheit to Celsius""")
choice=int(input("Enter your choice number:-"))   
temp=int(input("Enter your temperature:-"))

match choice:
    case 1:
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {fahrenheit}°F")


    case 2:
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {celsius}°C")

    case _:
        print("Invalid choice number") 




#Q22]      

print("""Create a unit conversion menu:
         1 . Kilometers to meters 
         2 . Meters to Kilometers 
         3 . Kilograms to Grams 
         4 . Grams to Kilograms""") 

choice=int(input("Enter your choice number:-")) 
num=int(input("Enter your value:-"))

match choice:
    case 1:
        meters = num*1000 
        print(f"{num} kms  is equal to {meters} meters") 
    case 2:
        kilometers=num/1000
        print(f"{num} meters is equal to {kilometers} kms") 
    case 3:
        grams=num*1000
        print(f"{num} kilograms is equal to {grams} grams.")
    case 4:
        kilograms=num/1000
        print(f"{num} grams is equal to {kilograms} kgs.") 
    case _:
        print("Invalid choice number") 



# Q23] 

account_type=input("""Enter your account type:-
                      1 . savings
                      2 . current""").strip().lower() 
amount=int(input("Enter your amount:-"))

match account_type:
    case "savings": 
        if amount>0:
            print("Withdrawal Request Accepted") 
        else:
            print("Invalid amount") 
    case "current":
        if amount>0:
            print("Withdrawal request Accepted")
        else:
            print("Invalid Amount") 
    case _:
        print("Invalid CAccount Type")




# Q24] 

print("""Create a menu:
          1 . Start Exam 
          2 . View Result  
          3 . Exit""")
choice=int(input("Enter your choice Number:-"))
age=int(input("Enter your age:-"))

match choice:
    case 1:
        if age>=18:
            print("You can start the exam")
        else:
            print("You are under threshold age")
    case 2:
        print("You can see your result")
    case 3:
        print("Exam ended")
    case _:
        print("Invalid choice number")               
    


#Q25]
print(""" a movie ticket menu:
          1 . Regular 
          2 . Premium 
          3 . VIP  """)

ticket_type = int(input("Enter ticket type: "))
age = int(input("Enter your age: "))
match ticket_type:
    case 1:
        if age<=5:
         print("Free Ticket")
        else:
            print("Your selected ticket type is ", ticket_type)
    case 2:
        if age<=5:
            print("Free Ticket")
        else:
            print("Your selected ticket type is ", ticket_type)
    case 3:
         if age<=5:
                     print("Free Ticket")
         else:
                     print("Your selected ticket type is ", ticket_type)
    case _:
       print("Invalid ticket type") 



# Q26]

print(""" A smart home controller:
          1 . Light
          2 . Fan
          3 . AC
          4 . TV""")

choice = int(input("Enter device: "))

match choice:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")



# Q27]

print(""" a hospital department menu:
          1 . General Medicine
          2 . Cardiology
          3 . Orthopedics
          4 . Pediatrics
          5 . Emergency""")

choice = int(input("Enter department: "))

match choice:
    case 1:
        print("General Medicine Selected")
    case 2:
        print("Cardiology Selected")
    case 3:
        print("Orthopedics Selected")
    case 4:
        print("Pediatrics Selected")
    case 5:
        print("Emergency Selected")
    case _:
        print("Invalid Department")


# Q28]

print("""a railway ticket menu:
         1 . Book Ticket
         2 . Cancel Ticket
         3 . Check PNR
         4 . Train Schedule
         5 . Exit""")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Book Ticket Selected")
    case 2:
        print("Cancel Ticket Selected")
    case 3:
        print("Check PNR Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")


# Q29]

print("""a railway ticket menu:
       1 . Search Book
       2 . Issue Book
       3 . Return Book
       4 . View Issued Books
       5 . Exit""")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Search Book Selected")
    case 2:
        print("Issue Book Selected")
    case 3:
        print("Return Book Selected")
    case 4:
        print("View Issued Books Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")



# Q30]

print(""" an order status:
           placed
           confirmed
           preparing
           out_for_delivery
           delivered 
           cancelled""")

status = input("Enter status: ").strip().lower()

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order has been confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid Order Status")


# Q31]

print("""a banking application.:
          1 . Personal Banking
          2 . Business Banking""")

banking_type = int(input("Enter banking type: "))

match banking_type:

    case 1:
        print("""Personal Banking:
                 1 . Balance
                 2 . Transfer
                 3 . Loan""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Personal Banking - Balance Selected")
            case 2:
                print("Personal Banking - Transfer Selected")
            case 3:
                print("Personal Banking - Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("""Business Banking:
                  1 . Balance
                  2 . Payroll
                  3 . Business Loan""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Business Banking - Balance Selected")
            case 2:
                print("Business Banking - Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")


# 32]

print("""a school management system
         1 . Student
         2 . Teacher
         3 . Parent""")

role = int(input("Enter role: "))

match role:

    case 1:
        print("""Student options
                 1 . Marks
                 2 . Attendance
                 3 . Homework""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Student Marks Selected")
            case 2:
                print("Student Attendance Selected")
            case 3:
                print("Student Homework Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("""Teacher options:
                 1 . Enter Marks
                 2 . Attendanc
                 3 . Assign Homework""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Enter Marks Selected")
            case 2:
                print("Teacher Attendance Selected")
            case 3:
                print("Assign Homework Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("""Parent options:
                 1 . Child Marks
                 2 . Child Attendance
                 3 . Contact Teacher""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Child Marks Selected")
            case 2:
                print("Child Attendance Selected")
            case 3:
                print("Contact Teacher Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")



# 33]

print("""Select transport:
         1 . Flight 
         2 . Train
         3 . Bus""")

transport = int(input("Enter transport: "))

match transport:

    case 1:
        print("""Flight:
                 1 . Economy
                 2 . Business""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Economy Selected")
            case 2:
                print("Business Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("""Train:
                 1 . Sleeper
                 2 . AC""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Sleeper Selected")
            case 2:
                print("AC Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("""Bus:
                 1 . Ordinary
                 2 . Volvo""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Ordinary Selected")
            case 2:
                print("Volvo Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Transport")


# Q 34]

print(""" a gaming console menu:
           1 . Start Game
           2 . Load Game
           3 . Settings
           4 . Exit""")

choice = int(input("Enter choice: "))

match choice:

    case 1:
        print("Game Started")

    case 2:
        print("Game Loaded")

    case 3:
        print("""Settings is selected:
                 1 . Sound
                 2 . Graphics
                 3 . Controls""")
        option = int(input("Enter setting: "))

        match option:
            case 1:
                print("Sound Settings Opened")
            case 2:
                print("Graphics Settings Opened")
            case 3:
                print("Controls Settings Opened")
            case _:
                print("Invalid Setting")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")



# Q 35]

print("""First select a category:
         1 . Starters
         2 . Main Course
         3 . Desserts
         4 . Drinks""")

category = int(input("Enter category: "))

match category:

    case 1:
        print("""Starters:
                 1 . Soup
                 2 . Spring Roll
                 3 . Garlic Bread""")
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Item")

    case 2:
        print("""Main Course:
                 1 . Pizza
                 2 . Pasta
                 3 . Biryani""")
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Item")

    case 3:
        print("""Desserts:
                 1 . Ice Cream
                 2 . Cake
                 3 . Gulab Jamun""")
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Item")

    case 4:
        print("""Drinks:
                 1 . Coffee
                 2 . Tea
                 3 . Juice""")
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Item")

    case _:
        print("Invalid Category")



# Q36] 

print("""Payment type:
         1 . UPI
         2 . Card
         3 . Wallet""")

payment = int(input("Enter payment type: "))

match payment:

    case 1:
        print("""If UPI is selected:
                 1 . Scan QR
                 2 . Enter UPI ID""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("""If Card is selected:
                 1 . Credit Card
                 2 . Debit Card""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("""If Wallet is selected:
                 1 . Add Money
                 2 . Pay Using Wallet""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Payment Type") 



# Q37]

print("""First select:
         1 . Programming
         2 . Mathematics
         3 . Communication""")

subject = int(input("Enter subject: "))

match subject:

    case 1:
        print("""Programming:
                 1 . Python
                 2 . Java
                 3 . C++""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("""Mathematics:
                 1 . Algebra
                 2 . Calculus
                 3 . Statistics""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("""Communication:
                 1 . English
                 2 . Presentation
                 3 . Interview Skills""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Subject")




# Q 38]

print("""Main options:
         1 . Engine
         2 . Lights
         3 . Music
         4 . Navigation""")

choice = int(input("Enter choice: "))

match choice:

    case 1:
        print("""For Engine:
                 1 . Start
                 2 . Stop""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Option")

    case 2:
        print("""For Lights:
                1 . Headlights
                2 . Indicators
                3 . Hazard Lights""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("""For Music:
                 1 . Play
                 2 . Pause
                 3 . Next
                 4 . Previous""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Song")
            case 4:
                print("Previous Song")
            case _:
                print("Invalid Option")

    case 4:
        print("""For Navigation:
                 1 . Start Navigation
                 2 . Stop Navigation""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Choice")



# Q39]

print("""Main menu:
         1 . Employee
         2 . Manager""")

role = int(input("Enter role: "))

match role:

    case 1:
        print("""Employee options:
                 1 . View Profile
                 2 . Apply Leave
                 3 . View Salary""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("View Profile Selected")

            case 2:
                leave_days = int(input("Enter number of leave days: "))

                if leave_days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")

            case 3:
                print("View Salary Selected")

            case _:
                print("Invalid Option")

    case 2:
        print("""Manager options:
                  1 . View Team
                  2 . Approve Leave
                  3 . View Reports""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("View Team Selected")
            case 2:
                print("Approve Leave Selected")
            case 3:
                print("View Reports Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")


# Q40]

print("""Main menu:
         1 . Student
         2 . Teacher
         3 . Administration""")

role = int(input("Enter role: "))

match role:

    case 1:
        print("""Student:
                 1 . Profile
                 2 . Marks
                 3 . Attendance
                 4 . Courses""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Option")

    case 2:
        print("""Teacher:
                 1 . Students
                 2 . Enter Marks
                 3 . Attendance
                 4 . Courses""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Students")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Option")

    case 3:
        print("""Administration:
                 1 . Fees
                 2 . Admissions
                 3 . Notices
                 4 . Departments""")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Fees")
            case 2:
                print("Opening Admissions")
            case 3:
                print("Opening Notices")
            case 4:
                print("Opening Departments")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")