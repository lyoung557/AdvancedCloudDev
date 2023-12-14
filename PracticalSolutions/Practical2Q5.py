
def calculate_mortgage_deduction():

     user_session = 0

     while user_session == 0:
        
        valid_input = 0

        while valid_input == 0:
            try:
                annual_salary = float(input("What is the annual salary? (£) "))
                percentage_deduction = float(input("What is the percentage deduction? (%) "))
                valid_input = 1
            except:       
                print("Input must be a number!")
                valid_input = 0


        mortgage_deduction = (annual_salary * percentage_deduction) / 100
        
        print("\t\t\t__________________________________")
        print(f"\t\t\t|The amount deducted is: £ {mortgage_deduction:.2f}")
        print("\t\t\t|_________________________________")
        print("")
               
        valid_exit = 0

        while valid_exit == 0:
            input_repeat = input("Calculate another (yes/no)? ").lower()
            if input_repeat == "no":
                print("Goodbye!")
                valid_exit = 1
                user_session = 1
            elif input_repeat != "yes":
                print("Invalid input. Please enter 'yes' or 'no'.")
                valid_exit = 0
            else:
                valid_exit = 1

calculate_mortgage_deduction()

