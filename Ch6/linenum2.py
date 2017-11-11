f = open("Sample.txt","r",encoding="utf_8")
lines = f.readline()

for i,line in enumerate(lines):
    print("{:4d}:{}".format(i + 1 ,line) ,end = "")
#改行しないend=""
f.close()