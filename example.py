
from is_prime import is_prime

num = int(input('Enter Number: '))

if num > 1000000:
    print('number is greter than 1000000')
elif num == 1:
    print('not prime')
else:
    print(is_prime(num))
