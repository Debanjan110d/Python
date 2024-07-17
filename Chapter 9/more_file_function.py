f =open("file.txt")

# print(f.readlines(),type(f.readlines()))

l1= f.readline()#long method

print(l1)


print(f.readline())
print(f.readline())#shortcut
print(f.readline())
f.close()

