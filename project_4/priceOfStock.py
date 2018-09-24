

def function_shares():
    while True:
        try:
            shares = int(input("Enter number of shares: "))
            break
        except ValueError:
            print("Invalid number!")
    return shares


def function_price():
    while True:
        try: 
            dollars, numerator, dominator = [int(x) for x in input("Enter price (dollars, numerator, denominator): ").split()]
            value = shares * (dollars+(numerator/dominator))
            value = float(value)
            # print(shares, "shares with market price", dollars, numerator,"/", dominator, "have value: $",round(value,2))
            print("{} shares with market price {} {}/{} have value ${:.2f}".format(shares, dollars, numerator, dominator, value))
            break
        except ValueError:
            print("Invalid price!")
    return value, dollars, numerator, dominator

def cont():
    while True:
        cont = input("Continue: ")
        if cont == "n":
            quit = False
            break
        elif cont == "y":
            quit = True
            break
    return quit


while True:

    shares = function_shares()
    function_price()
    quit = cont()

    if quit == False:
        break
    else:
        continue

    