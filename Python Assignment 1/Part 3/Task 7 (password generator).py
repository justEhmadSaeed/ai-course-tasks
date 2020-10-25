import random
import string

def main():

    length = int(input("Enter the length of Password: "))
    print("1. Very Strong")
    print("2. Strong")
    print("3. Moderate")
    print("4. Weak")
    strength = int(input("Choose the Password strength: "))
    
    if strength == 1:
        sample = f'{string.ascii_letters}{string.digits}{string.punctuation}'
    elif  strength == 2:
        sample = f'{string.ascii_letters}{string.digits}'
    elif  strength == 3:
        sample = f'{string.ascii_letters}'
    else:
        sample = f'{string.ascii_lowercase}'

    sample = list(sample)
    random.shuffle(sample)
    password = ''.join(random.choices(sample, k=length))
    print(password)

if __name__ == "__main__":
    main()