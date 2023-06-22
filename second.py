def format_currency(amount):
    return '₹ ' + format(amount, ',.0f')

def print_loan_details(principal, tenure, interest_rate):
    balance = principal
    loan_paid_to_date = 0
    number_of_months=tenure*12
    interest_rate = interest_rate / 100
    
    # Output header
    print('Year\tPrincipal (A)\tInterest (B)\tTotal Payment (A + B)\tBalance\t\tLoan Paid To Date')
    
    # Calculate and print EMIs for each month
    for month in range(tenure * 12 + 1):
        if month == 0:
            final_interest=20003
            output = '2023\t' + format_currency(principal) + '\t' + format_currency(final_interest) + '\t' + format_currency(principal+final_interest) + '\t\t' + format_currency(0) + '\t\t100.00%'
        else:
            R=interest_rate/number_of_months
            sch_pay=10000

            interest = balance*(interest_rate/number_of_months)
            principal_paid = sch_pay - interest
            balance -= principal_paid
            loan_paid_to_date += principal_paid
            
            output = get_month_name(month) + '\t' + format_currency(principal_paid) + '\t\t' + format_currency(interest) + '\t\t' + format_currency(sch_pay) + '\t\t' + format_currency(balance) + '\t' + format(loan_paid_to_date / principal * 100, '.2f') + '%'
        
        print(output)

def get_month_name(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months[(month - 1) % 12]

# If you want to get user input
# principal = float(input('Enter principal amount: '))
# tenure = int(input('Enter tenure in years: '))
# interest_rate = float(input('Enter interest rate in percentage: '))
# print_loan_details(principal, tenure, interest_rate)

# Print the loan details
print_loan_details(100000, 1, 35.08)
