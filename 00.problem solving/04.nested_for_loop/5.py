n=int(input("Enter the number: "))

rows=1
while rows<=n:
    columns=1
    while columns<=n:
        print(rows,end="")
        columns=columns+1
    print()
    rows=rows+1 