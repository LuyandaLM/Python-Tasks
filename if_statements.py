price = 100
if price < 100:
    print("Buy the chair!")

if price < 100:
    print("Buy the chair!")
else:
    print("Don't buy the chair")

if price < 100:
    print("Buy the chair!")
elif price == 100:
    print("You can buy it if you really want...")
else:
    print("Don't buy the chair!")


def age_program():
    seconds_or_years = input("Give me seconds (s) or years (y)? ")
    if seconds_or_years == "s":
        # Convert seconds to years
        user_value = input("Enter the number of seconds you've lived for: ")
        print("You've lived for {} years.".format(int(user_value) / 60 / 60 / 24 / 365))
    elif seconds_or_years == "y":
        # Convert years to seconds
        user_value = input("Enter the number of years you've lived for: ")
        print("You've lived for {} seconds".format(int(user_value) * 365 * 24 * 60 * 60))


age_program()
