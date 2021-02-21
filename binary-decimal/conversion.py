n = 1
while n <= 5:
    binary_input = input('Enter binary number:\n')
    decimal_number = int(binary_input, 2)
    print(str(n) + ': ' + str(decimal_number))

    n += 1

print('Calculations limit reached')