# Task 1

class Box:
    def __init__(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        if weight >= 0:
            self.__weight = weight

    def delWeight(self):
        del self.__weight

    weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")


box = Box(10)
print(box.weight)