def change_password(username, current_password, new_password, passwd_file):
   
    # Read all lines from the password file
    with open(passwd_file, 'r') as file:
        lines = file.readlines()

    # Write back to the password file, updating the password if conditions are met
    with open(passwd_file, 'w') as file:
        for line in lines:
            # Split the line into parts using colon as a separator
            user_parts = line.split(":")

            # Check if the current line corresponds to the specified username
            # and if the current password matches the existing password
            if user_parts[0] == username and user_parts[2].strip() == current_password:
                # Write the updated password to the file
                file.write(f"{username}:{user_parts[1]}:{new_password}\n")
                print("Password changed.")
            else:
                # Write the line as it is to the file
                file.write(line)

if __name__ == "__main__":
    # Get user input for username and passwords
    username = input("Enter username: ")
    current_password = input("Enter current password: ")
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new passsword: ")

    # Check if the new and confirm passwords match
    if new_password == confirm_password:
        # Define the path to the password file
        passwd_file = "passwd.txt"
        # Call the change_password function
        change_password(username, current_password, new_password, passwd_file)
    else:
        print("Passwords do not match.")
