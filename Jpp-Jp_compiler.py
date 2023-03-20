
while_dict = {}
whiles = []

output = ["00" for i in range(0, 16*16)]

determined_var = 0

variable_adress_space = 0


if __name__ == "__main__":
    name = open("compiler_logs/filename.txt")
    filename = name.readline()[0:-1]

    if(filename[-4:] != ".jpp"):
        quit()

    print(filename)

    try:
        f = open(filename, "r")
    except:
        try:
            f = open("compiler_logs/"+filename, "r")
        except:
            print("file doesnt exist")
            quit()


    o = open("compiler_logs/"+filename[:-4]+".jp", "w")

    i = 0

    for line in f:
        i += 1
        if line[0:3] == "END":
            break
        if i >= 16*16:
            print("code forced to end there was too many lines")
            break

        #while loop start
        if line[0] == "@":

            var_str = ""
            j = 4
            length = len(line)-1
            while j < length and line[j] != "=":
                var_str += line[j]
                j += 1
            j += 1



            start_val = ""
            while j < length and line[j] != ":":
                start_val += line[j]
                j += 1
            j += 1


            symbol = line[j]
            j += 1

            comparator_str = ""
            while j < length and line[j] != ":":
                comparator_str += line[j]
                j += 1
            j += 1

            symbol2 = line[j]
            j += 1

            to_add = ""
            while j < length and line[j] != "{":
                to_add += line[j]
                j += 1
            j += 1

            i -= 1
            
            whiles.append((var_str, symbol, comparator_str, symbol2, to_add))

            o.write(var_str + " " + start_val + "\n$looping_var 0\n#WHILE $looping_var{\n")
            determined_var += 1
        
        #while loop end
        elif line[0] == "}":
            var_str, symbol, comparator_str, symbol2, to_add = whiles.pop()
            if(var_str != ""):
                o.write("LDA " + var_str + "\n")
                if(symbol2 == "-"):
                    o.write("SUB " + to_add + "\n")
                else:
                    o.write("ADD " + to_add + "\n")

                o.write("STB " + var_str + "\n")

                o.write("LDA " + var_str + "\n")

                if(symbol == ">"):
                    o.write("GTH " + comparator_str + "\n")
                elif(symbol == "<"):
                    o.write("LTH " + comparator_str + "\n")
                elif(symbol == "="):
                    o.write("EQT " + comparator_str + "\n")
                else:
                    print("comparator not supported yet")

                o.write("STB $looping_var\n}\n")
            else:
                o.write("}\n")


        #write line of code
        else:
            if(line[0] == "#"):
                whiles.append(("", "", "", "", ""))
            o.write(line)

    o.write("END 0")

    print("compiled successfully")


