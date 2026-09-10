
# 1.

for i in range(5):
    print("Hello")


# 2.

for i in range(10):
    print(i, end=" ")

print()


# 3.

for i in range(1, 11):
    print(i, end=" ")

print()


# 4.

for i in range(10, 0, -1):
    print(i, end=" ")

print()


# 5.
for i in range(5, 51, 5):
    print(i, end=" ")

print()

# 6.

for i in range(2, 21, 2):
    print(i, end=" ")

print()


# 7.

for i in range(1, 20, 2):
    print(i, end=" ")

print()


# 8.

for i in range(3, 19, 3):
    print(i, end=" ")

print()


# 9.

for i in range(20, 1, -2):
    print(i, end=" ")

print()


# 10.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i, end=" ")

print()

# 11.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()


# 12. 

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")

print()


# 13.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, end=" ")

print()


# 14. 

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")

print()


# 15.

n = int(input("Enter n: "))

count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count = count + 1

print("Number of even numbers:", count)



# 16.

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


# 17.

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total = total + i

print("Sum of even numbers:", total)


# 18.

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total = total + i

print("Sum of odd numbers:", total)


# 19. 

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 20.

n = int(input("Enter n: "))

result = 1

for i in range(1, n + 1):
    result = result * i

print("Factorial:", result)

# 21. 

text = input("Enter a string: ")

for character in text:
    print(character)


# 22. 

text = input("Enter a string: ")

for character in text:
    print(character, end="")

print()


# 23. 

text = input("Enter a string: ")

count = 0

for character in text:
    count = count + 1

print("Number of characters:", count)


# 24.

text = input("Enter a string: ")

count = 0

for character in text:
    if character == "a":
        count = count + 1

print("Number of a:", count)


# 25. 

text = input("Enter a string: ")

count = 0

for character in text:
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count = count + 1

print("Uppercase characters:", count)

# 26.

for i in range(3):
    for j in range(4):
        print("*", end="")
    print()


# 27.

for i in range(4):
    for j in range(5):
        print("*", end="")
    print()


# 28.

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


# 29.

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 30

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

