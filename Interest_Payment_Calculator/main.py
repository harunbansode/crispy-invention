def main():
    print('Monthly Interest Calculator')
    print("")

    principal = int(input('Enter the principle: '))
    APR = float(input('Enter the Annual Interest Rate: '))
    year = int(input('Enter the year: '))

    monthly_interest_rate = APR / 1200
    amount_of_months = year * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (- amount_of_months))

    print(f'The monthly payment for this loan is: {monthly_payment}')


if __name__ == '__main__':
    main()
