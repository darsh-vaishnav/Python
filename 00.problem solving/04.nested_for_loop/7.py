# n=int(input("Enter the number: "))

# rows=1
# while rows<=n:
#     columns=1
#     while columns<=rows:
#         print(columns,end="")
#         columns=columns+1
#     print()
#     rows=rows+1 

# for
n = int(input("Enter the number:")) 
for i in range (1,1+n):
    for j in range(1,i+1):
        print(j,end="")
    print()       