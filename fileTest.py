fo = open("D:\\a.txt","r")
print("Name of the file:", fo.name)
print("Closed or not", fo.close)
print("Open mode", fo.mode)

for line in fo:
    print(line)
fo.close()
