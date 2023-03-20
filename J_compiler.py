
machine_code_dict = {
    "HLT": "0",
    "LDA": "1",
    "STA": "2",
    "LDB": "3",
    "IMD": "4",
    "ADD": "5",
    "SUB": "6",
    "LTH": "7",
    "GTH": "8",
    "EQT": "9",
    "LSH": "a",
    "RSH": "b",
    "JMP": "c",
    "STB": "d",
    "PRT": "e",
}

while_dict = {}

variables_dict = {}

output = ["00" for i in range(0, 16*16)]


if __name__ == "__main__":
    name = open("compiler_logs/filename.txt")
    filename = name.readline()[0:-1]

    if(filename[-2:] != ".j" and filename[-3:] != ".jp" and filename[-4:] != ".jpp"):
        quit()

    if(filename[-4:] == ".jpp"):
        filename = filename[:-2]
    if(filename[-3:] == ".jp"):
        filename = filename[:-1]


    print(filename)

    try:
        f = open(filename, "r")
    except:
        try:
            f = open("compiler_logs/"+filename, "r")
        except:
            print("file doesnt exist")
            quit()


    o = open(filename[:-2], "w")

    i = 0
    
    for line in f:
        i += 1
        if line[0:3] == "END":
            break
        if i >= 16*16:
            print("code forced to end there was too many lines")
            break

        #set variable
        if line[0] == "$":
            var_str = ""
            j = 1
            length = len(line)-1
            while j < length and line[j] != " " and line[j] != "":
                var_str += line[j]
                j += 1
            j += 1
            add_str = ""
            while j < length and line[j] != " ":
                add_str += line[j]
                j += 1
            
            variables_dict.update({var_str: str(hex(int(add_str)))[-1:]})
        
            i -= 1

        elif line[0] == "#":

            var_str = ""
            j = 1
            length = len(line)-1
            while j < length and line[j] != " " and line[j] != "":
                var_str += line[j]
                j += 1
        
            i -= 1
            
            while_dict.update({var_str: str(i)})
        
        #write line of code
        else:
            #is a variable used
            if (line[4] == "$"):
                output[i] = machine_code_dict[line[0:3]] + str(hex(int(variables_dict[line[5:-1]])))[-1:]
            elif (line[4] == "#"):
                output[i] = machine_code_dict[line[0:3]] + str(hex(int(while_dict[line[5:-1]])))[-1:]
            else:
                output[i] = machine_code_dict[line[0:3]] + str(hex(int(line[4:-1])))[-1:]

    o.write("v3.0 hex words addressed\n")

    for i in range (0, 16):
            o.write(str(hex(i))[-1:])
            o.write("0: ")
            for j in range (0, 15):
                o.write(output[i*16 + j])
                o.write(" ")
            o.write(output[i*16 + 15])
            o.write("\n")
    
    print("compiled successfully")


