'''

n=3
for i in range(3):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))
def max(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n1:
            return n2
        else:
            return n3
m =max(221,33,1111)
print(str(m))'''
n= 5
print(n*(n+1)/2)
   