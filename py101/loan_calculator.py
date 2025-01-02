# These are helper functions

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number < 0:
            raise ValueError(f"Please provide a positive value.")
    except ValueError:
        return True

    return False

# This is the main function

def loan_calculator():
    prompt('Welcome to your loan calculator!')

    while True:
        prompt('--------------------------------')

        # Loan amount
        prompt("What is the loan amount? ")
        loan_amount = input()

        while invalid_number(loan_amount):
            prompt("Please enter a valid number.")
            loan_amount = input()

        loan_amount = float(loan_amount)
        prompt(f'Your loan amount is ${loan_amount:.2f}')

        # Monthly interest rate
        prompt("What is the Annual Percentage Rate (APR)? ('5.5' for 5.5%)")
        annual_percentage_rate = input()

        while invalid_number(annual_percentage_rate):
            prompt("Please enter a valid number.")
            annual_percentage_rate = input()

        annual_percentage_rate = float(annual_percentage_rate)
        prompt(f'Your APR is {annual_percentage_rate:.2f}%')
        
        monthly_interest_rate = (annual_percentage_rate / 100) / 12

        # Loan duration
        prompt("What is the loan duration? ")
        prompt("First enter the number of years...")
        years = input()

        while invalid_number(years):
            prompt("Please enter a valid number.")
            years = input()

        years = float(years)

        prompt("Then enter the number of months...")
        months = input()

        while invalid_number(months):
            prompt("Please enter a valid number.")
            months = input()

        months = float(months)

        loan_duration_in_months = (years * 12) + months

        # Calculate monthly payment
        monthly_payment = loan_amount * (
            monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) **
             (-loan_duration_in_months))
        )

        prompt(f'Your monthly payment is ${monthly_payment:.2f}')


        # Ask if user would like to perform another calculation.
        prompt("Would you like to perform another calculation?")
        prompt("Your options are 'yes' or 'no'. You may type your response without quotation marks.")
        response = input()

        while response not in ['yes', 'no']:
            prompt("Hmm... that doesn't look like a valid operation. Please try again.")
            response = input()

        if response != 'yes':
            break

loan_calculator()
