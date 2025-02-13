import random

from pyexpat.errors import messages


def create_rotor() -> dict:
    """Generate a random roter"""
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)

    rotor = {}
    for letter in alphabet:
        reflection_letter = shuffled_alphabet.pop()
        rotor[letter] = reflection_letter

    return rotor


def encrypt(rotor: dict, message: str) -> str:
    """Encrypt a message"""
    encrypted_message = ""

    for char in message.upper():
        if char in rotor:
            encrypted_letter = rotor[char]
            encrypted_message += encrypted_letter
        else:
            encrypted_message += char

    return encrypted_message


def main():
    while True:
        try:
            n = int(input("How many rotors to create? (3 recommended)"))
            if n > 0:
                break
            else:
                print("The number of rotors must be greater than zero!")
        except ValueError:
            print("Enter an integer!")

    rotors = [create_rotor() for _ in range(n)]

    print("\nRotors' settings:")
    for i, rotor in enumerate(rotors, 1):
        print(f"Rotor {i}: {rotor}")

    while True:
        message = input("\nEnter the message you want to encrypt: ").strip()
        if message:
            break
        else:
            result = input('Do you have nothing to encrypt? (enter "yes" or "no")')
            if result == "yes":
                print("Then, auf wiedersehen 😊")
                exit()

    encrypted_message = message
    for rotor in rotors:
        encrypted_message = encrypt(rotor, encrypted_message)

    print(f"Encrypted message:{encrypted_message}")


if __name__ == "__main__":
    main()  # Run the program
