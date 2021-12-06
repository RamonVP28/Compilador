from Analizador_Sintactico import GetFile, Sintactic

if __name__ == "__main__":
    status = GetFile("Codigo.mr")
    if status[1] == True:
        print(status[0])
    else:
        print(Sintactic(status[0]))
