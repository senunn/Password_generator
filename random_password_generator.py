import random
import string



character_string = list(string.ascii_letters)
symbol_list = [chr(i) for i in range(33,48)]
number_list = [chr(i) for i in range(48,58)]
character_count= int(input("How many characters do you want in your password: "))
symbol_count = int(input("How many symbols do you want in your password: "))
number_count = int(input("How many numbers do you want in your password: "))



def random_elements(list1, num):
    random_elem_list = random.sample(list1,num)
    return random_elem_list


def randomizestring(input_string):
    new_list = list(input_string)
    random.shuffle(new_list)
    new_name = ''.join(new_list)
    return new_name

password_chars = random_elements(character_string,character_count)
symbol_chars = random_elements(symbol_list,symbol_count)
number_chars = random_elements(number_list,number_count)


passing_string = ''.join(password_chars+symbol_chars+number_chars)
print(passing_string)
print(randomizestring(passing_string))
