def login(username, password, passwd_file):
    
     # Open the password file and iterate through its lines
    with open(passwd_file, 'r') as file:
        # Split the line into parts using colon as a separator
        for line in file:
            parts = line.split(":")

            # Check if the current line corresponds to the specified username
            # and if the entered password matches the existing password
            if parts[0] == username and parts[2].strip() == password:
                print("Access granted.")
                return
            
    # If no match is found, print "Access denied."
    print("Access denied.")

if __name__ == "__main__":
    # Get user input for username and password
    username = input("User: ")
    password = input("Password: ")
    passwd_file = "passwd.txt" # Define the path to the password file

    # Call the login function
    login(username, password, passwd_file)