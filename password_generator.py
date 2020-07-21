import string
import random

def generate_ascii_characters_list():
    chr_lst = list(string.printable)[:-6]
    return chr_lst

def create_random_passwd(amnt_of_char):
    lst_of_chars = generate_ascii_characters_list()
    return ''.join(random.choice(lst_of_chars) for _ in range(amnt_of_char))

print(create_random_passwd(int(input('Provide length of the new password: '))))
