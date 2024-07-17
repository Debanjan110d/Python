f=open("poem.txt")

content=f.read()

if "twinkle" in content:
    print("yes")
else:
    print("no")

f.close()