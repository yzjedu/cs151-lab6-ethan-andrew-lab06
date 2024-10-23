1. Set Variables:
- Set INITIAL_BALANCE to 1000. 
- Set current_balance to INITIAL_BALANCE. 
- Set SENTINEL to 'E' for exiting the loop.


2. Start the ATM Program:
- Output a welcome message explaining the purpose of the program.


3. Main (main_menu function):
- Enter a loop that continues until the user selects 'E' to exit:
- Display the menu options:
  - D - Deposit 
  - W - Withdraw 
  - V - View Balance 
  - E - Exit
- Prompt the user to select an option using get_valid_option():
  If the user selects 'D', call the deposit() function.
  If the user selects 'W', call the withdraw() function.
  If the user selects 'V', call the view_balance() function.
  If the user selects 'E', print a message and exit.


4. Validate Menu Input (get_input function):
- Continuously prompt the user to select one of the valid menu options (D, W, V, or E). 
- If the input is invalid, display an error message and re-prompt until a valid input is received. 
- Return the valid menu option.


5. Deposit Function (deposit function):
- Prompt the user to enter an amount to deposit using input_validation(). 
- Validate that the deposit amount is a positive integer:
- If valid, add the amount to current_balance. 
- Display the updated balance. 
- If invalid, re-prompt the user until valid input is received.


6. Withdraw Function (withdraw function):
- Prompt the user to enter an amount to withdraw using input_validation(). 
- Validate that the withdrawal amount is a positive integer:
- If valid, subtract the amount from current_balance. 
- Display the updated balance. 
- If the current_balance becomes negative:
- Call the apply_negative_fee() function to charge a 5% fee. 
- If invalid, re-prompt the user until valid input is received.


7. View Balance Function (view_balance function):
- Display the current balance to the user.


8. Apply Negative Fee Function (apply_negative_fee function):
- If the balance is negative, calculate 5% of the absolute value of current_balance as the fee. 
- Deduct the fee from current_balance. 
- Display a warning message about the negative balance and the fee applied.


9. Input Validation Function (input_validation function):
- Prompt the user for input (e.g., deposit or withdrawal amount). 
- Continuously check if the input is a valid, non-negative integer. 
- If invalid (non-numeric or negative), display an error message and re-prompt until a valid input is received. 
- Return the valid input.


10. End the ATM Program:
- After the user selects 'E' to exit, output a final message indicating the ATM program has ended.
