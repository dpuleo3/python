# Empty set
a = set()

# Add elements to the set
a.add(1)
a.add(2)
a.add(3)
a.add(4)
# elements do not appear twice in a set
print(a)

a.remove(1) # delets the element 1 off the set
print(a)

# Print the numer of elements in the set
print(f"The set has {len(a)} elements")