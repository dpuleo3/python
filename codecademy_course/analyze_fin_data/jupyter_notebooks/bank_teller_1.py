balances = {"checking": 0, "savings": 0}

def make_deposit(account_type, amount, balances):
    print("Time to open your account")
    account_type = input("Savings or Checkings?: ")
    print("Perfect!, time to make a deposit")
    amount = input("How much would you like to deposit?: $")
    deposit_status = ""
    if amount > 0:
      if account_type == "savings":
        balances["savings"] += amount
        deposit_status = "successful"
      elif account_type == "checking":
        balances["checking"] += amount
        deposit_status = "successful"
      else:
        deposit_status = acc_error
    else:
      deposit_status = "Unsuccessful, please enter an amount greater than 0"
      deposit_statement = "Deposit of "+ str(amount) + " dollars to your " + account_type + " account was " + deposit_status + "."

make_deposit("checking", 200, balances)
# make_deposit(account_type, amount, balances)
print(balances)

