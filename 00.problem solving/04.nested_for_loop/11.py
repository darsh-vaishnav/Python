# rows=int(input("Enter the number of rows: "))
# cols=int(input("Enter the number of columns: "))
# i=0
# while i<rows :
#     j=2
#     while j<cols:
#         print(j,end=" ")
#         j=j+2
#     print()
#     i=i+1

# for 
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
for i in range(rows):
    for j in range(2,cols,2):
        print(j,end=" ")
    print( )    