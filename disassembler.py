def add(x:int, y:int):
    z = x + y
    print (x+y)

def hextobin(line:str):
    binary_value = ""
    for i in line:
        binary_value += bin(int(i, 16))[2:].zfill(4)
    return binary_value

def twos_comptodeci(imm):
    if imm[0] == "1":
        inverted_str = ''
        for bit in imm:
            inverted_str += '1' if bit == '0' else '0'
            decimal_value = -(int(inverted_str, 2) + 1)
    else:
        decimal_value = int(imm, 2)
    return decimal_value

def shift_and_insert(arr, index, new_value):
    if index < 0 or index >= len(arr):
        print("Invalid index")
        return

    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]

    # Insert the new value at the specified index
    arr[index] = new_value
