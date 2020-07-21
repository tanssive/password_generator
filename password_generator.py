import string
import random

def generate_ascii_characters_list():
    characters = list(string.printable)
    chr_lst = characters[:len(characters)-6]
    return chr_lst

def create_random_passwd(amnt_of_char):
    lst_of_chars = generate_ascii_characters_list()

    return ''.join(random.choice(lst_of_chars) for _ in range(amnt_of_char))

specified_len = int(input('Provide length of the new password: '))

print(create_random_passwd(specified_len))