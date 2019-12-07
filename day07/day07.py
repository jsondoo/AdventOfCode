from itertools import permutations

with open('input.txt', 'r') as file:
    text = file.read().split(',')

text = list(map(int, text))

def intcode(amp):
    # retrieve amp state
    i = idx[amp]
    data = memory[amp] 
    inp = inputs[amp]

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
        elif DE == 3:
            p1 = data[i+1]
            data[p1] = inp.pop(0)
            i += 2
        elif DE == 4:
            p1 = data[i+1]
            i += 2
            outs[amp] = data[p1]
            inputs[(amp + 1) % 5].append(data[p1])
            idx[amp] = i
            memory[amp] = data
            return
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
            halted[amp] = True
            break

    return

best = float('-inf')
settings = permutations([5,6,7,8,9])
# settings = [[0,1,2,4,3]]

# amplifier states
halted = [False] * 5
idx = [0] * 5
outs = [0] * 5
inputs = []
memory = [list(text) for i in range(5)]

for setting in settings:
    print(setting)
    halted = [False] * 5
    idx = [0] * 5
    outs = [0] * 5
    inputs = [[setting[i]] for i in range(5)]
    memory = [list(text) for i in range(5)]
    inputs[0].append(0)

    while not any(halted):
        for amp in range(5):
            intcode(amp)
            if any(halted):
                break
            
    best = max(best, max(outs))
        

print(best)

