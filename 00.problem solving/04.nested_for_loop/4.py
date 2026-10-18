# Que 4
rows=0
while rows<=1:
    columns=0
    while columns<=2:
        print(f"({rows},{columns})",end=" ")
        columns=columns+1
    print()
    rows=rows+1 

# for
rows=int(input("Enter the rows: "))
columns=int(input("Enter the columns: "))
for i in range (1,1+rows):
    for j in range (1,1+columns):
        print(f"({i},{j})",end=" ")
    print()    
