with open("log.txt") as f:
    content=f.read()


with open("this.txt","w") as f:
    f.write(content)

