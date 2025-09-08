import random
import string

def Password_Generate(length):
    letter = string.ascii_letters
    digit = string.digits
    symbols = string.punctuation

    all_char = letter+digit+symbols
    Password = "".join(random.choice(all_char) for i in range(length))

    return Password
def show():
    print("=== Password Generator ===")
    
    # Prompt user for password length
    while True:
        try:
            length =  int(input("User Enter a Length: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate and display password
    password = Password_Generate(length)
    print("\nGenerated Password:", password)
show()