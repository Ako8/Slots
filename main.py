import random

MAX_BET = 100
MIN_BET = 1
MAX_LINES = 3

ROW = 3
COL = 3

slot_symbols = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def spin_slots(row, col, symbols):
    symbol_list = []
    for symbol, value in symbols.items():
        for _ in range(value):
            symbol_list.append(symbol)
    columns = []
    for _ in range(col):
        column = []
        new_slot = symbol_list[:]
        for _ in range(row):
            sam = random.choice(new_slot)
            new_slot.remove(sam)
            column.append(sam)
        columns.append(column)
    return columns


def deposit():
    while True:
        dep = input("What would you like to Deposit? $")
        if dep.isdigit():
            if int(dep) > 0:
                break
            else:
                print("Deposit can't be 0.")
        else:
            print("Deposit must be digit.")
    return dep


def get_bet():
    while True:
        bet = input("What would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet should be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Bet should be digit.")
    return bet


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on between 1-{MAX_LINES}.")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines should be between 1-{MAX_LINES}.")
        else:
            print("Pleas enter digit.")
    return lines


def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row])


def winning_check(columns, bet, lines, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings


def main():
    balance = deposit()
    bet = get_bet()
    line = get_number_of_lines()
    total_bet = bet*line
    print(f"Your toal bet is ${total_bet}")
    slot = spin_slots(ROW, COL, slot_symbols)
    print_slot(slot)
    win = winning_check(slot, bet, line, symbol_value)
    print(f"You won {win}")
    print(f"left: {int(balance)-total_bet+win}")

main()