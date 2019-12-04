with open('input.txt', 'r') as file:
    data = file.read()

inputL = 158126
inputR = 624574

def criteria(n):
    never_decrease = True
    adjacent = False

    prev = length = None
    for i,a in enumerate(str(n)):
        a = int(a)

        if i == 0:
            prev = a
            length = 1
        else:
            if a < prev:
                never_decrease = False 

            if prev == a:
                length += 1
            elif length == 2:
                adjacent = True
            else:
                length = 1

            prev = a

    return never_decrease and (length == 2 or adjacent)

count = 0
for x in range(inputL+1, inputR):
    if criteria(x):
        count += 1

print(count)