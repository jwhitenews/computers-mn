class Employee:

    def __init__(self, year, make, model, cc, color):
        self.year = year
        self.make = make
        self.model = model
        self.cc = cc
        self.color = color

    def sled_list(self):
        return '{} {}'.format(self.year, self.make)