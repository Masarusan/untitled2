def to_cm(inch):
    return inch * 2.54
inches = [9,5.5,6,4,5,6.5,10]
for cm in map(to_cm,inches):
    print(cm)