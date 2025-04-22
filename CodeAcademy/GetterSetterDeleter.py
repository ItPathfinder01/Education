# # Task 1
#
# class Box:
#     def __init__(self, weight):
#         self.__weight = weight
#
#     def getWeight(self):
#         return self.__weight
#
#     def setWeight(self, weight):
#         if weight >= 0:
#             self.__weight = weight
#
#     def delWeight(self):
#         del self.__weight
#
#     weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")
#
#
# box = Box(11)
#
# box.setWeight(13)
# print(box.weight)

# Task 2

# class Identificator:
#     def __init__(self, ID):
#         self.ID = ID
#
#     def setID(self, ID):
#         return f"Now your ID is {ID}."
#
#
# class NewID(Identificator):
#     def __init__(self, ID):
#         super().__init__(ID)
#
#     def updateID(self, newID):
#         self.ID = newID
#         return f"Your ID is updated to {newID}."
#
#
# iden = Identificator(1)
# print(iden.setID(3))
# iden2 = NewID(0)
# print(iden2.updateID(4))
#
#
class Identificator:
    def __init__(self, ID):
        self.ID = ID

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return f"Your ID is {self.ID}."


class NewID(Identificator):
    def __init__(self, ID):
        super().__init__(ID)

    def updateID(self, newID):
        rek = newID + 1
        self.setID(rek)
        return f"Your ID is updated to {rek}."


iden = Identificator(1)
iden.setID(3)
print(iden.getID())

iden2 = NewID(1)
print(iden2.updateID(4))