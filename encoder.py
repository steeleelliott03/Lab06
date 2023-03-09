# Steele Elliott
# Lab 06
# Software Engineering

def encode(password):
    new = ''
    for i in range(0, len(password)):
        new = chr(int(password[i]) + 3)
    return password


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
            print('Your password has been encoded and stored!')
        elif choice == 2:
            print(f'The encoded password is {encoded} and your decoded password is {password}.')



if __name__ == '__main__':
    main()
