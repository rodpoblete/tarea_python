"""
* Los datos se ingresarán de forma que la fecha (año/mes/día) va siempre incrementándose, nunca decreciendo.
* Las frutas posibles de ingresar son siempre "naranja", "manzana", "pera", "kiwi", ninguna otra
* El último número de cada línea es la cantidad vendida de la fruta (en esa fecha).
* Para terminar el ingreso de datos se debe ingresar una línea en blanco (o sea, solo presionar enter).


----------------------------------------------------------
Ingrese datos: 2000 3 3 manzana 1
Ingrese datos: 2000 3 3 kiwi 5
----------------------------------------------------------

Las estadísticas que DonJuan quiere obtener son:
* Por cada año ingresaso, la cantidad de "naranja", "manzana", "pera", "kiwi" que ha vendido.
* Por cada mes ingresado, la cantidad de "naranja", "manzana", "pera", "kiwi", que han vendido
* La cantidad total de "naranja", "pera", "kiwi", vendida, mostrando el total y porcentajes.

----------------------------------------------------------
> Total mes 1/2001 n= 8 m= 10 p= 0 k= 8
> Año 2001 n= 8 m = 10 p= 0 k= 8
> Total Vendido: 85
> Total Naranjas: 17 20.0 %
> Total Manzanas: 22.25.888888888889 %
> Total Peras: 33.38.343424242434 %
> Total kiwis: 13 15.121313123123123 %
__________________________________________________________
"""


def estadistica():

    manzanas, peras, kiwis, naranjas = 0, 0, 0, 0
    anio, mes = 0, 0

    while True:
        user_input = input("Ingrese Datos: ").split()

        if not user_input:
            break

        # 0: año
        # 1: mes
        # 2: día
        # 3: fruta
        # 4: cantidad vendida

        if user_input[3] == "manzana":
            manzanas += int(user_input[4])
        elif user_input[3] == "pera":
            peras += int(user_input[4])
        elif user_input[3] == "kiwi":
            kiwis += int(user_input[4])
        elif user_input[3] == "naranja":
            naranjas += int(user_input[4])

        anio, mes = user_input[0], user_input[1]

    print(f"año: {anio} mes:{mes}")


if __name__ == "__main__":
    estadistica()
