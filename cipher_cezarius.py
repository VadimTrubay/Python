import string

alphabet_upper = string.ascii_uppercase
alphabet_lower = string.ascii_lowercase
result_string = ''

while True:
    try:
        text = input('enter your string>: ')
        if text.isnumeric():
            raise ValueError
    except ValueError:
        print(f'is not string, please enter type string')
    else:
        while True:
            try:
                shift = int(input('enter shift>: '))
            except ValueError:
                print(f'is not integer, please enter type integer')
            else:
                for i in text:
                    if i in alphabet_upper:
                        result_string += alphabet_upper[(alphabet_upper.index(i) + shift) % 26]
                    elif i in alphabet_lower:
                        result_string += alphabet_lower[(alphabet_lower.index(i) + shift) % 26]
                    else:
                        result_string += i
                print('=====================')
                print(f'result string: {result_string}')
                break

