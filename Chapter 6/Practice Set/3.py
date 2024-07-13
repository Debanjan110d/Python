# SPAM COMMMENT DETECTOR

text = input("Enter the text: ")

if (("make a lot of money" in text) and  ("click this" in text) and ("subscribe this" in text)) :
    print("This text is spam")
else:
    print("This text is not spam")
