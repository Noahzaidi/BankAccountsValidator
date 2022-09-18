
import pandas as pd

from numpy import true_divide


def validador(my_iban):
    
    def validate_digitos(my_iban):
        num_caracteres_lista = list(my_iban)
        if(len(num_caracteres_lista)<15):
            return False
        else:
            return True

    diccionario_SEPA = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20,
                "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31,
                "W": 32, "X": 33, "Y": 34, "Z": 35,
                "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    letters = {ord(k): str(v) for k, v in diccionario_SEPA.items()}


    def chech_validador_iban(iban):
        
        try:
            ceros_iban = iban[:2] + '00' + iban[4:]
            iban_invertido = ceros_iban[4:] + ceros_iban[:4]
            iban_numerado = iban_invertido.translate(letters)

            try:
                verificacion = 98 - (int(iban_numerado) % 97)

                if verificacion < 10:
                    verificacion = '{:02}'.format(int(verificacion))
                return verificacion
            except:
                print ("Iban Incorrecto")
                return False

        except:
            print ("Iban Incorrecto")
            return False 
            


    def validate_iban(iban):
        
        iban_invertido = iban[4:] + iban[:4]
        iban_numerado = iban_invertido.translate(letters)

        return int(iban_numerado) % 97

    if validate_digitos(my_iban):
        
        try:
        
            if chech_validador_iban(my_iban) == int(my_iban[2:4]):
                if validate_iban(my_iban) == 1:


                    print("Su Iban es correcto") 
                    return True
                            
                else:
                    print("Iban Incorrecto")
                    return False
                        
            else:
                print("Iban Incorrecto")
                return False

        except:
            print("IBAN incorrecto")   
            return False
    else:
        print("Numero de carácteres IBAN incorrecto")      
        return False


def asignar_bic(iban):

    # Creacion del diccionario
    bics = pd.read_csv('BIC.csv', sep=';')

    def arreglar_ceros(numero):
        if(len(list(str(numero)))==1):
            return '000' + str(numero)
        if(len(list(str(numero)))==2):
            return '00' + str(numero)
        if(len(list(str(numero)))==3):
            return '0' + str(numero)
        if(len(list(str(numero)))==4):
            return str(numero)

    nuevo_cod = [arreglar_ceros(x) for x in bics['COD']]
    nuevo_bic = [x for x in bics['BIC']]
    nom_bic=  [x for x in bics['NOM']]

    dict_list = dict(zip(nuevo_cod, nuevo_bic))
    dict_nom= dict(zip(nuevo_bic,nom_bic, ))

    iban_list = list(iban)
    cod = str(iban_list[4]) + str(iban_list[5]) + str(iban_list[6]) + str(iban_list[7])
    


    for clave in dict_list:
        
        if(clave == cod):
            bicx=dict_list[clave]
            print("BIC: "+ bicx)

            for x in dict_nom:

                if bicx==x:
                    print ("BANCO: " + dict_nom[x])

def extraerdatos(iban):

    print("Código de país es: "+ (iban[0:2]))
    print("Dígitos de control: "+ (iban[2:4]))
    print("Código de banco: "+ (iban[4:8]))
    print("Código de oficina: "+ (iban[8:12]))
    print("Dígitos de control de cuenta bancaria: "+ (iban[12:14]))
    print("Número de cuenta bancaria: "+ (iban[14:24]))










            



