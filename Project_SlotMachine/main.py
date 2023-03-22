def deposit():
    while True: 
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            # isdigit() tells us if its a valid whole number
            amount = int(amount)
            # now we can convert it to an integer
            if amount > 0: 
                break
            else: 
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")
    
    return amount

def main():
    # this is our program
    # when we run main, we are running the program
    balance = deposit()

main()