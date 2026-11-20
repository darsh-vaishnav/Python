# string=input("Enter the string: ")

# for i in range(len(string)):
#     flag=False
#     for j in range(i):
#         if string[i]==string[j]:
#             flag=True

#     if flag == False:
#         total = 0
#         for k in range(len(string)):
#             if string[i]==string[k]:
#                total+=1
#     print(f"{string[i]} = {total}")



s = input("Enter a string: ")  #Store the string

counted = ""          # characters already processed , This variable remembers which characters have already been counted.
                      # Initially:
                      #   counted = ""
                      # After processing B:
                      #   counted = "B"
                      # After processing A:
                      #   counted = "BA"

for i in range(len(s)): #len(s) gives 6.
                        # range(6) produces 0, 1, 2, 3, 4, 5.
                        # The loop visits each character.

    ch = s[i]           # Get the current character
    already = False     #   ch = s[i]
                        #   already = False
                        # For example, when i = 0:
                        #    ch = s[0]       # B
                        #    already = False
                        # already tells us whether the current character was counted before.

    for c in counted:     # skip if this character was already counted
        if c == ch:
            already = True
            break
    if already:
        continue

    count = 0
    for j in range(len(s)):   # inner loop: count occurrences of ch
        if s[j] == ch:
            count += 1

    print(ch, "=", count)
    counted += ch
    
            