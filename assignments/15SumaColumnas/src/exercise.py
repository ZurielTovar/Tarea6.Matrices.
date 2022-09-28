def main():
    #escribe tu código abajo de esta línea
    r = int(input())
    c = int(input())
    if r > 0 and c > 0:
        suma = 0
        matriz = []
        resultados = []
        for i in range (r):
            renglones = []
            for j in range (c):
                num = int(input())
                renglones.append(num)
            matriz.append(renglones)

        for j in range (c):
            suma = 0
            for l in range (r):
                suma = suma + matriz[l][j]
            resultados.append(suma)

        print(resultados)
    else:
        print("Error")





if __name__=='__main__':
    main()
