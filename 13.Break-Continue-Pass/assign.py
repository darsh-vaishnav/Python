# Que 1
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished") 

# Output
#1
#2
#3
#4
#Finished

# Que 2

word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)
# Output
# s
# k
# y
# l    

# Que 3
n = 2

while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2

# Output
# 2
# 4
# 6
    

####### part a 2    
# Que 4
limit=int(input("Enter the number: "))
for i in range (1,limit+1):
    if i==7:
        break
    print(i,end=" ")


# Que 5
str = input("Enter the String: ")
target = input("Enter the target character: ")
for ch in str:
    if ch == target:
        break
    print(ch,end="")

# Que 6
num = input("Enter number squence with space: ").split()

for i in num:
    n = int(i)
    if n < 0:
        break
    print(n, end=" ")

####### part a 3   

# Que 7
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

#1 1
#1 2
#2 1
#2 2
#3 1
#3 2           

# Que 8
sentence = input("Enter sentence with space: ").split()
word = input("Enter the word: ")
target=False
for i in sentence:
    if i == word:
        print("Found")
        found = True
        break
if found == False:
    print("Not found")  

#----------Part B-1------------    

# que 9      
for i in range(1, 7):
    if i == 4:
        continue
    print(i)
# 1
# 2
# 3
# 5
# 6

# Que 10
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")
#dctn

# Que 11
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# 1
# 2
# 4  
# 5  

#----------Part B-2------------

# Que 12
n=int(input("Enter the integer: "))
for i in range (1,1+n):
   if i%3==0:
       continue 
   print(i,end=" ")

# Que 13
# str = input("Enter the String: ")
target = input("Enter the target character: ")
for ch in str:
    if ch == target:
        continue
    print(ch,end="") 

# Que 14     
marks = input("Enter marks space: ").split()

for i in marks:
    marks = int(i)
    if marks <= 40:
        continue
    print(marks, end=" ") 

#----------Part B-3------------    

# Que 15
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)
# A 1
# B 1
# A 3
# B 3
# A 4
# B 4  

# Que 16
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    
    print(n)

# Que 17    
word = input("Enter a word: ")
count = 0

for ch in word:
    if ch in "aeiouAEIOU":
        continue
    count += 1

print(count)

#----------Part C-1------------ 

# Que 18
for i in range(1, 4):
    print(i)
else:
    print("Done")
# 1
# 2
# 3
# Done    

# Que 19
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

# 1
# 3
# 4
# Completed

# Que 20
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")

# 1
# 2
# Outside loop

# Que 21
for item in []:
    print("Inside")
else:
    print("Else block")

# Else block
    
#----------Part C-2------------ 

# Que 22
num = input("Enter integer squence with space: ").split()
find = int(input("Enter the target number:"))
found=False
for i in num:
    if int(i) == find:
        print("Found")
        found = True
        break
if found == False:
    print("Not found") 

# Que 23
word= input("Enter word: ")
ch = input("Enter the character: ")
found=False
for i in word:
    if i == ch:
        print("Character exists")
        found = True
        break
if found == False:
    print("Character missing")  

# Que 24
n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

#----------Part C-3------------  
 
# Que 25   
values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")
# All are even

# Que 26
#case 1
for x in range(3):
    continue
else:
    print("A")
#A

#case 2
for x in range(3):
    break
else:
    print("B")
# 

#case 3
for x in range(0):
    print(x)
else:
    print("C")
#C


# Que 27
string=input("Enter the string:")
for ch in string:
    if string.count(ch) >=2:
        print(ch)
        break
else:
    print("No repeated character") 

#----------Part D-1------------ 

# Que 28
for i in range(1, 4):
    if i == 2:
        pass
    print(i) 
# 1
# 2
# 3          

# Que 29
x = 10

if x > 5:
    pass

print("Finished")
# Finished

# Que 30
for letter in "cat":
    pass

print("Loop ended")
#Loop ended

#----------Part D-2------------ 

# Que 31
for i in range(1,6):
    if i%2==0:
        pass
    print(i)

# Que 32    
choice=int(input("Enter the choice:"))
if choice==1:
    print("Program closed")
elif choice == 2:
    print("Program closed")
    pass
else:
    print("Unknown option")  
    print("Program closed")
     
#----------Part D-3------------ 

# Que 33
# Program A
for i in range(1, 5):
    if i == 3:
        pass
    print(i)
#1
#2
#3
#4
# Program B
for i in range(1, 5):
    if i == 3:
        continue
    print(i)
#1
#2
#4

# Que 34
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

##----------Part E------------

# Que 35
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")

# 1
# 3
# Finished 
   
# Que 36
num = input("Enter integer squence with space: ").split()
find = int(input("Enter the target number:"))
for i in num:
    if int(i) < 0:
        continue
    if i==find :
        print("Target found")
        break
else:
    print("Target Not found")
# Que 37

num = input("Enter integer sequence with space: ").split()

for i in num:
    if int(i) == 0:
        continue
    if int(i) > 0:
        break
    print(int(i))
else:
    print("All values processed")

# Que 38
for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")
# 1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
       
# Que 39

num = input("Enter integer squence with space: ").split()
for i in num:
    if int(i)<0:
        continue
    if int(i) % 4 == 0 and int(i) % 6 == 0:
        print("Found:", int(i))
        break
else:
    print("No matching number")

# Que 34
# 1.Stop searching immediately after finding a username. :break
# 2.Skip a blank string and process the remaining strings. :Continue
# 3.Display "Not found" only when a search loop finishes without finding a match. : for-else
# 4.Keep an unfinished function syntactically valid while its implementation is planned. :pass
# 5.Skip the current number but keep processing later numbers. :continue
# 6.Stop a loop when a user enters a sentinel value. :break
# 7.Report that all items were checked, provided no match caused an early stop. : for-else
# 8.Temporarily leave a conditional block empty without causing a syntax error. : pass