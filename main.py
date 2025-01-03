from random import \
    random  # Ejercicio 1 Crea una función que dada una cadena y una letra cuente cuantas veces aparece dicha letra
def contar_letras(cadena, letra):
    if(len(letra)>1):
       return "Error!"
    return cadena.count(letra)

# Ejercicio 2. Crea una función que dada una cadena determine si es un palíndromo o
# si no lo es (sin usar .reversed())
def palindromo(cadena):
    return cadena == cadena[::-1]
# Ejercicio 3. Crea una función que dada un cadena devuelva una lista con las
# siguientes cadenas:
# • Una con las 5 primeras letras
# • Una con las 5 últimas letras
# • Una con las letras impares
# • Una con la letras pares
# • Una con la cadena alrevés (sin usar .reversed())
def lista_cadenas(cadena):

    return cadena[:5],cadena[-5:], cadena[1::2], cadena[0::2], cadena[::-1]

# Ejercicio 4. Crea una función que dada una cadena determine si es un palíndromo o
# si no lo es (sin usar .reversed()) y usando slice notation

#El ejercicio 4 ya lo he echo el ejercicio 2 uso esa función para no repetir código


#Ejercicio 5. Crea una función que dada una cadena de texto encuentra la palabra de
# mayor longitud y la longitud de la misma

def palabra_mayor_longitud(cadena):
    cadena_lista = cadena.split()
    #Lo que hace este return es pilla el maximo en cadena lista ( que son los valores de cadena) y pilla la palabra mas larga
    #Y despues de la coma lo que se calcula es cuanta longitud tiene esa palabra
    return max(cadena_lista, key=len), len(max(cadena_lista, key=len))


# Ejercicio 6. Crea una función que dada una cadena de texto encuentre la palabra más
# larga y la más corta de dicha cadena
def palabra_mas_larga_mas_corta(cadena):
    cadena_lista = cadena.split()
    return max(cadena_lista, key=len), min(cadena_lista, key=len)


# Ejercicio 7. Crea una función que cuenta cuantas veces aparece una subcadena en
# un texto
def contar_subcadenas(cadena, subcadena):
    return cadena.count(subcadena)

# Ejercicio 8 Crea una función que cuenta cuantas veces aparece una subcadena en un
# texto y el índice de inicio y fin de cada una de las instancias de la subcadena dentro del texto.
def contar_subcadenas_y_indices(cadena, subcadena):
        return cadena.count(subcadena),cadena.index(subcadena),cadena.rindex(subcadena)


# Ejercicio 9. Crea una función que encuentre todas las palabras de un texto que
# empiezan y acaban por una misma subcadena dada
def encontrar_palabras(cadena:str, subcadena:str):
    resultado= []
    for subcaden in cadena.split(" "):
        if subcaden.startswith(subcadena) and subcaden.endswith(subcadena):
                resultado.append(subcaden)
    return resultado



# Ejercicio 10. Crea una función que reciba como parámetro un número entero y que
# devuelva un cadena que contenga la tabla de múltiplicar de dicho número
def tabla_multiplicar(numero):
    print("Esta tabla es del numero: ",numero)
    print(f"1 * {numero}: ",1*numero)
    print(f"2 * {numero}: ", 2 * numero)
    print(f"3 * {numero}: ", 3 * numero)
    print(f"4 * {numero}: ", 4 * numero)
    print(f"5 * {numero}: ", 5 * numero)
    print(f"6 * {numero}: ", 6 * numero)
    print(f"7 * {numero}: ", 7 * numero)
    print(f"8 * {numero}: ", 8 * numero)
    print(f"9 * {numero}: ", 9 * numero)
    print(f"10 * {numero}: ", 10 * numero)

print("Ejercicios de STRINGS")
print("--------------------------------------------------------")
print("Ejercicio 1: ")
print("La cantidad es:",contar_letras("Hola mundoooooo", "o"))
print("--------------------------------------------------------")
print("Ejercicio 2: ")
print("Es palindromo:",palindromo("radar"))
print("--------------------------------------------------------")
print("Ejercicio 3: ")
print("Lista de cadenas:",lista_cadenas("Hola mundooooo"))
print("--------------------------------------------------------")
print("Ejercicio 4: ")
print("Es palindromo:",palindromo("radara"))
print("--------------------------------------------------------")
print("Ejercicio 5: ")
print(palabra_mayor_longitud("Viva el vino de la vidaaaa"))
print("--------------------------------------------------------")
print("Ejercicio 6: ")
print(palabra_mas_larga_mas_corta("Viva e vino de la vidaaaa"))
print("--------------------------------------------------------")
print("Ejercicio 7: ")
print("La cantidad es:",contar_subcadenas("Hola mundo", "do"))
print("--------------------------------------------------------")
print("Ejercicio 8: ")
print("La cantidad(1),aparece(2),termina(3):",contar_subcadenas_y_indices("Ta vida es bella", "a"))
print("--------------------------------------------------------")
print("Ejercicio 9: ")
print("La cantidad es:",encontrar_palabras("Ta vidavi es villavi", "vi"))
print("--------------------------------------------------------")
print("Ejercicio 10: ")
tabla_multiplicar(12)
print("--------------------------------------------------------")

def calculaconpipo():
    print("Dime que quieres hacer: ")
    print("     (1) aprender las tablas de multiplicar")
    print("     (2) practicar las tablas de multiplicar")
    print("     (3) salir ")
    opcion = input()
    # el codigo tiene que repetirse hasta que se introduzca un tres
    while opcion != "3":
        if opcion == 0:
            print("Dime que quieres hacer: ")
            print("     (1) aprender las tablas de multiplicar")
            print("     (2) practicar las tablas de multiplicar")
            print("     (3) salir ")
            opcion = input()
        if opcion == "1":
            print("¿Qué tabla quieres aprender?")
            tabla = input()
            tabla_multiplicar(int(tabla))
            opcion = 0
        elif opcion == "2":
            acierto = 0
            falla = 0
            print("Muy bien, dime las tablas de multiplicar que quieres practicar: ")
            print("Separa el numero de la tabla con '-' , e.g: 1-5-7: ")
            tablas = input()
            # mete los numeros en una lista
            tablas_multi = []
            for tabla in tablas.split("-"):
                tablas_multi.append(int(tabla))

            print("Muy bien, ahora dime cuantos intentos quieres tener: ")
            intentos = int(input())
            print("LETS GOOOO, BOYYYYY:")
            for num_intento in range(intentos):
                num_random = int(random() * 10)
                # tabla_random tiene que ser int
                tabla_random = int(random() * (len(tablas_multi) - 1))
                respuesta_correcta = num_random * tablas_multi[tabla_random]
                print(num_random, "x", tablas_multi[tabla_random], "=")
                respuesta_usuario = int(input())
                if respuesta_usuario == respuesta_correcta:
                    print("YES!")
                    acierto = acierto + 1
                else:
                    print("Error! ", num_random, "x", tablas_multi[tabla_random], "=", respuesta_correcta, "y no", respuesta_usuario)
                    falla = falla + 1

            print("Has acertado ", acierto, " y has fallado ", falla, " de un total intentos: ", intentos,
                  " lo que hace una tasa de acierto del ", ((acierto / intentos) * 100), "%")
            print(("Pulse cualquier tecla para continuar..."))
            continuar = input()
            acierto = 0
            falla = 0
            # El codigo tiene que volver al principio
            opcion = 0
        elif opcion == "3":
            print("Adios")
            break
        else:
            print("No has elegido una opcion correcta")

print("Calcula con PIPO")
calculaconpipo()

print("--------------------------------------------------------")
print("Ahorcado")











