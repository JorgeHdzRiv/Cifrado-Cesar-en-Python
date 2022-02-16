# Cifrado Cesar Python
## Que es?
La acción de un cifrado César es reemplazar cada letra de texto plano por una diferente, un número fijo de lugares en el alfabeto.

![cifrado](./images/cifrado.png)

El cifrado ilustrado aquí utiliza un desplazamiento a la izquierda de tres, de modo que (por ejemplo) cada aparición de E en el texto plano se convierte en B en el texto cifrado.

## Codigo encriptacion

Para nuestro programa elaboraremos un cifrado sencillo que solo recorra una sola letra, cada letra del mensaje se reemplaza por su consecuente más cercano (A se convierte en B, B se convierte en C, y así sucesivamente). La única excepción es Z, la cual se convierte en A.

Se utilizaran los siguientes supuestos:
* Solo acepta letras latinas (nota:los romanos no usaban espacios en blanco ni dígitos).

* Todas las letras del mensaje están en mayúsculas (nota: los romanos solo conocían las mayúsculas).

### Codigo
* [encriptado](../Cifrado_Cesar/src/encriptado.py)
