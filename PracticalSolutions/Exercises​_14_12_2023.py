import random

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find the sum of all numbers based on user input
def sum_of_numbers():
    total_sum = 0
    upper_limit = int(input("Enter a number: "))

    # Calculate the sum of numbers from 1 to the entered number
    for i in range(1, upper_limit + 1):
        total_sum += i

    return total_sum


# Fist Excersise:
result = sum_of_numbers()
print(f"\nThe sum of numbers from 1 to the entered number is: {result}")



# Second Excersise:

# Generate a random list of length 500 containing integers from 125 to 2250
random_list = [random.randint(125, 2250) for _ in range(500)]

# 1 - Find and print all numbers divisible by 5
divisible_by_5 = [num for num in random_list if num % 5 == 0]
print("\nNumbers divisible by 5:")
print(divisible_by_5)

# 2 - Find and print all prime numbers.
prime_numbers = [num for num in random_list if is_prime(num)]
print("\nPrime numbers:")
print(prime_numbers)

# 3 - Find and print all even numbers.
even_numbers = [num for num in random_list if num % 2 == 0]
print("\nEven numbers:")
print(even_numbers)

# 4 - Find and print all numbers divisible by 2 and 10
divisible_by_2_and_10 = [num for num in random_list if num % 2 == 0 and num % 10 == 0]
print("\nNumbers divisible by 2 and 10:")
print(divisible_by_2_and_10)