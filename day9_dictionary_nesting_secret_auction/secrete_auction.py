from secret_auction_art import logo
from os import system, name as os_name 

print(logo)

bids = {}
bidding_finished = False
# Define the clear function for screen
def clear():
    # for windows
    if os_name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Define the highest bidder function
def get_highest_bidder(bids):
    # show the highest bid
    max = 1
    winner = 'None'
    for akey in bids:
        if bids[akey] > max:
            max = bids[akey]
            winner = akey

    return {"name": winner, "amount": max}

while not bidding_finished:
    name = input("Please enter your name: ")
    price = int(input("Please enter the bid price: $"))
    # Add user inputs into the bid dictionary
    bids[name] = price
    should_continue = input("Is any other user available for bid? Type 'yes' or 'no'\n").lower()
    if should_continue == 'no':
        bidding_finished = True
    elif should_continue == 'yes':
        clear()
else:
    bidder = get_highest_bidder(bids)
    print(f"The auction winner is: {bidder['name']} and the bid amount is: {bidder['amount']}")
# print(bids)