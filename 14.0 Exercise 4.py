#Imagine the price of a house is $1M
#                 If the buyer has good credit
#                              They need to put down 10%
#                 Otherwise
#                                  they need to put down 20%
# write down a program to display a buyer with good credit

price = 1000000
has_good_credit = True
if has_good_credit :
    down_payment = 0.1*price
else :
    down_payment = 0.2*price
print(f"Down payment : ${down_payment}")
