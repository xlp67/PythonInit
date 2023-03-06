import random
import time

a = 0
while a < 10:
    a = random.randint(1, 20)
    print(a, end=' ')
    time.sleep(1)
print('\nO VALOR {} É MAIOR QUE 10!'.format(a))
while a > 10:
    a = random.randint(1, 20)
    print(a, end=' ')
    time.sleep(1)
print('\nO VALOR {} É MENOR QUE 10!'.format(a))
while a != 10:
    a = random.randint(1, 20)
    print(a, end=' ')
    time.sleep(1)
print('\nO VALOR É {}!'.format(a))
