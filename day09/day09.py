with open('input.txt', 'r') as file:
    data = file.read().split(',')

data = list(map(int, data))

# text might need more space
# TODO
data.extend([0]*10000)
print(data)

def intcode():
    rel_base = 0
    i = 0
    inpoot = 1

    while i < len(data):
        # print(rel_base)
        inst = str(data[i]) 
        # pad with zeros to make 5 characters
        inst = list('0'* (5 - len(inst)) + inst)
        DE = int(''.join(inst[-2:]))

        # for A,B,C, 1 is immediate mode, 0 is position mode
        if DE == 1:
            C, B, A = int(inst[-3]), int(inst[-4]), int(inst[-5])
            p1, p2, p3 = data[i+1], data[i+2], data[i+3]

            # new
            p1, p2 = p1 + rel_base if C == 2 else p1, p2 + rel_base if B == 2 else p2

            data[p3] = (p1 if C == 1 else data[p1]) + (p2 if B == 1 else data[p2])
            i += 4
        elif DE == 2:
            C, B, A = int(inst[-3]), int(inst[-4]), int(inst[-5])
            p1, p2, p3 = data[i+1], data[i+2], data[i+3]

            # new
            p1, p2 = p1 + rel_base if C == 2 else p1, p2 + rel_base if B == 2 else p2

            data[p3] = (p1 if C == 1 else data[p1]) * (p2 if B == 1 else data[p2])
            i += 4
        elif DE == 3:
            C = int(inst[-3])
            p1 = data[i+1]

            # support parameters
            p1 = p1 + rel_base if C == 2 else p1

            if C == 1:
                data[p1] = inpoot
            else:
                data[data[p1]] = inpoot
            i += 2
        elif DE == 4:
            C = int(inst[-3])
            p1 = data[i+1]

            # support parameters
            p1 = p1 + rel_base if C == 2 else p1

            if C == 1:
                print(p1)
            else:
                print(data[p1])
            i += 2
        elif DE == 5:
            C, B = int(inst[-3]), int(inst[-4])
            p1, p2 = data[i+1], data[i+2]

            # new
            p1, p2 = p1 + rel_base if C == 2 else p1, p2 + rel_base if B == 2 else p2

            p1, p2 = p1 if C == 1 else data[p1], p2 if B == 1 else data[p2]
            if p1 != 0:
                i = p2
            else:
                i += 3
        elif DE == 6:
            C, B = int(inst[-3]), int(inst[-4])
            p1, p2 = data[i+1], data[i+2]

            # new
            p1, p2 = p1 + rel_base if C == 2 else p1, p2 + rel_base if B == 2 else p2

            p1, p2 = p1 if C == 1 else data[p1], p2 if B == 1 else data[p2]
            if p1 == 0:
                i = p2
            else:
                i += 3
        elif DE == 7:
            C, B, A = int(inst[-3]), int(inst[-4]), int(inst[-5])
            p1, p2, p3 = data[i+1], data[i+2], data[i+3]

            # new
            p1, p2 = p1 + rel_base if C == 2 else p1, p2 + rel_base if B == 2 else p2

            p1, p2 = p1 if C == 1 else data[p1], p2 if B == 1 else data[p2]
            if p1 < p2:
                data[p3] = 1
            else:
                data[p3] = 0
            i += 4
        elif DE == 8:
            C, B, A = int(inst[-3]), int(inst[-4]), int(inst[-5])
            p1, p2, p3 = data[i+1], data[i+2], data[i+3]

            # new
            p1, p2 = p1 + rel_base if C == 2 else p1, p2 + rel_base if B == 2 else p2

            p1, p2 = p1 if C == 1 else data[p1], p2 if B == 1 else data[p2]
            if p1 == p2:
                data[p3] = 1
            else:
                data[p3] = 0
            i += 4
        elif DE == 9:
            C = int(inst[-3])
            p1 = data[i+1]

            if C == 1:
                rel_base += p1
            elif C == 0:
                rel_base += data[p1]
            else:
                rel_base += data[p1 + rel_base]
            i += 2
        elif DE == 99:
            break
        else:
            print("Wrong op code: ", DE)

    return

intcode()