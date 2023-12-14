#Write a function that takes in a string and returns the index of the first occurrence of a specific character in the string.
def firstIndexCharacter(input,target):
    try:
        i = input.index(target)
        return i
    except ValueError:
        print('Integer value expected')
        return -1

str1 = "This is my string"
char_to_find = "i"
output = firstIndexCharacter(str1,char_to_find)
print(f'Character {char_to_find} is located at index: {output}')
