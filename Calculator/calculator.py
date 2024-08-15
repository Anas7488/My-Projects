#Python 3 Program for simple Calculator

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

n1 = int(input("Enter First Number"))
n2 = int(input("Enter Second Number"))

print("A = Adding\nB = Subtracting\nC = Multiplying\nD = Divide")
print("Select operation")
choice = input("a/b/c/d: ")
if choice == 'a':
    print(sum(n1,n2))
elif choice == 'b':
    print(sub(n1,n2))
elif choice == 'c':
    print(mul(n1,n2))
elif choice == 'd':
    print(div(n1,n2))
else:
    print("Invalid input")