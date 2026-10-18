# Que 3
rows=1
while rows<=3:
    columns=1
    while columns<=4:
        print("*",end="")
        columns=columns+1
    print()
    rows=rows+1 

# for
char = input("Enter the character: ")
rows = int(input("Enter the rows: "))
columns = int(input("Enter the columns: "))      

for i in range(rows):
    for j in range (columns):
        print(char,end=" ")
    print()    