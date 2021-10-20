N = 1
while N <= 5:
    binary_input = input('Enter binary number:\n')
    decimal_number = int(binary_input, 2)
    print(str(N) + ': ' + str(decimal_number))

    N += 1

print('Calculations limit reached')
