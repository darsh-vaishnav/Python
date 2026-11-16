n = int(input("Enter the number: "))
i = 0
while i < n:
    j = 0
    while j < n:
        if i == j:
            print("Same", end=" ")
        else:
            print("Different", end=" ")
        j += 1
    print()
    i += 1



# n=int(input("Enter the number: "))
# for i in range(1,1+n):
#     for j in range(1,1+n):
#         if i==j:
#             print("Same",end=" ")
#         else:
#             print("Different",end=" ")
#     print( )        