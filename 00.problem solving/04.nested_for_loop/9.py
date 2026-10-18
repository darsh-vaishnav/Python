# rows=int(input("Enter the rows:"))
# columns=int(input("Enter the columns:"))

# i=1
# while i<=rows:
#     j=1
#     while j<=columns:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1 

# for
rows = int(input("Enter the rows: "))
columns = int(input("Enter the columns: "))

for i in range (1,1+rows):
    for j in range (1,1+columns):
        print("*",end=" ")
    print()    

