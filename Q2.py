decimal = int(input('Enter decimal number: '))
numberAtBinary = []
while decimal > 0:
    b = decimal % 2
    decimal = int(decimal / 2)

    numberAtBinary.append(b)

numberAtBinary.reverse()
print(numberAtBinary)