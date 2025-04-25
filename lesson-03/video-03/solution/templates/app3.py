#function to calculate monthly payment
def calculate_monthly_payment(principal, annual_interest_rate, years): 
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    return monthly_payment 
