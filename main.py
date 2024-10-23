# Programmers: Ethan D'Souza & Andrew Leimbach
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/23/2024
# Lab Assignment: 06
# Problem: Refactor Lab05 Code, using functions.
# Purpose: Understanding functions, reviewing loops, re-using our old knowledge.

# Set variables
INITIAL_BALANCE = 1000
current_balance = INITIAL_BALANCE
SENTINEL = 'E'


def main():

    choice = ''
    while choice != SENTINEL:
        print("Please select an option:")
        print("D - Deposit")
        print("W - Withdraw")
        print("V - View Balance")
        print("E - Exit")

        choice = get_input()

        if choice == 'D':
            deposit()
        elif choice == 'W':
            withdraw()
        elif choice == 'V':
            view_balance()
        elif choice == 'E':
            print("Thank you for using the ATM program. Goodbye!")
        else:
            print("Error: Invalid choice. Please enter D, W, V, or E.")


def get_input():
    while True:
        choice = input("Your choice: ").strip().upper()
        if choice in ['D', 'W', 'V', 'E']:
            break
        else:
            print("Error: Invalid choice. Please enter D, W, V, or E.")
    return choice


def deposit():
    global current_balance
    while True:
        deposit_amount = input("Enter the amount to deposit: ").strip()
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount >= 0:
                current_balance += deposit_amount
                print("Deposit successful! Your new balance is", current_balance)
                break
            else:
                print("Error: Please enter a positive number.")
        else:
            print("Error: Please enter a valid number.")


def withdraw():
    global current_balance
    while True:
        withdraw_amount = input("Enter the amount to withdraw: ").strip()
        if withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
            if withdraw_amount >= 0:
                current_balance -= withdraw_amount
                print("Withdrawal successful! Your new balance is", current_balance)
                if current_balance < 0:
                    apply_negative_fee()
                break
            else:
                print("Error: Please enter a positive number.")
        else:
            print("Error: Please enter a valid number.")


def view_balance():
    print("Your current balance is", current_balance)


def apply_negative_fee():
    global current_balance
    fee = abs(current_balance) * 0.05
    current_balance -= fee
    print("Your balance is negative. A 5% fee of", fee, "has been applied. New balance:", current_balance)


# Start the program
print("Welcome to the ATM program!")
main()
print("ATM program has ended.")

