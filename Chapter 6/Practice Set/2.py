marks1 = int(input("Enter Your Marks : "))
marks2 = int(input("Enter Your Marks : "))
marks3 = int(input("Enter Your Marks : "))

total_percentage=((marks1+marks2+marks3)/300)*100
marks1_percentage=(marks1/100)*100
marks2_percentage=(marks2/100)*100
marks3_percentage=(marks3/100)*100


print("your marks1 Percentage : ",marks1_percentage)
print("your marks2 Percentage : ",marks2_percentage)
print("your marks3 Percentage : ",marks3_percentage)


print("your total Percentage : ",total_percentage)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3 >=33):
    print("You passed")
else:
    print("You failed")