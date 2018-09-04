

debt = input("Input the cost of the item in $: ")
debt = int(debt)
x = 2500
payment = 50
payment = float(payment)
month = 0
month = int(month)
total_interest_paid = 0



while debt < x:
    print("The cost of the item: ", debt)
    if debt <= 1000:

        while debt >= payment:
            month += 1
            monthly_interest_rate = 0.015
            payment
            interest_paid = debt * monthly_interest_rate
            debt = (debt - payment) + (debt * monthly_interest_rate)
            new_total = total_interest_paid + interest_paid
        


            print("Month: ", month, "Payment: ", round(payment, 2), "Interest paid: ", round(interest_paid,2), "Remaining debt: ", round(debt,2))
            total_interest_paid = total_interest_paid + interest_paid


        else:
            month += 1
            monthly_interest_rate = 0.015
            interest_paid = debt * monthly_interest_rate
            payment = debt + interest_paid
            debt = (debt - payment) + (debt * monthly_interest_rate)
            new_total = total_interest_paid + interest_paid
           
            print("Month: ", month, "Payment: ", round(payment, 2), "Interest paid: ", round(interest_paid,2), "Remaining debt: ", round(debt,2), "\n\nNumber of months: ", month, "\nTotal interest paid: ", round(new_total,2))

            break

    else:
        while debt >= payment:
            month += 1
            monthly_interest_rate = 0.020
            payment
            interest_paid = debt * monthly_interest_rate
            debt = (debt - payment) + (debt * monthly_interest_rate)
            new_total = total_interest_paid + interest_paid
        


            print("Month: ", month, "Payment: ", round(payment, 2), "Interest paid: ", round(interest_paid,2), "Remaining debt: ", round(debt,2))
            total_interest_paid = total_interest_paid + interest_paid


        else:
            month += 1
            monthly_interest_rate = 0.020
            interest_paid = debt * monthly_interest_rate
            payment = debt + interest_paid
            debt = (debt - payment) + (debt * monthly_interest_rate)
            new_total = total_interest_paid + interest_paid
           
            print("Month: ", month, "Payment: ", round(payment, 2), "Interest paid: ", round(interest_paid,2), "Remaining debt: ", round(debt,2), "\n\nNumber of months: ", month, "\nTotal interest paid: ", round(new_total,2))
            break
        