#1. Föst greiðsla er alltaf í mesta lagi $50 á mánuði sem skiptist í afborganir af höfuðstól og vexti.

#2. Leyfið notandanum að slá inn höfuðstól lánsins (í $). Þið megið þó gera ráð fyrir því að notandinn slái alltaf 
#   inn upphæð sem er < $2500.

#3.  Hafið vaxtaprósentuna breytilega þannig að ef heildarupphæð lánsins er ≤ $1000 þá er vaxtaprósentan 1,5% á mánuði, 
#    annars 2,0% á mánuði. Athugið þó að vaxtaprósentan er föst yfir lánstímann.

#4.  Fyrir sérhverja greiðslu skrifar forritið út númer mánaðar, heildargreiðslu og vaxtagreiðslu fyrir viðkomandi mánuð
#    og eftirstöðvar lánsins.

#5.  Skrifið allar rauntölur út með í mesta lagi tveimur aukastöfum. Þið eigið að nota innbyggða Python fallið round() til þess.

#  Input the cost of the item in $: 500
#  Month: 1 Payment: 50.0 Interest paid: 7.5 Remaining debt: 457.5 
#  Month: 2 Payment: 50.0 Interest paid: 6.86 Remaining debt: 414.36 
#  Month: 3 Payment: 50.0 Interest paid: 6.22 Remaining debt: 370.58  
#  Month: 4 Payment: 50.0 Interest paid: 5.56 Remaining debt: 326.14 
#  Month: 5 Payment: 50.0 Interest paid: 4.89 Remaining debt: 281.03  
#  Month: 6 Payment: 50.0 Interest paid: 4.22 Remaining debt: 235.24 
#  Month: 7 Payment: 50.0 Interest paid: 3.53 Remaining debt: 188.77 
#  Month: 8 Payment: 50.0 Interest paid: 2.83 Remaining debt: 141.6 
#  Month: 9 Payment: 50.0 Interest paid: 2.12 Remaining debt: 93.73 
#  Month: 10 Payment: 50.0 Interest paid: 1.41 Remaining debt: 45.13 
#  Month: 11 Payment: 45.81 Interest paid: 0.68 Remaining debt: 0.0
#  Number of months: 11 Total interest paid: 45.81

balance = 4213
annual_interest_rate = 0.2
monthly_payment_rate =0.04
monthly_interest_rate = annual_interest_rate / 12
monthly_payment = monthly_payment_rate * balance

for month in range(1, 13):
    monthly_payment = monthly_payment_rate * balance
    balance = (balance - monthly_payment) * (1 + monthly_interest_rate)

    print('Month: %d \n Minimum monthly payment: %g \n Remaining balance: %g'\
          % (month, round(monthly_payment, 2), round(balance,2)))


          debt = 500
interest_rate = 0.015
monthly_payment = 50
interest_paid = debt * interest_rate



for month in range(1, 13):
    monthly_payment
    interest_paid = 
    debt_left = (debt - monthly_payment) * (1 + interest_paid)


    print("Month: ", month, "Payment: ", round(monthly_payment, 2), "Interest paid: ", interest_paid, "Remaining debt: ", round(debt_left, 2))