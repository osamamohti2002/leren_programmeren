import random

NUM1 = random.randint(1, 10)
NUM2= random.randint(5, 15)

number = input('Weet jij wat ' + str(NUM1) + ' + ' + str(NUM2) + ' is? ')
try:
    if int(number) == NUM1 + NUM2:  
        print('Dat is juist')
    else:
        print('Nee dat klopt niet')
except ValueError:
    print('Dat is geen nummer!')
