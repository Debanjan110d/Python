with open("log.txt") as f:
    content1=f.read()


with open("this.txt",) as d:
      content2=d.read()

if content1==content2:
     print("This files are identical")
else:
     print("This files are not identical")