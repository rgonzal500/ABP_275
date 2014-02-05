# Trust Fund Buddy - Good
# Demonstrates type conversion

print(
"""
                       Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs.  Since you're rich, ignore pennies
and use only dollar amounts.

"""
)

car = input("Lamborghini Tune-Ups: ")
car = int(car)

rent = int(raw_input("Manhattan Apartment: "))
jet = int(raw_input("Private Jet Rental: "))
gifts = int(raw_input("Gifts: "))
food = int(raw_input("Dining Out: "))
staff = int(raw_input("Staff (butlers, chef, driver, assistant): "))
guru = int(raw_input("Personal Guru and Coach: ") )
games = int(raw_input("Computer Games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total:", total)

raw_input("\n\nPress the enter key to exit.")
