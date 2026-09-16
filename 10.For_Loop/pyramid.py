# num=int(input("Enter row value:"))
# for i in range(1,num):
#     for j in range(1,num-i,):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()    
rows = int(input("enter the rows:"))

for i in range (1,rows+1):
    for space in range(1,rows-i):
        print("",end="")
    for star in range(1,2*i-1):
        print("*",end="")
    print()    