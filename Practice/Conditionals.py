#Example of Conditionals.. --
# { If, Else}

a = 66
if a > 55:
    print(a,"Is Greater than 55")

if a > 67:
    print(a, "is greater than 67")
else:
    print(a,"is smaller than 67")

def greet(name):
    return ("Hello ", name+ "!" )
x = greet("Anas")
print(x)
#Combining conditional and functions
def is_even(number):
    if number % 2==0:
        return True
    else:
        return False
number = 5
if is_even(number):
    print(number,"is Even ")
else:
    print(number,"is Odd")