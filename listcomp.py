temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

def foo(st):
    return [i if type(i) == int else 0 for i in st]

def foo(st):
    return sum([float(i) for i in st])