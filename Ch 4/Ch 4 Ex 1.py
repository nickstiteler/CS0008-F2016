
rt = 0
days = 5
while days>0:
    nb = int(input("enter number of bugs"))
    if nb<0:
        print("enter a positive integer")
        exit
    rt = rt+nb
    days = days-1
print('Total number of bugs is',rt)


