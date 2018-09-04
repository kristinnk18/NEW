balance = 10
annual_interest_rate = 0.2
monthly_payment_rate =0.04
monthly_interest_rate = annual_interest_rate / 12
monthly_payment = monthly_payment_rate * balance

for month in range(1, 13):
    monthly_payment = monthly_payment_rate * balance
    balance = (balance - monthly_payment) * (1 + monthly_interest_rate)

    print('Month: %d \n Minimum monthly payment: %g \n Remaining balance: %g'\
          % (month, round(monthly_payment, 2), round(balance,2)))