f = open('./day01.txt', 'r')
masses = map(int, f.readlines())

mass_to_fuel = map(lambda m : m // 3 - 2, masses)

print("Part 1 answer:")
print(sum(mass_to_fuel))


def massive(mass):
	fuel = mass // 3 -2
	return fuel + massive(fuel) if fuel >= 0 else 0

mass_to_fuel2 = map(lambda yeet : massive(yeet), masses)

print("Part 2 answer:")
print(sum(mass_to_fuel2))



