cal = 42
minutes = 0
for min in range(5,30,5):
    cal = cal+(4.2*minutes)
    print('calories burned after',min,'minutes is',cal)
    minutes = minutes+5