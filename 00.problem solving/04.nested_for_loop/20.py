# n=int(input("Enter the number: "))
# for i in range(1,1+n):
#     for j in range(1,1+n):
#         if i==j:
#             print("SPECIAL",end=" ")
#         elif i+j == n:
#             print("PAIR",end=" ")   
#         else:         
#             print("NORMAL",end=" ")
#     print()  


n=int(input("Enter the number: "))
i=1
while i<=n:
    j=1
    while j<=n:
        if i==j:
            print("SPECIAL",end=" ")
        elif i+j == n:
            print("PAIR",end=" ")   
        else:         
            print("NORMAL",end=" ")
        j+=1
    print()
    i+=1
