def delete_user(username, passwd_file):

    # Read all lines from the password file
    with open(passwd_file, 'r') as file:
        lines = file.readlines()

    # Write back to the password file, excluding the specified user
    with open(passwd_file, 'w') as file:
        for line in lines:
            # Skip the line if it starts with the specified username
            if not line.startswith(username + ":"):
                file.write(line)

if __name__ == "__main__":
    # Get user input for the username to be deleted
    username_to_delete = input("Enter username to delete: ")

    # Define the path to the password file
    passwd_file = "passwd.txt"

    # Call the delete_user function
    delete_user(username_to_delete, passwd_file)

    # Print a message indicating that the user has been deleted
    print("User Deleted.")
