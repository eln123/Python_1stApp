MAX_LINES = 3
# a convention in Python,
# is a variables in all caps
# is never changed
# using a variable here makes the whole program
# dynamic, so if you want to change the 
# number you only have to do it once

MAX_BET = 100
MIN_BET = 1



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

def get_number_of_lines():
    while True: 
         lines = input("Enter the number of lines to bet on (1 -" + str(MAX_LINES) + ") ")
         if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
    
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between $" + str(MIN_BET) + " - $" + str(MAX_BET) + ".")
        else: 
            print("Please enter a number")
    return amount

def main():
    # this is our program
    # when we run main, we are running the program
    balance = deposit()
    lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough to bet that amount, your current balance is: $" + str(balance))
        else : print("You are betting $" + str(bet) + " on " + str(lines) + " lines. Total bet is equal to: $" + str(total_bet))

main()