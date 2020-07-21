import string
import random

def generate_random_password(amnt_of_char):
    print(''.join(random.choice(string.printable) for _ in range(amnt_of_char)))

generate_random_password(int(input('Provide length of the new password:')))


