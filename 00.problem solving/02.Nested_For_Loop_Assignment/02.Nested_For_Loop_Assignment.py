# 1
# for i in range(1,4):
#     for j in range(1,4):
#         print("*",end=" ")
#     print()

# 2
# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

#3
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#4
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

#5
# n=6
# i=0
# for i in range(1,n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

#6
# n=5
# j=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#7
# n=5
# i=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

#8
# for i in range(1, 6):
#     print("Table of", i)

#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

#     print()

#9
# i=1
# for i in range(1,4):
#     for j in range(1,6):
#         print(i*j,end=" ")
#     print()

#10
# i=1
# for i in range(1,6):
#     for j in range(1,6):
#         print(j*j,end=" ")
#     print()

#11
# for i in range(1, 6):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()

#12
# for i in range(1, 6):
#     for j in range(i):
#         print(chr(64 + i), end=" ")
#     print()

# #13
# for i in range(1, 6):
#     for j in range(i):
#         print(chr(64 + i), end=" ")
#     print()

# 12. Repeated Alphabet Pattern

for i in range(5):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


# 13. Odd Number Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print()


# 14. Even Number Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(2 * j, end=" ")
    print()


# 15. 5×5 Star Square

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# 16. 5×5 Number Square

for i in range(5):
    for j in range(1, 6):
        print(j, end=" ")
    print()


# 17. Row-wise Numbers

num = 1

for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num = num + 1
    print()


# 18. Print 1 to 20 in 4 Rows

num = 1

for i in range(4):
    for j in range(5):
        print(num, end=" ")
        num = num + 1
    print()


# 19. Print Coordinate Pairs

for i in range(1, 4):
    for j in range(1, 4):
        print("(", i, ",", j, ")", end=" ")
    print()


# 20. Print All Number Combinations

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 21. 10×10 Multiplication Grid

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()


# 22. Repeated Number Pattern

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()


# 23. Decreasing Number Pattern

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 24. Reverse Number Pattern

for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()


# 25. Repeated Row Number Pattern

for i in range(1, 6):
    for j in range(5):
        print(i, end="")
    print()