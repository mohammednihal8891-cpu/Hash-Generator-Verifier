import hashlib
import os

HASH_FILE = "original_hash.txt"


def generate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


while True:
    print("\n" + "=" * 45)
    print("       HASH GENERATOR & VERIFIER")
    print("=" * 45)
    print("1. Generate Hash")
    print("2. Verify File")
    print("3. Exit")
    print("=" * 45)

    choice = input("Enter your choice: ")

    if choice == "1":

        filename = input("Enter file name: ")

        if os.path.exists(filename):
            file_hash = generate_hash(filename)

            print("\nSHA-256 Hash:")
            print(file_hash)

            with open(HASH_FILE, "w") as file:
                file.write(file_hash)

            print("\n[+] Hash saved successfully!")

        else:
            print("\n[!] File not found!")

    elif choice == "2":

        filename = input("Enter file name: ")

        if os.path.exists(filename):

            if os.path.exists(HASH_FILE):

                current_hash = generate_hash(filename)

                with open(HASH_FILE, "r") as file:
                    original_hash = file.read().strip()

                print("\nOriginal Hash:")
                print(original_hash)

                print("\nCurrent Hash:")
                print(current_hash)

                if current_hash == original_hash:
                    print("\n[+] FILE IS ORIGINAL")
                else:
                    print("\n[!] FILE HAS BEEN MODIFIED")

            else:
                print("\n[!] No original hash found!")
                print("Generate a hash first.")

        else:
            print("\n[!] File not found!")

    elif choice == "3":

        print("\nExiting...")
        break

    else:
        print("\n[!] Invalid choice!")
