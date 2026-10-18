# n=int(input("Enter the number: "))

# rows=n
# while rows>=1:
#     columns=1
#     while columns<=rows:
#         print(columns,end="")
#         columns=columns+1
#     print()
#     rows=rows-1 

# for
n = int(input("Enter the number:")) 
for i in range (n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()      