#Import libraries
import random

#Display menu
print("Exercises - 21.12.23 - Steven Guiney")
print("1. Program One")
print("2. Program Two")
print("3. Exit")
choice = input("Please select a menu option: (1,2 or 3): ")

#Enter Program One
if choice == '1':
    
    numchoice = int(input("Enter a number to get a sum of all numbers from 1 to the supplied value:"))
    result = sum(range(1,numchoice+1))
    print (f"The sum of all numbers from 1 to {numchoice} is: {result}")

#Enter Program Two
elif choice == '2':

    #Create list of random numbers
    random_list = [random.randint(125, 2250) for _ in range(500)]

    #Offer to print raw list at this stage
    choice2 = input("Created Random List of 500 numbers between 125 and 2250, do you want to print it?")
    if(choice2.lower() == "y"):
        print(random_list)
    elif(choice2.lower() == "n"):
        print('List will not be printed')
    else:
        print('Invalid choice, enter y of n. List will not be printed')
    
    #Print numbers divisible by 5
    print("Numbers divisible by 5:")
    for num in random_list:
      if num % 5 == 0:
           print(f" {num},",end="")

    #Print prime numbers in list
    print("")
    prime_numbers = [num for num in random_list if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    print("Prime numbers:")
    print(prime_numbers)
    
    #Print numbers divisible by 2 and 10
    print("Numbers divisible by 2 AND 10:")
    for num in random_list:
      if num % 2 == 0 and num % 10 == 0:
           print(f" {num},",end="",flush=True) 
elif choice == '3':
    exit(0)
else:
    print("Invalid choice. Please enter 1 or 2.")
    #error.raise()
