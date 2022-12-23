enter_password = input('dive me your password>: ')
digit = False
upper = False
lower = False
spec = False

if enter_password == '1234' or enter_password == 'qwerty' or enter_password == 'admin' or enter_password == '':
    print('Password complexity is 1')
    exit()

for char in enter_password:
    if char.isdigit():
        digit = True
    elif char.isupper():
        upper = True
    elif char.islower():
        lower = True
    else:
        spec = True

correct_length = len(enter_password) > 8
result = digit + upper + lower + spec

if result == 1:
    print('Password complexity is 2')
elif result == 2:
    print('Password complexity is 3')
elif result == 3 and not correct_length:
    print('Password complexity is 4')
elif result == 4 and correct_length:
    print('Password complexity is 5')
