def count_characters(arg1, arg2):
    input_string = arg1
    input_character = arg2

    number_occurances = input_string.count(input_character)
    return(number_occurances)

users_string = input("What is the text which you would like to search? ").lower()
users_character = input("What character would you like to search for? ").lower()
character_count = count_characters(users_string, users_character)
print("The character '" + str(users_character) + "' appeared in the string " + str(character_count) + " times!")