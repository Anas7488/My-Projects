import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'k':
            return True
    elif comp == 'p':
        if you =='s':
            return False
        elif you=='k':
            return True
    elif comp == 'k':
        if you =='p':
            return False
        elif you == 's':
            return True

comp = random.choice(['s','p','k'])
you = input("Choose Stone(s) Paper(p) Scissor(k) ")
if you not in['s','p','k']:
    print("Invalid Input! ")
else:
   res= gamewin(comp,you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if res is None:
    print("Tie")
elif res:
    print("You Win")
else:
    print("You loose")


