# for i in range(1,6):
#     for j in range(1,6):
#         if i%j==0:
#             print("X",end=" ")
#         else:
#             print("O",end=" ")
#     print()

i=1
while i<6:
    j=1
    while j<6:
        if i%j==0:
            print("X",end=" ")
        else:
            print("O",end=" ")
        j+=1 
    print( )
    i+=1 