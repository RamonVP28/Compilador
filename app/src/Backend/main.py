from Analizador_Sintactico import GetFile, Sintactic, WriteFile
from Analizador_Lexico import AnalizadorLexico
from Analizar_Semantico import AnalizadorSemantico

def run(code):
    WriteFile("./Temp/Code.mr", code)
    status = GetFile("./Temp/Code.mr")
    if status[1] != True:
        result = "<Inicio Sintactico>" + Sintactic(status[0]) + "<Fin Sintactico>"
        if "Error" not in result:
            result += "\n" + "<Inicio Lexico>" + str(AnalizadorLexico()) + "<Fin Lexico>"
            result += "\n" + "<Inicio Semantico>" + AnalizadorSemantico() + "<Fin Semantico>"
    return result