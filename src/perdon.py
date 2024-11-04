

def serie_num(num: int, secuencia: str):
    for i in range(num, -1, -1):
        suma = total(i, num)
        secuencia = str(i) + " + " + secuencia
        print(f"{i} => {secuencia} = {str(suma)}")
    

def total (i, num):
    for j in range(i, num):
        num += j
    return num


def main():
    secuencia = ""
    numero = input("numero ")
    numero = int(numero)
    serie_num(numero, secuencia)


if __name__ == "__main__":
    main()