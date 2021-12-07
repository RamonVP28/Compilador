from Analizador_Sintactico import GetFile, Sintactic, WriteFile
from Analizador_Lexico import AnalizadorLexico
import sys

if __name__ == "__main__":
    code = sys.argv[1]
    WriteFile("./Temp/Code.mr", code)
    status = GetFile("./Temp/Code.mr")
    if status[1] != True:
        result = Sintactic(status[0])
        print(result)
        if "Error" not in result:
            print(AnalizadorLexico())