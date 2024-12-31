# Simple Banking system

def check(balance):
  print(f"Your available balance is NPR {balance}")

def deposit():
  amount = int(input("Enter the amount to be deposited: "))
  if amount < 0:
    print("The amount cannot be negative")
    return 0
  else:
    print(f"Your have successfully deposited NPR {amount}")
    return amount
    

def withdraw(balance):
  amount = int(input("Enter the amount to be withdrawn: "))
  if amount > balance:
    print("The amount exceeds your balance")
    return 0
  elif amount < 0:
    print("The amount cannot be negative")
    return 0
  else:
    print(f"Your have successfully withdrawn NPR {amount}")
    return amount
  
def main():
  balance = 0

  while True:
    print("\n**********************")
    print("Simple Banking Program")
    print("**********************")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    print("**********************\n")

    cmd = int(input("\nEnter your Command(1-4): "))

    if cmd == 1:
      check(balance)
    elif cmd == 2:
      balance += deposit()
    elif cmd == 3:
      balance -= withdraw(balance)
      check(balance)
    elif cmd == 4:
      break
    else:
      print("Your command is invalid")
  print("Have a great day ! ")

if __name__ == '__main__':
  main()