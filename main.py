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
    
    j = 0
    for instruction in instruction_list:
        if instruction.opcode == "beq" or instruction.opcode == "bne":
            label_list.append(j)
            temp = hex_data[j]
            instruction.addr = temp[-4:]
            
        j += 1
    print("Successfully identified branch targets")
    
    target_index = []
    index_select = []
    # Parsing through object list per index
    for i in range(len(instruction_list)):
        if i in label_list:
            print(instruction_list[i].imm)
            new_pos = i+int(instruction_list[i].imm)+1
            print(new_pos)
            if new_pos not in target_index:
                target_index.append(new_pos)
                index_select.append(i)
    print("Target:")
    print(target_index)
    print("Index:")
    print(index_select)
    
    

    # Begins new file generation
    new_file = filetitle+".s"
    try:
        new_file = open(new_file,"x")
    except FileExistsError:
        print("Error: File already exists. Overwriting preexistent file.")
        new_file = open(new_file,"w")
    
    line = 0
    branch_counter = 0
    for instruction in instruction_list:
        for index in range(len(target_index)):
            if line == target_index[index]:
                address = format(target_index[index]*4, '04X')
                new_file.write("Addr_"+str(address)+":\n")


        if (isinstance(instruction,RegisterInstruction)):
            if instruction.funct == "sll" or instruction.funct == "srl":
                concat = ("\t"+instruction.funct+" "+instruction.rd+", "+instruction.rt+", "+str(instruction.shamt))
            else:
                concat = ("\t"+instruction.funct+" "+instruction.rd+", "+instruction.rs+", "+instruction.rt)
            new_file.write(concat+"\n")
        elif (isinstance(instruction,ImmediateInstruction)):
            if instruction.opcode == "sw" or instruction.opcode == "lw":
                concat = ("\t"+instruction.opcode+" "+instruction.rt+", "+str(instruction.imm)+"("+instruction.rs+")")
            elif instruction.opcode == "beq" or instruction.opcode == "bne":
                branch_counter += 1
                concat = ("\t"+instruction.opcode+" "+instruction.rs+", "+instruction.rt+", Addr_"+str(format((line+instruction.imm+1)*4, '04X')))
                print(str(instruction.imm))
                print(str(instruction.addr))
                print(line+instruction.imm+1)
            else:
                concat = ("\t"+instruction.opcode+" "+instruction.rt+", "+instruction.rs+", "+str(instruction.imm))
            new_file.write(concat+"\n")
        elif (isinstance(instruction,JumpInstruction)):
            print("Jump not implemented")
        line+=1
    
    new_file.close()
            

if __name__ == "__main__":
    main()
