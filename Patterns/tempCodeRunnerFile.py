#Star Pyramid 
'''
r = int(input("Enter Number of Rows: "))
for i in range (0,r):
    for j in range(0,i+1):
        print("* ", end=" ")
    print()

#Simple Alphaber Pyramid

r = int(input("Enter Number of Rows: "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()'''

n = 5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()