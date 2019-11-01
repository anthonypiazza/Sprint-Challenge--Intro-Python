# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print(f"\nStarts with D:")
a = [h.name for h in humans if h.name[0] == "D"]
print(f"{a}\n")

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print(f"\nEnds with e:")
b = [h.name for h in humans if h.name[len(h.name)-1] == "e"]
print(f"{b}\n")

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("\nStarts between C and G, inclusive:")
c = [h.name for h in humans if h.name[0] == "C" or h.name[0] == "D" or h.name[0] == "E" or h.name[0] == "F" or h.name[0] == "G"]
print(f"{c}\n")

# Write a list comprehension that creates a list of all the ages plus 10.
print(f"\nAges plus 10:")
d = [h.age + 10 for h in humans]
print(f"{d}\n")

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print(f"\nName hyphen age:")
e = [f"{h.name}-{h.age}" for h in humans]
print(f"{e}\n")

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print(f"\nNames and ages between 27 and 32:")
f = [(h.name, h.age) for h in humans if h.age >= 27 and h.age <= 32]
print(f"{f}\n")

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print(f"\nAll names uppercase:")
g = [Human(h.name.upper(), h.age+5) for h in humans]
print(f"{g}\n")

# Write a list comprehension that contains the square root of all the ages.
print("\nSquare root of ages:")
import math
h = [math.sqrt(h.age) for h in humans]
print(f"{h}\n")
