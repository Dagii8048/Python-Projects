import caesarCipher

def ask_continue():
    while True:
        response = input("Shall we continue? 'Y' for yes, 'N' for no: ").strip().lower()
        if response in ('y', 'n'):
            return response == 'y'
        print("Invalid input. Please enter 'Y' or 'N'.")

def get_shift():
    while True:
        try:
            shift = int(input("Enter the shift (non-negative integer): "))
            if shift >= 0:
                return shift
            else:
                print("Shift must be a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_message():
    while True:
        message = input("Enter the message (only letters): ").strip()
        if message.isalpha():
            return message
        print("Message must only contain letters (A-Z or a-z).")

def print_cipher():
    print("Welcome! This app uses the Caesar Cipher for encryption and decryption.")

    while True:
        choice = input(
            "\nChoose an option:\n"
            "  [E] Encrypt\n"
            "  [D] Decrypt\n"
            "  [Q] Quit\n"
            "Your choice: "
        ).strip().lower()

        if choice == 'e':
            print("\n--- Encryption ---")
            message = get_message()
            shift = get_shift()
            result = caesarCipher.caesar_encrypt(message, shift)
            print(f"Encrypted message: {result}")

        elif choice == 'd':
            print("\n--- Decryption ---")
            message = get_message()
            shift = get_shift()
            result = caesarCipher.caesar_decrypt(message, shift)
            print(f"Decrypted message: {result}")

        elif choice == 'q':
            print("Thank you for using our app :)")
            break

        else:
            print("Invalid choice. Please select 'E', 'D', or 'Q'.")
            continue

        # Ask if user wants to continue
        if not ask_continue():
            print("Goodbye! Stay safe :)")
            break

if __name__ == '__main__':
    print_cipher()
