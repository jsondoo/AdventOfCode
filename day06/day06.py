import collections

with open('input.txt', 'r') as file:
    data = file.read().split('\n')

planets = collections.defaultdict(set) # map string to list of strings

for orbit in data:
    n1, n2 = orbit.split(')')
    planets[n1].add(n2)

total_orbits = 0
level = 1
queue = collections.deque()
queue.append('COM')

while queue:
    print(queue)
    n = len(queue)
    for _ in range(n):
        p = queue.popleft()
        children = planets[p]
        total_orbits += len(children) * level
        queue.extend(children)

    level += 1

print(total_orbits)


# lmaoo
def traverse(node, lst, target):
    lst.append(node)

    if node == target:
        print(lst)
        return
    elif len(planets[node]) == 0:
        return 
    else:
        children = planets[node]
        for c in children:
            traverse(c, lst.copy(), target)

traverse('COM', [], 'YOU')
traverse('COM', [], 'SAN')