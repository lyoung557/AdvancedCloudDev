"""
Write a program that takes in a user's total income and marital status (single or married), and returns their federal
income tax owed. Use the following tax brackets: for single filers, income up to £9,950 is taxed at 10%; income between
£9,951 and £40,525 is taxed at 12%; income between £40,526 and £86,375 is taxed at 22%; income between £86,376 and
£164,925 is taxed at 24%; income between £164,926 and £209,425 is taxed at 32%; income between £209,426 and £523,600 is
taxed at 35%; income above £523,600 is taxed at 37%. For married filers, the income brackets are doubled.

"""

# This function determine if the user is single or married and return an integer
def maritalStatus():

    status = (input('Are you married ? Answer "yes" or "no": ')).lower()
    while True:
        if status == 'yes' or status == 'y':
            incomeBracketsMultiplier = 2
            break
        elif status == 'no' or status == 'n':
            incomeBracketsMultiplier = 1
            break

        status = (input('Try again. Are you married ? Answer "yes" or "no": ')).lower()

    return incomeBracketsMultiplier


# This function calculate a federal tax owned
def incomeTax(incomeBracketsMultiplier):

    while True:
        try:
            income = int(input('\nWhat is your income: '))
            break
        except ValueError:
            print('Not a number. Try again.')
    if incomeBracketsMultiplier == 1:
        print(f'Your income remains the same £{income}.')
    else:
        income = income * incomeBracketsMultiplier
        print(f'Your income is doubled. It is £{income}.')

    if income <= 9950:
        taxToPay=income * 0.1
    elif income <= 40525:
        taxToPay=income * 0.12
    elif income <= 86375:
        taxToPay=income * 0.22
    elif income <= 164925:
        taxToPay=income * 0.24
    elif income <= 209425:
        taxToPay=income * 0.32
    elif income <= 523600:
        taxToPay=income * 0.35
    else:
        taxToPay=income * 0.37

    return taxToPay

# This function display information about the owned tax.
def taxOwnedProgram():
    print('\n--- CALCULATE YOUR FEDERAL TAX PROGRAM ---\n')
    multiplier = maritalStatus()
    tax= incomeTax(multiplier)
    print(f'\nYou own £{tax} to the Federal Income Office.')

# Run the program
taxOwnedProgram()