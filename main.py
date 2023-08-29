import sys


def impar_par(numeros):
    for i in numeros:
        if(i.isnumeric()):
            print(f'{i} é {"PAR" if int(i)%2 == 0 else "ÍMPAR"} \n')


if __name__ == '__main__':
    impar_par(sys.argv)