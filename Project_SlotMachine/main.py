import random

# when you pick a line,
# from 1 - 3, it goes in order from top to bottom
# you can't pick which of the 3 horizontal lines you bet on
# if you hit 2, that means top and middle, 1 means top, 3 means top middle and bottom lines

MAX_LINES = 3
# a convention in Python,
# is a variables in all caps
# is never changed
# using a variable here makes the whole program
# dynamic, so if you want to change the 
# number you only have to do it once

MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# you have 2 A's, 4 B's, 6 C's, 8 D's to choose from


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
  
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    # in this function, we are generating
    # what symbols we will see in each column,
    # based on the frequency of symbols we have 
    # in the symbol_count dictionary 
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # when you use .items(), it gives you
        # the key and value
        # the key is symbol, the value is symbol_count (e.g. A is key, 2 is value)
        for _ in range(symbol_count):
            # the underscore _ is an anonymous variable
            # if you are looping through something
            # and don't care about the count or iteration,
            # you can just use this and you won't have an unused variable
            all_symbols.append(symbol)
            # so we are looping through symbol_count
            # and 
    columns = []
    # we are going to create and append nested lists, which are rows

    # now, for each column we have, we need to generate
    # the number of rows we need
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        # here, we are creating a copy with the slice operator, which is a colon
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    # transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            # this gives you the index and item
            if i  != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



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

def spin(balance):
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

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        print("You won $" + str(winnings) + ".")
        print("You won on lines", *winning_lines)
        # the asterisk * is the splat operator,
        # which passes each line in the winning_lines list,
        # to the print function being run
        return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print("Current balance is $" + str(balance))
        answer = input("Press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)

    print("You left with $" + str(balance))


main()