inches = [9,5.5,6,4,5,6.5,10]
cms = [inch * 2.54 for inch in inches if inch > 5]
print(cms)