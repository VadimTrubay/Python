import random
import string

len_password = int(input('give me password length>: '))

password = ''
char_count = len_password // 4
rest_char = len_password % 4
all_symbol = string.ascii_letters + string.digits + string.punctuation
consisten_password = ''

for symbol in string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation:
    if char_count > len(symbol):
        consisten_password += ''.join(random.choices(symbol, k=char_count))
    else:
        consisten_password += ''.join(random.sample(symbol, k=char_count))
consisten_password += ''.join(random.choices(all_symbol, k=char_count))

for _ in range(len_password):
    random_character = random.sample(consisten_password, k=1)[0]
    password += random_character
    consisten_password = consisten_password.replace(random_character, '', 1)
print(f'Your password>: {password}')

