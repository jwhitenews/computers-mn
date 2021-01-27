def charcount(char, path):
    file = open(path)
    content = file.read()
    return content.count(char)