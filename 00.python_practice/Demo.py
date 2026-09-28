# print("Hello world 1")
# print("Hello world 2")
# print("Hello world 3")
# print("Hello world 4")

# print ("HELLO")
  

uppercase=2
lowercase=3
digit=3
spaces=2
special=3
if uppercase>lowercase and uppercase>digit and uppercase>spaces and uppercase>special:
    print("Uppercase letters are present",uppercase)
elif lowercase>digit and lowercase>spaces and lowercase>special and lowercase>uppercase:
    print("Lowercase letters are present",lowercase)
elif digit>spaces and digit>special and digit>uppercase and digit>lowercase:
    print("Digits are present",digit)
elif spaces>special and spaces>uppercase and spaces>lowercase and spaces>digit:
    print("Spaces are present",spaces)
elif special>0 and special>uppercase and special>lowercase and special>digit and special>spaces:
    print("Special characters are present",special)


