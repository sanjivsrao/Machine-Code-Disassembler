from disassembler import twos_comptodeci
import sys


class RegisterInstruction:
    def __init__(self, binary_string):
        if len(binary_string) != 32:
            raise ValueError("Opcode must be 32 bits long")
        self.type = "R"
        self.index
        self.opcode = int(binary_string[:6],2)
        self.rs = RegisterDict[int(binary_string[6:11],2)]
        self.rt = RegisterDict[int(binary_string[11:16],2)]
        self.rd = RegisterDict[int(binary_string[16:21],2)]
        self.shamt = int(binary_string[21:26], 2)
        self.funct = RFuncDict[int(binary_string[26:],2)]

class ImmediateInstruction:
    def __init__(self, binary_string):
        if len(binary_string) != 32:
            raise ValueError("Opcode must be 32 bits long")
        self.type = "I"
        self.index
        op = int(binary_string[:6],2)
        if op in OpCodeDict:
            self.opcode = OpCodeDict[int(binary_string[:6],2)]
        else:
            print("Cannot disassemble "+str(op)+ " at line "+str(i))
            sys.exit(0)
        self.rs = RegisterDict[int(binary_string[6:11],2)]
        self.rt = RegisterDict[int(binary_string[11:16],2)]
        self.imm = twos_comptodeci(binary_string[16:])
        self.addr = twos_comptodeci(binary_string[16:])
        
class JumpInstruction:
    def __init__(self, binary_string):
        if len(binary_string) != 32:
            raise ValueError("Input binary string must be 32 bits long")
        self.type = "J"
        self.index
        self.opcode = JumpDict[int(binary_string[:6],2)]
        self.addr = hex(int(binary_string[6:])).zfill(4)

OpCodeDict = {
    8: "addi",
    9: "addiu",
    12: "andi",
    4: "beq",
    5: "bne",
    36: "lbu",
    37: "lhu",
    48: "ll",
    15: "lui",
    35: "lw",
    13: "ori",
    10: "slti",
    11: "sltiu",
    40: "sb",
    56: "sc",
    41: "sh",
    43: "sw"
}

JumpDict = {
    2 : "j",
    3 : "jal",
}

RFuncDict = {
    32: "add",
    33: "addu",
    36: "and",
    8: "jr",
    39: "nor",
    37: "or",
    42: "slt",
    43: "sltu",
    0: "sll",
    2: "srl",
    34: "sub",
    35: "subu"
}

RegisterDict = {
    0: "$zero",
    1: "$at",
    2: "$v0",
    3: "$v1",
    4: "$a0",
    5: "$a1",
    6: "$a2",
    7: "$a3",
    8: "$t0",
    9: "$t1",
    10: "$t2",
    11: "$t3",
    12: "$t4",
    13: "$t5",
    14: "$t6",
    15: "$t7",
    16: "$s0",
    17: "$s1",
    18: "$s2",
    19: "$s3",
    20: "$s4",
    21: "$s5",
    22: "$s6",
    23: "$s7",
    24: "$t8",
    25: "$t9",
    26: "$k0",
    27: "$k1",
    28: "$gp",
    29: "$sp",
    30: "$fp",
    31: "$ra"
}