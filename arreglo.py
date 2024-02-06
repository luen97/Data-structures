import random


class Array:
    # Aquí forzamos a que la creación del array tenga
    # solo un tipo de dato, pero si nos damos cuenta
    # podríamos meter allí lo que quisieramos pues
    # a fin de cunetas es una lista
    
    def __init__(self, capacity, fill_value):
        self.items = list() # same as = []
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self,index, value):
        self.items[index] = value

    def random_fill(self, lower, upper):
        for i in range(len(self.items)):
            self.items[i] = random.randint(lower, upper)

    def sum(self):
        acumulado = 0

        for value in self.items:
            acumulado += value
        return acumulado