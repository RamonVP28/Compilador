from Analizador_Lexico import TableTokens

Operaciones = {}

def setOperaciones(Elemento, Operacion):
    Operaciones[Elemento] = Operacion

def AnalizadorSemantico():
    ListTokens = TableTokens
    aux = ""
    tabulaciones = ""
    for Token in ListTokens:
        if Token == "ClassName":
            aux += "<Clase" + ListTokens[Token] + ">\n"
        elif Token == "InicioClass":
            aux += "<Bloque>\n"
            tabulaciones += "\t"
        elif Token == "string" or Token == "float" or Token == "int":
            aux += tabulaciones +"<Variable " + ListTokens[Token] + ">\n"
        elif Token == "Function":
            aux += tabulaciones + "<Función " + ListTokens[Token] + ">\n"
        elif Token == "InicioFunction":
            aux += tabulaciones + "<Bloque>\n"
            tabulaciones += "\t" 
        elif Token == "Print":
            aux += tabulaciones + "<Imprección " + ListTokens[Token] + ">\n"
            if "Print" in Operaciones:
                tabulaciones += "\t"
                temp = Operaciones["Print"].strip()
                temp += "+"
                SubAux = ""
                for c in temp:
                    SubAux += c
                    if c == "+":
                        aux += tabulaciones + "<Concatenar " + SubAux + ">\n"
                        aux = aux.replace("+", "").replace("(", "")
                        SubAux = ""
            tabulaciones = tabulaciones[:-1]
        elif Token == "EndFunction":
            tabulaciones = tabulaciones[:-1]
            aux += tabulaciones + "<Fin de Funcion>\n"
        elif Token == "EndClass":
            tabulaciones = tabulaciones[:-1]
            aux += tabulaciones + "<Fin de Clase>\n"
    aux = "<inicio>\n" + aux + "<fin>\n"
    return aux