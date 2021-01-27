#with applies the close method automatically r(read) attribute is default
with open("files/fruit.txt") as myfile:
    content = myfile.read()
print(content)