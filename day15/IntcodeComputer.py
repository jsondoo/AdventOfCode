from collections import deque

def getOperandValue(computer, parameter, mode):
    if mode == 0: 
        if parameter >= len(computer.mem): computer.mem.extend([0 for _ in range(parameter-len(computer.mem)+1)])
        return computer.mem[parameter]
    if mode == 1: 
        return parameter
    if mode == 2:
        idx = parameter + computer.relative_base
        if idx >= len(computer.mem): computer.mem.extend([0 for _ in range(idx-len(computer.mem)+1)])
        return computer.mem[parameter + computer.relative_base]

def getAddress(computer, parameter, mode):
    val = None
    if mode == 0: val = parameter
    if mode == 1: print("this shouldnt happen")
    if mode == 2: val = parameter + computer.relative_base

    if val is None: print("Error in getting address")
    if val >= len(computer.mem): computer.mem.extend([0 for _ in range(val-len(computer.mem)+1)])

    return val


class IntcodeComputer:
    def __init__(self, mem, initial_inputs=[]):
        self.mem = mem[:]
        self.ip = 0
        self.relative_base = 0
        self.inputQ = deque(initial_inputs)
        self.output = []
        self.halted = False

    def run(self, inputs=[]):  # inputs: list of inputs after phase_setting
        self.inputQ.extend(inputs)
        while (self.ip < len(self.mem)):
            op_code = self.mem[self.ip]%100
            p1_mode = (self.mem[self.ip] // 100) % 10
            p2_mode = (self.mem[self.ip] // 1000) % 10
            p3_mode = (self.mem[self.ip] // 10000) % 10

            param1, param2, param3 = (None if self.ip+1 >= len(self.mem) else self.mem[self.ip+1]), \
                                     (None if self.ip+2 >= len(self.mem) else self.mem[self.ip+2]), \
                                     (None if self.ip+3 >= len(self.mem) else self.mem[self.ip+3])

            if op_code == 1:
                addend1, addend2 = getOperandValue(self, param1, p1_mode), getOperandValue(self, param2, p2_mode)
                self.mem[getAddress(self, param3, p3_mode)] = addend1 + addend2
                self.ip+=4
            elif op_code == 2:
                mul1, mul2 = getOperandValue(self, param1, p1_mode), getOperandValue(self, param2, p2_mode)
                self.mem[getAddress(self, param3, p3_mode)] = mul1 * mul2
                self.ip+=4
            elif op_code == 3:
                if len(self.inputQ) <= 0: print("Error; input queue empty\n\n")
                val = self.inputQ.popleft()
                self.mem[getAddress(self, param1, p1_mode)] = int(val)
                self.ip+=2
            elif op_code == 4:
                val = getOperandValue(self, param1, p1_mode)
                self.output.append(val)
                self.ip+=2
                return val
            elif op_code == 5:
                param1, param2 =  getOperandValue(self, param1, p1_mode), getOperandValue(self, param2, p2_mode)
                if param1 != 0: self.ip = param2
                else: self.ip+= 3
            elif op_code == 6:
                param1, param2 =  getOperandValue(self, param1, p1_mode), getOperandValue(self, param2, p2_mode)
                if param1 == 0: self.ip = param2
                else: self.ip+= 3
            elif op_code == 7:
                param1, param2 = getOperandValue(self, param1, p1_mode), getOperandValue(self, param2, p2_mode)
                self.mem[getAddress(self, param3, p3_mode)] = 1 if param1 < param2 else 0
                self.ip+= 4
            elif op_code == 8:
                param1, param2 = getOperandValue(self, param1, p1_mode), getOperandValue(self, param2, p2_mode)
                self.mem[getAddress(self, param3, p3_mode)] = 1 if param1 == param2 else 0
                self.ip+= 4
            elif op_code == 9:
                param1 = getOperandValue(self, param1, p1_mode)
                self.relative_base += param1
                self.ip+=2
            elif op_code == 99:
                self.halted = True
                break
            else:
                print("invalid opcode", op_code)
                break