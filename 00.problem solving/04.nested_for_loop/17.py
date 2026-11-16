# n=int(input("Enter the number: "))
# for i in range (1,1+n):
#     for j in range (1,1+n):
#         if j%i==0 :
#             print(j,end=" ")
#     print( )

# for
n=int(input("Enter the number: ")) 
i=1
while i<=n:
    j=1
    while j<=n:
        if j%i==0:
            print(j,end=" ")
        j+=1
    print( )    
    i+=1
