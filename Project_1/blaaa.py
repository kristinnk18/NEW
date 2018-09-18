

balance = input("Input the cost of the item in $: ")
balance = float(balance)
x = 2500
monthly_payment_rate = input("Input the monthly payment in $: ")
monthly_payment_rate = float(monthly_payment_rate)
month = 0
month = int(month)



while balance < x:
    print("The cost of the item: ", balance)
    if balance <= 1000:
        month += 1
        monthly_interest_rate = 0.015
        interest_paid = balance * monthly_interest_rate
        balance = (balance - monthly_payment_rate) + (balance * monthly_interest_rate)
        while balance >= monthly_payment_rate:
            monthly_payment_rate
        else:
            monthly_payment_rate = balance + interest_paid
           
        print("Month: ", month, "Payment: ", round(monthly_payment_rate, 2), "Interest paid: ", round(interest_paid,2), "Remaining debt: ", round(balance,2))
        print("Number of months: ", month)
        break

    else:
        while balance >= monthly_payment_rate:
            month += 1
            monthly_interest_rate = 0.020
            monthly_payment_rate
            interest_paid = balance * monthly_interest_rate
            balance = (balance - monthly_payment_rate) + (balance * monthly_interest_rate)

            print("Month: ", month, "Payment: ", round(monthly_payment_rate, 2), "Interest paid: ", round(interest_paid,2), "Remaining debt: ", round(balance,2))
        else:
            month += 1
            monthly_interest_rate = 0.020
            interest_paid = balance * monthly_interest_rate
            monthly_payment_rate = balance + interest_paid
            balance = (balance - monthly_payment_rate) + (balance * monthly_interest_rate)

            print("Month: ", month, "Payment: ", round(monthly_payment_rate, 2), "Interest PPaid: ", round(interest_paid,2), "Remaining debt: ", round(balance,2))
            break
        