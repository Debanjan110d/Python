marks = {
    "Harry":100,
    "Subham":56,
    "Rohan":23,
    100:"Debanjan"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99})
print(marks)
print(marks.get("Harry"))