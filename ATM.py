#Beginning balance
account_balance = float(500.50)

#Define the function print_balance to print the balance
def print_balance():
    print( "Your current balance: $%.2f"%account_balance)

#Define function of deposit to print the deposit amount
def deposit(deposit_amount):
    global account_balance
    account_balance = account_balance + deposit_amount
    print("Deposit was $%.2f, current balance is $%.2f"%(deposit_amount,account_balance))

#Define the function withdraw amount, attach it to withdraw_amount
def withdraw(withdraw_amount):
    global account_balance

#Verify the withdraw_amount is greater than the account_balance, if so, print the following message
    if(withdraw_amount > account_balance):
        print ("withdraw_amount is greater that your account balance of account_balance")
    else:
#Calculate the account_balance and display the withdraw amount and the account balance with the '$' and two decimal points
        account_balance = account_balance - withdraw_amount
        print ("Deposit was $%.2f, current balance is $%.2f"%(withdraw_amount,account_balance))
#Prompt and read the input from the user and execute the decided functions
print ("WELCOME TO ATM")
print ("---------------")
print ("D:Deposit")
print ("W:Withdrawal")
print ("B:Account Balance")
print ("Q:Quit")
summary= ""

#While loop - if there is user input the loop will iterate through the designated if loop.
while(True):
    userchoice = input ("What would you like to do?")
    if (userchoice == 'B'):
        print_balance()
        summary = "\nBeginning Balance: "+str(account_balance)
    if (userchoice == 'D'):
        deposit_amount=float(input("How much would you like to deposit today?"))
        deposit(deposit_amount)
        summary += "\nDeposit Amount: "+str(deposit_amount)
    if (userchoice == 'W'):
        withdraw_amount=float(input("How much would you like to withdraw?"))
        withdraw(withdraw_amount)
        summary += "\nWithdraw Amount: "+str(withdraw_amount)
    if (userchoice == 'Q'):
        print(summary)
        print ("\nThank you for banking with us.")
        break

