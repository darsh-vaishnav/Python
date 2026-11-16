# n=int(input("Enter the number: "))
# for i in range (1,1+n):
#     for j in range (1,1+n):
#         if i+j>n:
#             print(f"{i} {j}")    


# while
n=int(input("Enter the number: "))    
i=1
while i<=n:
    j=1
    while j<=n:
        if i+j>n:
           print(f"{i} {j}")           
        j+=1    
    i+=1