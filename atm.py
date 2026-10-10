print ("=================== ATM MANAGEMENT SYSTEM ===================")

#Login functionality
print("Good Morning! Welcome to the VK Bank ATM.")
print("Please insert your card to proceed.")

# User Account
ask_user = input("Do you have an account with us? (yes/no): ").strip().lower()
if ask_user == "yes":
    print("Please proceed to enter your account details.")
else:
    print("Please visit our nearest branch to create an account.")
    print("Thank you for visiting VK Bank ATM. Have a great day!")
    exit()

# Basic ATM functionality
name = input("Enter your name: ")
acc_number = input("Enter your account number: ")

# Pre-defined options for the user
balance = 1000  # Assuming a default balance for demonstration
pin = 1234
real_acc = 9586321470125493

# Checking if the account number is valid
if acc_number != str(real_acc):
    print("Invalid account number. Please try again.")
    exit()

print(f"Hello, {name}! Your account number is {acc_number}.")

# Checking if the PIN is correct
user_pin = int(input("Enter your PIN: "))
if user_pin != pin:
    print("Invalid PIN. Please try again.")
    exit()

# Displaying options for the user
print("\nPlease choose an option:")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

# Taking user input for the chosen option
option = input("Enter the option number (1/2/3/4): ")

# Check Balance functionality
if option == "1":
    print(f"Your current balance is: ${balance}")
    
# Deposit Money functionality
elif option == "2":
    deposit_amount = float(input("Enter the amount to deposit: "))
    if deposit_amount > 0:
        balance += deposit_amount
        print(f"Successfully deposited ${deposit_amount}. New balance is: ${balance}")
    else:
        print("Invalid deposit amount. Please try again.")

# Withdraw Money functionality
elif option == "3":
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    if 0 < withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"Successfully withdrew ${withdraw_amount}. New balance is: ${balance}")
    else:
        print("Invalid withdrawal amount. Please try again.")

# Exit functionality
elif option == "4":
    print("Thank you for using the ATM. Have a great day!")
    exit()

else:
    print("Invalid option. Please try again.")
    
    
