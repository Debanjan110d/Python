a = "0123456789"
# String slicing: extract a subset of characters from the string a
# The syntax is a[start:stop:step], where:
#   start: the starting index (inclusive), default is 0
#   stop: the ending index (exclusive), default is the end of the string
#   step: the increment between indices, default is 1
print(a[1:8:3])  # Output: "147"
# Here, start=1, stop=8, and step=3, so we get every 3rd character starting from index 1