#1
text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

counts = {
    "Uppercase": uppercase,
    "Lowercase": lowercase,
    "Digits": digits,
    "Spaces": spaces,
    "Special characters": special
}

highest = max(counts.values())

if list(counts.values()).count(highest) > 1:
    print("Tie")
else:
    for category, count in counts.items():
        if count == highest:
            print("Highest category:", category)

# ---------------------------1--------------------------------#
text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

highest = uppercase

if lowercase>highest:
    highest==lowercase

elif digits>highest:
    highest==uppercase   

elif spaces>highest:
    highest==spaces      

elif special>highest:
    highest==special

tie=0

if uppercase==highest:
    tie+=1
if lowercase==highest:
    tie+=1    
if digits==highest:
    tie+=1   
if spaces==highest:
    tie+=1     
if special==highest:
    tie+=1             

if tie>1:
    print("Highest Category:Tie")
elif uppercase==highest:
    print("Lower Category :Uppercase")    
elif lowercase==highest:
    print("Lower Category :Lowercase")
elif digits==highest:
    print("Lower Category :Digits")
elif spaces==highest:
    print("Lower Category :Spaces")
else:
    print("Lower Category :Special character")


#--------------------------------2----------------------------#

fail=0
Pass=0
Good=0
Excellent=0

for i in range (1,11):
    marks=int(input(f"Enter the marks of students:"))

    if marks<=35:
        print("Fail")
        fail+=1
    elif marks<=50:
        print("Pass") 
        Pass+=1  
    elif marks<=75:
        print("Good")
        good+=1
    elif marks<=100:
        print("Excellent")  
        excellent+=1

print("Number of Student:")
print("Fail:",fail)
print("Pass:",Pass)    
print("Good:",good) 
print("Excellent:",excellent)          

#---------------------3---------------------------
sentence=input("Enter the sentence:")

words=sentence.split()

highest_score=0
highest_word=""

for word in words:

 for character in word:
    if character.lower() in"aeiou":
        score=+2
    elif character.isalpha():
        score=+1
    elif character.isdigit():
        score=+3 
    else:
        score=+4          
        print(word, "=", score)

if score > highest_score:
         highest_score = score
         highest_word = word

print("Word with highest score:", highest_word)
print("Highest score:", highest_score)

#------------4-------------------------------#


for password in range(1,6):
    password=input("Enter the Passwords "+str(i)+":")

    conditions=0
    if len(password) >=8:
        conditions+=1
    for character in password:
        if character.isupper():
            conditions+=1
            break
    for character in password:
        if character.islower():
            conditions+=1
            break    
    for character in password:
        if character.isdigit():
            conditions+=1
            break  
    for character in password:
        if character.isalnum():
                conditions+=1
                break   

    if conditions == 5:
      print("Strong")
    elif conditions >= 3:
      print("Medium")
    else:
      print("Weak")      

#----------------5------------------

sentence = input("Enter a sentence: ")

words = sentence.split()

short = 0
medium = 0
long = 0

for word in words:
    length = len(word)

    print(word, "Length:", length)

    if length <= 3:
        print("Short")
        short += 1

    elif length <= 6:
        print("Medium")
        medium += 1

    else:
        print("Long")
        long += 1

print("Short:", short)
print("Medium :", medium)
print("Long:", long)

#--------------6----------------

for i in range(1, 6):
    number = input("Enter number " + str(i) + ": ")

    number = str(number)

    even = 0
    odd = 0

    for digit in number:
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even digits:", even)
    print("Odd digits:", odd)

    if even > odd:
        print("Even occurs more")
    elif odd > even:
        print("Odd occurs more")
    else:
        print("Equal")

# 7

text = input("Enter a string: ")

for i in range(len(text)):
    ch = text[i]
    already_seen = False

    for j in range(i):
        if text[j] == ch:
            already_seen = True
            break

    if already_seen:
        continue

    occurrences = 0

    for x in text:
        if ch == x:
            occurrences += 1

    if occurrences > 1:
        print(ch, ":", occurrences)

        if occurrences == 2:
            print("Duplicate")
        elif occurrences <= 4:
            print("Repeated")
        else:
            print("Highly Repeated")


# 8 

total = 0
budget = 0
regular = 0
premium = 0
luxury = 0

for i in range(1, 9):
    price = float(input("Enter price of product " + str(i) + ": "))

    total += price

    if price < 500:
        print("Budget")
        budget += 1
    elif price < 2000:
        print("Regular")
        regular += 1
    elif price < 5000:
        print("Premium")
        premium += 1
    else:
        print("Luxury")
        luxury += 1

average = total / 8

print("Total Amount:", total)
print("Budget Products:", budget)
print("Regular Products:", regular)
print("Premium Products:", premium)
print("Luxury Products:", luxury)
print("Average Price:", average)


# 9

text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for i in range(len(text)):
    ch = text[i]
    position = i + 1

    if position % 2 == 0:
        position_type = "Even"
    else:
        position_type = "Odd"

    if ch.isdigit():
        category = "Digit"
        digits += 1

    elif ch.isalpha():
        if ch.lower() in "aeiou":
            category = "Vowel"
            vowels += 1
        else:
            category = "Consonant"
            consonants += 1

    else:
        category = "Special Character"
        special += 1

    print(ch, "Position:", position, position_type, category)

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)


# 10

n = int(input("Enter n: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if j % 3 == 0 and j % 5 == 0:
            print("Z", end=" ")

        elif j % 3 == 0:
            print("X", end=" ")

        elif j % 5 == 0:
            print("Y", end=" ")

        else:
            print(j, end=" ")

    print()        
    