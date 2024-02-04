def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key if mode == "encrypt" else -key
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def main():
    print("\nCaesar Cipher:")
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            plaintext = input("Enter the text to encrypt: ")
            key = int(input("Enter the key : "))
            encrypted_text = caesar_cipher(plaintext, key, "encrypt")
            print("Encrypted Text:", encrypted_text)
        elif choice == "2":
            ciphertext = input("Enter the text to decrypt: ")
            key = int(input("Enter the key : "))
            decrypted_text = caesar_cipher(ciphertext, key, "decrypt")
            print("Decrypted Text:", decrypted_text)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
