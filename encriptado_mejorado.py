#Texto para encriptacion
texto = input("Ingresa tu mensaje: ")

#Iniciar la variable cambio
cambio = 0

#Lista opciones recorrido
opciones = ['izq','der']

#Tratamiento de errores

while cambio == 0:
    try:
        cambio = int(input("Ingrese el valor de cambio del cifrado del 1 al 25: "))
        recorrido = input("Ingrese hacia donde se hara el recorrido izq o der: ")
        if cambio not in range(1,26):
            raise ValueError
    except ValueError:
        cambio = 0
    if cambio == 0:
        print("Valor de cambio invalido intente de nuevo")
    if recorrido not in opciones:
        print("Recorrido incorrecto intente de nuevo")
        recorrido = input("Ingrese hacia donde se hara el recorrido izq o der: ")
        
cifrado = ''

for char in texto:
    #Comprobar si es una letra
    if char.isalpha():
        #Cambiamos el codigo 
        if recorrido == 'der':
            codigo = ord(char)+cambio
        else:
            codigo = ord(char)-cambio
        #Verificar si es mayusucula o minuscula y encontrar codigo
        if char.isupper():
            inicial = ord('A')
        else:
            inicial = ord('a')
        #Correcion
        codigo -= inicial
        codigo %= 26
        #Agregando caracter codificado al mensaje
        cifrado += chr(inicial+codigo)
    else:
        #Agregar caracter original al mensaje
        cifrado += char

print(cifrado)