import sys
import disassembler
import inspect
import instruction_format
from instruction_format import RegisterInstruction
from instruction_format import ImmediateInstruction
from instruction_format import JumpInstruction
import binascii

def main():
    filetitle = str(input("Enter filename w/o extension: "))
    filename = filetitle + ".obj"
    print(filename)
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("FileNotFoundError: This file does not exist")
        sys.exit(0)
    except IOError:
        print("IOError: There was an error loading this file")
        sys.exit(0)
    except:
        print("Invalid filename")
        sys.exit(0)
    hex_data = []
    data = []
    instruction_list = []
    for line in file:
        line = line[:-1]
        hex_line = str(line)
        binary_line = disassembler.hextobin(line);
        hex_data.append(hex_line)
        data.append(binary_line)

    print (data)
    print (hex_data)
    i = 0
    for code in data:
        print(str(i)+":"+code)
        i+=1
        decimal_opcode = int(code[:6],2)
        if decimal_opcode == 0:
            instf = RegisterInstruction(code)
        elif decimal_opcode == 2 or decimal_opcode == 3:
            instf = JumpInstruction(code)
        else:
            instf = ImmediateInstruction(code)
        instruction_list.append(instf)
    
    # Checks for branch instructions and creates labels
    label_list = []
    address_list = []
    for instruction in instruction_list:
        if instruction.opcode == "beq" or instruction.opcode == "bne":
            instruction.
    for instruction in instruction_list:
        if (instruction_list.index(instruction)) in label_list:
            #Isolates position for Address tag
            new_pos = instruction_list.index(instruction)+instruction.imm+1
            if new_pos in address_list:
                pass
            else:
                address_list.append(new_pos)
                instruction_list[new_pos:] = disassembler.shift_elements(instruction_list[new_pos:],1)


    # Begins new file generation
    new_file = filetitle+".s"
    try:
        new_file = open(new_file,"x")
    except FileExistsError:
        print("Error: File already exists. Overwriting preexistent file.")
        new_file = open(new_file,"w")
    
    for instruction in instruction_list:
        if (isinstance(instruction,RegisterInstruction)):
            if instruction.funct == "sll" or instruction.funct == "srl":
                concat = (instruction.funct+" "+instruction.rd+", "+instruction.rt+", "+str(instruction.shamt))
            else:
                concat = (instruction.funct+" "+instruction.rd+", "+instruction.rs+", "+instruction.rt)
            new_file.write(concat+"\n")
        elif (isinstance(instruction,ImmediateInstruction)):
            if instruction.opcode == "sw" or instruction.opcode == "lw":
                concat = (instruction.opcode+" "+instruction.rt+", "+str(instruction.imm)+"("+instruction.rs+")")
            elif instruction.opcode == "beq" or instruction.opcode == "bne":
                print(str(instruction.addr)+"\n")
                concat = (instruction.opcode+" "+instruction.rs+", "+instruction.rt+", "+str(instruction.imm))
            else:
                concat = (instruction.opcode+" "+instruction.rs+", "+instruction.rt+", "+str(instruction.imm))
            new_file.write(concat+"\n")
        elif (isinstance(instruction,JumpInstruction)):
            print("Jump not implemented")
    new_file.seek(0)
    
    new_file.close()
            


if __name__ == "__main__":
    main()
