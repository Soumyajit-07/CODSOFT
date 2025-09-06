def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return "Zero is not allow by Division"
    return x/y
def mod(x,y):
    if y == 0:
        return "Zero is not allow by Modular"
    return x%y
a = int(input("User Choise:-"))
b = int(input("User Choise:-"))
while True:
    print("\nOptions: A-Add | B-Sub | C-Mul | D-Div | E-Mod | F-Exit")
    Choose = input("User Choice: ")

    if Choose == "A":
        print("Addition: ",add(a,b))
    elif Choose == "B":
        print("Subtraction: ",sub(a,b))
    elif Choose == "C":
        print("Multiplication: ",mul(a,b))
    elif Choose == "D":
        print("Diviso :",div(a,b))
    elif Choose == "E":
        print("Modular :",mod(a,b))
    elif Choose == "F":
        print("Exit to Calculator")
        break
    else:
        print("⚠️ Invalid choice, try again")
