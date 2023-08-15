import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    
    try:
        password_length = int(input("Enter desired password length: "))
        if password_length <= 0:
            print("Password length must be a positive integer")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
