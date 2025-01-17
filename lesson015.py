number = int(input('Type a number: '))

if number > 3:
    print("The number is greater than 3")
print('-----')

if number > 3:
    print("The number is greater than 3")
else:
    print("The number is not greater than 3")
print('-----')

if number < 1:
    print('Number is less than 1')
elif number < 2:
    print('Number is between 1 an 2')
elif number < 3:
    print('Number is between 2 an 3')
else:
    print('The number is greater than or equal to 3')