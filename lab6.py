def password_encoder(password):
    password = list(password)
    for i in range(len(password)):
        password[i] = int(password[i])
        password[i] += 3
        password[i] = str(password[i])

    password = ''.join(password)
    return password


def password_decoder(password):
    password = list(password)
    for i in range(len(password)):
        password[i] = int(password[i])
        password[i] -= 3
        password[i] = str(password[i])

    password = ''.join(password)
    return password


while True:
    print('''Menu  
------------- 
1. Encode  
2. Decode  
3. Quit ''')
    menu_selection = input('Please enter an option: ')
    if menu_selection == '1':
        password_1 = password_encoder(input('Please enter your password to encode: '))
        print('Your password has been encoded and stored!')
    if menu_selection == '2':
        password_2 = password_decoder(password_1)
        print(f'The encoded password is {password_1}, and the original password is {password_2}')
    if menu_selection == '3':
        break
