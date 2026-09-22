#1
text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for characters in text:
    if characters.isupper():
        uppercase += 1
    elif characters.islower():
        lowercase += 1
    elif characters.isdigit():
        digits += 1
    elif characters == " ":
        spaces += 1
    else:
        special += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


# if list(values())(highest) > 1:
#     print("Tie")
# else:
#     for category, in items():
#         if 
#             print("Highest category:", category)

#2
fail = 0
passed = 0
good = 0
excellent = 0

for i in range(1, 11):
    marks = int(input(f"Enter marks of student {i}: "))

    if marks < 35:
        print("Fail")
    elif marks < 50:
        print("Pass")
    elif marks < 75:
        print("Good")
    elif marks <= 100:
        print("Excellent")
    

print("Number of students:")
print("Fail:", fail)
print("Pass:", passed)
print("Good:", good)
print("Excellent:", excellent)   



#3
sentence = input("Enter a sentence: ")

words = sentence.split()

highest_score = 0
highest_word = ""

for word in words:
    score = 0

    for ch in word:
        if ch.lower() in "aeiou":
            score += 2
        elif ch.isalpha():
            score += 1
        elif ch.isdigit():
            score += 3
        else:
            score += 4

    print(word, "=", score)

    if score > highest_score:
        highest_score = score
        highest_word = word

print("Word with highest score:", highest_word)
print("Highest score:", highest_score)

#4
