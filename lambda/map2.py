def to_cm(inch):
    return inch * 2.45
inches = [ 9,5.5,6,4,5,6.5,10]
cms = list(map(to_cm,inches))
print(cms)