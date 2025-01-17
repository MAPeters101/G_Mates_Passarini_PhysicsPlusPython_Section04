n = 1

if (n > 3) and (n%2==0):
    print('The number is greater than 3 and even')
elif n > 3:
    print('The number is only greater than 3 but is not even')
elif n%2==0:
    print('The number is not greater than 3 but is even')
else:
    print('The number does not satisfy any conditions')
