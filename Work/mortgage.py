# mortgage.py
#
# Exercise 1.7
# mortgage.py


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_n = 0
ex_pay_start_m = 60;
ex_pay_end_m = 108;
ex_pay_am = 1000;


while principal > 0:
   
    if month_n >= ex_pay_start_m and month_n <= ex_pay_end_m:
        payment_i = payment + ex_pay_am;
    else:
        payment_i = payment;
    new_princ = principal * (1+rate/12);
    if new_princ < payment_i:
        payment_i = new_princ;
            
        
    principal = new_princ - payment_i;
    total_paid = total_paid + payment_i
    print([principal, total_paid])
    month_n = month_n + 1;
    
    

print('Total paid', total_paid)
print('final year n ', month_n/12)