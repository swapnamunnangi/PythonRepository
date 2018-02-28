f= open("guru99.txt","w")
f= open("guru99.txt","r")
f.write("created the file")

for line in f:
    print(line)
f.close()