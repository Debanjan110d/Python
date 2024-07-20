class Programmer:
    def __init__(self, name, language, experience):
        self.name = name
        self.language = language
        self.experience = experience


p1 = Programmer("Tim", "Python", 5)
p2 = Programmer("Bill", "Java", 10)
p3 = Programmer("Jill", "C++", 7)
p4 = Programmer("Debanjan","Javascript"," 5 Month")

print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)
print(p4.__dict__)

print(p1.name)
print(p1.language)
print(p1.experience)

print(p2.name)
print(p2.language)
print(p2.experience)

print(p3.name)
print(p3.language)
print(p3.experience)

print(p4.name)
print(p4.language)
print(p4.experience)
