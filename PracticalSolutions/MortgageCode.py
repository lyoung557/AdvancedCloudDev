def mortgageCheck():
    try:
        requesterAge = int(input("How old are you: "))
        pound_sign = '£'
        if requesterAge >= 18 and requesterAge <=55:
            yearlyIncome = float(input("Please enter your yearly income: "))
            fYearlyIncome = format(yearlyIncome, '.2f')
            print(f'Yearly Income: {pound_sign} {fYearlyIncome}')
            if yearlyIncome >= 18500:
                outstandingDebt = float(input("how much debt do you have: credit cards, car loans etc: "))
                fOutstandingDebt = format(outstandingDebt, '.2f')
                print (f"debt : {pound_sign} {fOutstandingDebt}")
                debtThreshold = (yearlyIncome /20)
                if outstandingDebt > debtThreshold:
                    print("You have too much debt - fix your finances ya scab")
                else:
                   print ("You could qualify for a mortgage! Contact our team on 02895623084")
            else:
                print ("You do not currently earn enough - change jobs, marry rich or start an OF")
        elif requesterAge >=55:
            print("you are going to die soon - we wont lend you money")
        else:
            print ("you are not old enough - grow up")
    except ValueError:
        print("Answer the question properly stupid")

vicTerribleProgram = mortgageCheck()
vicTerribleProgram
