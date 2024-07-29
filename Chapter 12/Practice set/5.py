n =int(input("Enter number : "))

table = [n*i for i in range(1,11)]
with open("tables.txt","a") as f: # " a " is used to append it continusly
    f.write(f"Table of {n} : {str(table)} \n\n")