from Analizador_Lexico import TableTokens, setTableTokens

#Obtenemos el código
def GetFile(filename):
    stop = False
    try:
        file = open(filename, "r")
        Code = file
        return [Code,stop]
    except FileNotFoundError:
        Error = "Error 0: Archivo no encontrado"
        stop = True
        return [Error,stop]

#Buscar error 
def Error(input, error):
    aux = input
    if error != ":":
        input = input[:len(error)-1]
    temp = ""
    print(len(input))
    print(input)
    for i in range(len(input)):
        temp += " "
    temp += "^"
    return aux + "\n" + temp

#Analizador sintáctico
def Sintactic(Code):
    aux = ""
    count = 0
    FuncOpen = False
    for lines in Code:
        if lines != "\n":
            aux += lines
            count += 1
        if "//" in lines:
            aux = lines[:lines.index("//")] + "\n"
        if "class" in lines:
            if lines[lines.index("class")+len("class")] == " ":
                setTableTokens("ClassName", lines[lines.index("class")+len("class"):].strip())
            else:
                return "Error (sintaxis) linea {}: Falta espacio en blanco\n".format(count) + Error(lines.strip(), "class")
            if (temp := lines.strip())[len(temp)-1] != ":":
                return "Error (sintaxis) linea {}: Faltan dos puntos para abrir la clase\n".format(count) + Error(lines.strip(), ":")
            else:
                setTableTokens("InicioClass", ":")
        if "=" in lines:
            temp = lines[:lines.index("=")].strip()
            if isint(temp) or isfloat(temp):
                return "Error (sintaxis) linea {}: No se puede asignar un valor a un dato numerico\n".format(count) + Error(lines.strip(), temp)
            temp2 = lines[lines.index("=")+1:].strip()
            if temp2[0] == "\"" and temp2[len(temp2)-1] == "\"":
                setTableTokens(temp, "string")
            if isint(temp2):
                setTableTokens(temp, "int")
            if isfloat(temp2):
                setTableTokens(temp, "float")
        if "function" in lines:
            if lines[lines.index("function")+len("function")] == " ":
                setTableTokens("Function", lines[lines.index("function")+len("function"):].strip())
            else:
                return "Error (sintaxis) linea {}: Falta espacio en blanco\n".format(count) + Error(lines.strip(), "function")
            if (temp := lines.strip())[len(temp)-1] != ":":
                return "Error (sintaxis) linea {}: Faltan dos puntos para abrir la clase\n".format(count) + Error(lines.strip(), ":")
            else:
                FuncOpen = True
                setTableTokens("InicioFunction", ":")
            temp = lines[lines.index("function")+len("function"):]
            if lines.find("(") == -1:
                return "Error (sintaxis) linea {}: Falta parentesis\n".format(count) + Error(lines.strip(), lines[:lines.index(":")-1])
            if lines.find(")") == -1:
                return "Error (sintaxis) linea {}: Falta parentesis\n".format(count) + Error(lines.strip(), lines[:lines.index(":")-1])
        if "end" in lines:
            if "InicioFunction" in TableTokens and FuncOpen == True:
                FuncOpen = False
                setTableTokens("EndFunction", "end")
            elif "InicioClass" in TableTokens:
                setTableTokens("EndClass", "end")
    if "InicioClass" in TableTokens and "EndClass" not in TableTokens:
        return "Error (sintaxis): No a cerrado una clase o función\n"
    print(TableTokens)
    print(aux)

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False