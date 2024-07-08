name=input("What is your name?")
para =  f''' Dear {name} 
              You are selected
              Date of joining 
                Regards
              '''
print( para )
print(para.replace("Date of joining","19.04.2025").replace("Regards","Best Of Luck"))
