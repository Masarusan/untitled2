f= open("kakugen.txt","r",encoding="utf_8")

for i,line in enumerate(f):
    print("{:4d}:{}".format(i + 1,line.rstrip("\n")))

f.close()