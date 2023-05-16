class School:

    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def __repr__(self):
        return (f"A {self.level} school named {self.name} with {self.numberOfStudents} students")

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getStudents(self, newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents
        return newNumberOfStudents


class PrimarySchool(School):
    def __repr__(self):
        parentRepr = super().__repr__()
        return f"{parentRepr} The pickup policy is - {self.pickupPolicy} "

    def __init__(self, name, level, numberOfStudents, pickupPolicy):
        super().__init__(name, 'secondary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy


class HighSchool(School):
    def __init__(self, name, level, numberOfStudents, sportTeams):
        super().__init__(name, "High", numberOfStudents)
        self.sportTeams = sportTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return f"{parentRepr}. Here are our sport teams {self.sportTeams} "

    def getSportTeams(self):
        return self.sportTeams


sport = HighSchool("Harward", "High", 50, ["Manchester", "Arsenal", "Liverpool"])

print(sport)

Primary1 = PrimarySchool("Nasa", "Secondary", 30, "Pickup Allowed")

A1 = School("Class A", "primary", 30)

print(A1)

print(Primary1)