n=int(input("Enter the number: "))

rows=n
while rows>=1:
    columns=1
    while columns<=rows:
        print(columns,end="")
        columns=columns+1
    print()
    rows=rows-1 