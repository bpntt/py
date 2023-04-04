def find(orbits):
    orbits = [(a, b) for (a, b) in orbits if a != b]
    space = [a*b for (a, b) in orbits]
    return orbits[space.index(max(space))]


orbits = [(1, 3), (2.5, 10), (6, 6), (7, 3), (4, 3)]
print(find(orbits))
