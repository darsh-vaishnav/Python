string=input("Enter the string: ")

for i in range(len(string)):
    flag=False
    for j in range(i):
        if string[i]==string[j]:
            flag=True

    if flag == False:
        total = 0
        for k in range(len(string)):
            if string[i]==string[k]:
               total+=1
    print(f"{string[i]} = {total}")



s = input("Enter a string: ")

counted = ""          # characters already processed

for i in range(len(s)):
    ch = s[i]

    # skip if this character was already counted
    already = False
    for c in counted:
        if c == ch:
            already = True
            break
    if already:
        continue

    # inner loop: count occurrences of ch
    count = 0
    for j in range(len(s)):
        if s[j] == ch:
            count += 1

    print(ch, "=", count)
    counted += ch
    
            