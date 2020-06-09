# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_n = 0


while principal > 0:
    if month_n < 13:
        payment_i = payment + 1000;
    else:
        paymenti = payment;
        
    principal = principal * (1+rate/12) - payment_i;
    total_paid = total_paid + payment
    month_n = month_n + 1;

print('Total paid', total_paid)
print('final year n ', month_n/12)