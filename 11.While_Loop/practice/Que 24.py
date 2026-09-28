text = input("Enter a string: ")
count = 0
index = 0
while index < len(text):
    if text[index] == "a":
        count += 1
    index += 1
print("Number of a characters:", count)