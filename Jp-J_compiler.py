
while_dict = {}
whiles = []

output = ["00" for i in range(0, 16*16)]

determined_var = 0

variable_adress_space = 0


if __name__ == "__main__":
    name = open("compiler_logs/filename.txt")
    filename = name.readline()[0:-1]

    if(filename[-3:] != ".jp" and filename[-4:] != ".jpp"):
        quit()

    if(filename[-4:] == ".jpp"):
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


    o = open("compiler_logs/"+filename[:-3]+".j", "w")

    i = 0
    
    for line in f:
        i += 1
        if line[0:3] == "END":
            break
        if i >= 16*16:
            print("code forced to end there was too many lines")
            break

        #while loop start
        if line[0] == "#":

            var_str = ""
            j = 8
            length = len(line)-1
            while j < length and line[j] != "{":
                var_str += line[j]
                j += 1
        
            i -= 1
            
            whiles.append((str(determined_var), var_str))

            o.write("#" + str(determined_var) + "\n")
            determined_var += 1
        
        #while loop end
        elif line[0] == "}":
            ref, var = whiles.pop()
            o.write("LDB $" + var + "\nJMP #" + ref + "\n")

        elif line[0] == "$":

            var_str = ""
            j = 1
            length = len(line)-1
            while j < length and line[j] != " ":
                var_str += line[j]
                j += 1
            j += 1
        
            i -= 1
            
            
            o.write("$" + var_str + " " + str(variable_adress_space) + "\nIMD " + line[j:length] + "\nSTA " + str(variable_adress_space) + "\n")
            variable_adress_space += 1


        #write line of code
        else:
            o.write(line)

    o.write("END 0")

    print("compiled successfully")


