
from procesossepa import asignar_bic, extraerdatos, validador



def main():

    iban=input("Introduzca IBAN ")
    
    if validador(iban)==True:
        asignar_bic(iban)
        extraerdatos(iban)



if __name__ == "__main__":
    main()


