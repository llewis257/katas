# Complete the method/function so that it converts dash/underscore 
# delimited words into camel casing. 
# The first word within the output should be capitalized only 
# if the original word was capitalized (known as Upper Camel Case, 
# also often referred to as Pascal case).
# Examples

# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
import re
def CamelCase(text):
    ls_text = re.split('-|_', text)
    new_text = ''.join(ls_text[0])
    for word in ls_text[1:]:
        new_text = new_text + word[0].upper() + word[1:]
        #new_text = new_text + word.title() ## for shorter solution, uncomment this and comment previous line
    return new_text

print(CamelCase('the-stealth-warrior'))
print(CamelCase('A-B-C'))
print(CamelCase(''))

    

