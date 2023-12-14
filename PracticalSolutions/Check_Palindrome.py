# Checks if the input is a Palindrome
# Returns Boolean if it is or is not a Palindrome.
def is_palindrome(input):
    # Compare the string with its reverse
    return str(input) == str(input[::-1])
    if result:
      return true
    else:
      return false


if(is_palindrome(input("Please Enter a Palindrome: "))):
  print("Is A palindrome")
else:
  print("Is Not A Palindrome")
