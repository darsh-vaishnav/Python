n=int(input("Enter the number: "))

rows=1
while rows<=n:
    columns=1
    while columns<=n:
        print(columns,end="")
        columns=columns+1
    print()
    rows=rows+1 

# for  
n = int(input("Enter the numbers: "))
for i in range (1,1+n):
    for j in range (1,1+n):
        print(j,end="")
    print()    
                