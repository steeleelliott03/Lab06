# Steele Elliott
# Lab 06
# Software Engineering

def encode(password):
    new_password = []
    for i in range(0, len(password)):
        new_password.append(str(int(password[i]) + 3))

    new_password = ''.join(new_password)
    return new_password


def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            encoded = encode(password)
            print('Your password has been encoded and stored!\n')
        elif choice == 2:
            print(f'The encoded password is {encoded} and your decoded password is {password}.\n')
  
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


if __name__ == '__main__':
    main()
    
# This has been edited succesfully
