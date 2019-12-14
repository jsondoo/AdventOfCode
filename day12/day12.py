import math
memory = open('input.txt', 'r').read().split('\n')
velocity = [[0,0,0] for _ in range(4)]
moons = []
for moon in memory:
    c = []
    for i,coords in enumerate(moon.split(',')):
        val = coords.split('=')[1]
        if i == 2:
            val = val[:-1]
        c.append(int(val))
    moons.append(c)

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

def total_energy():
    total = 0
    for i in range(len(moons)):
        moon, vel = moons[i], velocity[i]
        p, k = 0, 0
        for xyz in moon:
            p += abs(xyz)
        for v in vel:
            k += abs(v)
        total += p * k
    return total

def step():
    global velocity, moons
    len_x, len_y, len_z = None, None, None
    seenx, seeny, seenz = set(), set(), set()

    step = 0
    while True and (not len_x or not len_y or not len_z):
        # apply GRAVITY
        for m1 in range(len(moons)):
            for m2 in range(m1+1, len(moons)):
                # m1 and m2 are indices
                moon1, moon2 = moons[m1], moons[m2] # moon runes
                for xyz in range(3):
                    if moon1[xyz] > moon2[xyz]:
                        velocity[m1][xyz] -= 1
                        velocity[m2][xyz] += 1
                    elif moon1[xyz] < moon2[xyz]:
                        velocity[m2][xyz] -= 1
                        velocity[m1][xyz] += 1

        # apply VELOCITY
        for i in range(len(moons)):
            moons[i][0] += velocity[i][0]
            moons[i][1] += velocity[i][1]
            moons[i][2] += velocity[i][2]

        x = (moons[0][0],moons[1][0],moons[2][0],moons[3][0],velocity[0][0],velocity[1][0],velocity[2][0],velocity[3][0])
        y = (moons[0][1],moons[1][1],moons[2][1],moons[3][1],velocity[0][1],velocity[1][1],velocity[2][1],velocity[3][1])
        z = (moons[0][2],moons[1][2],moons[2][2],moons[3][2],velocity[0][2],velocity[1][2],velocity[2][2],velocity[3][2])

        if x not in seenx:
            seenx.add(x)
        elif not len_x:
            len_x = step

        if y not in seeny:
            seeny.add(y)
        elif not len_y:
            len_y = step

        if z not in seenz:
            seenz.add(z)
        elif not len_z:
            len_z = step

        step += 1

    return (len_x, len_y, len_z)

cx,cy,cz = step()
print(lcm(lcm(cx,cy),cz))
