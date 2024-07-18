with open("log.txt") as f:
    content = f.readlines()

for i, line in enumerate(content, start=1):
    if "python" in line:
        print(f"The word 'python' is situated in line {i}")
        break
else:
    print("The word 'python' is not found in the file")