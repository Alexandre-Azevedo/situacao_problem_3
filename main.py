import sys

#PARA EXECUTAR O SCRIPT BASTA PASSAR python3 main.py <numeros testados>
#EX:  python3 main.py 3 4 5 431

def impar_par(numeros):
    for i in numeros:
        if(i.isnumeric()):
            print(f'{i} é {"PAR" if int(i)%2 == 0 else "ÍMPAR"} \n')


if __name__ == '__main__':
    impar_par(sys.argv)