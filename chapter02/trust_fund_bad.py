# Trust Fund Buddy - Bad
# Demonstrates a logical error

print(
"""
            Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs.  Since you're rich, ignore pennies
and use only dollar amounts.

"""
)

car =  raw_input("Lamborghini Tune-Ups: ")
rent = raw_input("Manhattan Apartment: ")
jet = raw_input("Private Jet Rental: ")
gifts = raw_input("Gifts: ")
food = raw_input("Dining Out: ")
staff = raw_input("Staff (butlers, chef, driver, assistant): ")
guru = raw_input("Personal Guru and Coach: ")
games = raw_input("Computer Games: ")

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total:", total)

input("\n\nPress the enter key to exit.")

