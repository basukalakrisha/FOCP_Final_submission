
import codecs

def add_user():
    
    # Get user input
    print()
    username = input("Enter new username: ").lower()
    real_name = input("Enter real name: ")
    password = input("Enter password: ").strip()

    # Read existing password file
    with open("passwd.txt", "a+") as file:
        # Move the file cursor to the beginning
        file.seek(0)
        # Read all existing user entries
        existing_users = file.readlines()

        # Check if the username already exists
        if any(username in user_entry for user_entry in existing_users):
            print("Cannot add. Most likely username already exists.")
            return

        # Encrypt password using ROT-13
        encrypted_password = codecs.encode(password, 'rot_13')

        # Add new user entry to the file
        file.write(f"{username}:{real_name}:{encrypted_password}\n")

    print("User Created.")

if __name__ == "__main__":
    add_user()