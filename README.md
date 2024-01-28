# FOCP_Final_submission
#TASK-1
This python program defines a pizza price calculator where the user inputs the number of pizzas, delivery preference, whether it's Tuesday, and if ordered via an app, then calculates and displays the total price considering discounts and delivery costs. The program uses functions for input validation and discount calculations.

*output example:*
BPP Pizza Price Calculator
==============
How many pizzas ordered? 9
Is delivery required? (Y/N) Y
Is it Tuesday? (Y/N) T
Please answer "Y" or "N".
Is it Tuesday? (Y/N) Y
Did the customer use the app? (Y/N) N
Total price: £54.00

#Task 2
The code defines a function analyze_log to read and analyze a log file containing entries for cat visits, specifically focusing on a cat named 'OURS.' It calculates statistics such as the total number of correct entries, the number of times other cats were sprayed with water, total time inside, average visit duration, and durations of the longest and shortest visits by the correct cat. The script takes the log file path as a command-line argument and prints the analysis result.

*output example*
Log File Analysis
--------------------
Total number of times the correct cat has entered the house is: 11        
Number of times cats were doused with water: 45
Total time spent in the house by the correct cat: 5.00 hours
Average duration of each visit by the correct cat: 27.27 minutes
Duration of the longest visit by the correct cat: 45 minutes
Duration of the shortest visit by the correct cat: 10 minutes

#Task 3 
Task 3 folder contains 4 python programs
*1)adduser.py*

      The code defines a function add_user that prompts the user for a new username, real name, and password, then appends an encrypted user entry to a password 
      file. It uses ROT-13 for simple encryption and checks for duplicate usernames before adding a new user.

*2)deluser.py*

     The code defines a function delete_user to remove a specified user from a password file by excluding the corresponding line. When executed, the script prompts 
     the user for a username, deletes the user from the "passwd.txt" file, and prints a confirmation message.

*3)login.py*

      The code defines a login function to authenticate users by comparing entered credentials with entries in a password file, printing "Access granted" or 
      "Access denied." When executed, the script prompts the user for a username and password, calls the login function, and outputs the authentication result.

 *4)passwd.py*
 
      The code defines a function change_password to update a user's password in a password file by verifying the specified username and current password. When 
      executed, the script prompts the user for a username, current password, new password, and confirmation, then calls the function to update the password in the 
     "passwd.txt" file and provides feedback on success or mismatched passwords.



