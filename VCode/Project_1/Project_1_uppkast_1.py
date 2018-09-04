

balance = input("Input the cost of the item in $: ")
balance = float(balance)
x = 2500
monthly_payment_rate = input("Input the monthly payment in $: ")
monthly_payment_rate = float(monthly_payment_rate)
monthly_payment = monthly_payment_rate



while balance < x:
    if balance <= 1000:
        for month in range(1, 13):
            monthly_interest_rate = 0.015
            monthly_payment = monthly_payment_rate
            interest_paid = balance * monthly_interest_rate
            balance = (balance - monthly_payment) + (balance * monthly_interest_rate)
        

            if balance <= 50:
                monthly_interest_rate = 0.015
                monthly_payment = balance
                interest_paid = balance * monthly_interest_rate
                balance = (balance - monthly_payment)
                
                
            print("Month: ", month, "Payment: ", round(monthly_payment, 2), "Interest paid: ", round(interest_paid,2), "Remaining debt: ", round(balance,2))
        break
    else:
        for month in range(1, 13):
            monthly_interest_rate = 0.02
            monthly_payment = monthly_payment_rate
            interest_paid = balance * monthly_interest_rate
            balance = (balance - monthly_payment) + (balance * monthly_interest_rate)

            print("Month: ", month, "payment: ", round(monthly_payment, 2), "Interest paid: ", round(interest_paid,2), "Remaining balance: ", round(balance,2))
        break
        