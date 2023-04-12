# Program to check whether a word passed through a funtion has 'is' in the begining, if not then return it as such else return the word itself


def check_is_there(word):
    if len(word)>2 and word[0:2]=='Is':
        return word
    return "Is" + word


print(check_is_there("Array"))
print(check_is_there("IsNotArray"))