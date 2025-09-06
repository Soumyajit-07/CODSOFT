def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
a = int(input("User Choise:-"))
b = int(input("User Choise:-"))
while True:
    print("\nOptions: A-Add | B-Sub | C-Mul | D-Div | E-Mod | F-Exit")
    Choose = input("User Choice: ")

    if Choose == "A":
        print(add(a,b))
    elif Choose == "B":
        print(sub(a,b))
    elif Choose == "C":
        print(mul(a,b))
    elif Choose == "D":
        print(a,b)
    elif Choose == "E":
        print(mod(a,b))
    elif Choose == "F":
        print("Exit")
        break
    else:
        print("⚠️ Invalid choice, try again")