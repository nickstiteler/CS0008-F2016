
budg = float(input('Enter the amount that you have budgeted'))
num = int(input('Enter the number of expenses you have'))
while num>0:
    exp = float(input('enter the cost of your expense'))
    budg = budg-exp
    num = num-1
if(budg>0):
    print(budg,'dollars under budget')
elif(budg==0):
    print(budg,'You were exactly on budget')
else:
    budg=-budg
    print(budg,'dollars over budget')