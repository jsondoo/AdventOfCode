from itertools import permutations

with open('input.txt', 'r') as file:
    text = file.read().split(',')

text = list(map(int, text))

taken = [False] * 5

# TODO trace mode

def intcode(inp1, inp2, amp):
    data = text[:] # may have to change so each amp has own memory
    print(data)
    print(inp1, inp2)
   
    i = 0
    while i < len(data):
        inst = str(data[i]) 
        # pad with zeros to make 5 characters
        inst = list('0'* (5 - len(inst)) + inst)
        DE = int(''.join(inst[-2:]))

        # for A,B,C, 1 is immediate mode, 0 is position mode
        if DE == 1:
            C, B, A = int(inst[-3]), int(inst[-4]), int(inst[-5])
            p1, p2, p3 = data[i+1], data[i+2], data[i+3]
            data[p3] = (p1 if C == 1 else data[p1]) + (p2 if B == 1 else data[p2])
            i += 4
        elif DE == 2:
            C, B, A = int(inst[-3]), int(inst[-4]), int(inst[-5])
            p1, p2, p3 = data[i+1], data[i+2], data[i+3]
            data[p3] = (p1 if C == 1 else data[p1]) * (p2 if B == 1 else data[p2])
            i += 4
            print(data)
        elif DE == 3:
            p1 = data[i+1]
            if not taken[amp]:
                data[p1] = inp1
                taken[amp] = True
            else:
                data[p1] = inp2
            i += 2
            print(data)
        elif DE == 4:
            print(data)
            p1 = data[i+1]
            i += 2
            return data[p1]
        elif DE == 5:
            C, B = int(inst[-3]), int(inst[-4])
            p1, p2 = data[i+1], data[i+2]
            p1, p2 = p1 if C == 1 else data[p1], p2 if B == 1 else data[p2]
            if p1 != 0:
                i = p2
            else:
                i += 3
        elif DE == 6:
            C, B = int(inst[-3]), int(inst[-4])
            p1, p2 = data[i+1], data[i+2]
            p1, p2 = p1 if C == 1 else data[p1], p2 if B == 1 else data[p2]
            if p1 == 0:
                i = p2
            else:
                i += 3
        elif DE == 7:
            C, B, A = int(inst[-3]), int(inst[-4]), int(inst[-5])
            p1, p2, p3 = data[i+1], data[i+2], data[i+3]
            p1, p2 = p1 if C == 1 else data[p1], p2 if B == 1 else data[p2]
            if p1 < p2:
                data[p3] = 1
            else:
                data[p3] = 0
            i += 4
        elif DE == 8:
            C, B, A = int(inst[-3]), int(inst[-4]), int(inst[-5])
            p1, p2, p3 = data[i+1], data[i+2], data[i+3]
            p1, p2 = p1 if C == 1 else data[p1], p2 if B == 1 else data[p2]
            if p1 == p2:
                data[p3] = 1
            else:
                data[p3] = 0
            i += 4
        elif DE == 99:
            break

best = float('-inf')

settings = permutations([i for i in range(5)])

for setting in settings:
    print(setting)
    taken = [False] * 5
    inp = 0
    for amp, p in enumerate(setting):
        inp = intcode(p, inp, amp)
    best = max(best, inp)

print(best)

