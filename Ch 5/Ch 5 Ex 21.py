# ROCK, PAPER, SCISSORS

import random
cpu_num = random.randint(1,3)
num = (input('Enter "rock", "paper", or "scissors"'))
while not(num=='rock' or num=='scissors' or num=='paper'):
    print('Enter rock, paper, or scissors')
if(cpu_num==1):
    print('rock')
elif(cpu_num==2):
    print('paper')
else:
    print('scissors')
if(cpu_num==1 and num=='rock'):
    print('Tie')
elif(cpu_num==1 and num=='scissors'):
    print('CPU wins! Rock beats scissors.')
elif(cpu_num==1 and num=='paper'):
    print('You win! Paper beats rock.')
elif(cpu_num==2 and num=='rock'):
    print('You win! Rock beats scissors.')
elif(cpu_num==2 and num=='scissors'):
    print('Tie')
elif(cpu_num==2 and num=='paper'):
    print('CPU wins! Scissors beats paper')
elif(cpu_num==3 and num=='rock'):
    print('CPU wins! Paper beats rock.')
elif(cpu_num==3 and num=='scissors'):
    print('You win! Scissors beats paper.')
else:
    print('Tie')
