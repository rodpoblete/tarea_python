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
* Por cada año ingresado, la cantidad de "naranja", "manzana", "pera", "kiwi" que ha vendido.
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
    """Función que retorna las cantidad de frutas vendidas por período y sus estadísticas"""

    # Inicializamos las variables que contienen la suma de las frutas
    manzanas, peras, kiwis, naranjas = 0, 0, 0, 0
    # Inicializamos variables que guardaran último año que ingreso el usuario por cada iteración del while
    ultimo_anio, ultimo_mes, ultimo_dia = 0, 0, 0

    while True:
        # Capturamos el ingreso del usuario y con el método split lo separamos en una lista
        user_input = input("Ingrese Datos: ").split()

        # Cada indice de la lista contiene el siguiente valor
        # 0: año
        # 1: mes
        # 2: día
        # 3: fruta
        # 4: cantidad vendida

        # Se valida si el usuario no ingresa nada y presiona enter el programa se interrumpe y se muestran las estadisticas globales
        if not user_input:
            print(
                f"Total mes {ultimo_mes}/{ultimo_anio} n= {naranjas} m= {manzanas} p= {peras} k= {kiwis}"
            )
            print(
                f"Año: {ultimo_anio} n= {naranjas} m= {manzanas} p= {peras} k= {kiwis}"
            )
            print(f"Total Vendido: {total_vendido}")
            print(
                f"Total Naranjas: {naranjas} {round((naranjas/total_vendido) * 100), 1} %"
            )
            print(f"Total Manzanas: {manzanas} {(manzanas/total_vendido) * 100} %")
            print(f"Total Peras: {peras} {(peras/total_vendido) * 100} %")
            print(f"Total Kiwis: {kiwis} {(kiwis/total_vendido) * 100} %")
            break

        # Asignamos nombres a los elementos de la lista para que sea más sencillo trabajar con ellos. (cada nombre es representativo a su valor)
        anio = user_input[0]
        mes = user_input[1]
        dia = user_input[2]
        fruta = user_input[3]
        cantidad_vendida = int(user_input[4])

        # Con estas condicionales evaluamos cada fruta que ingresa el usuario y la vamos sumando. Si ingresa una distinta se mostrará el texto de la sentencia else
        if fruta == "manzana":
            manzanas += cantidad_vendida
        elif fruta == "pera":
            peras += cantidad_vendida
        elif fruta == "kiwi":
            kiwis += cantidad_vendida
        elif fruta == "naranja":
            naranjas += cantidad_vendida
        else:
            print("Ingrese sólo la fruta en venta")

        # Comparamos si ha cambiado el mes o año para mostrar por pantalla la cantidad de fruta vendida en ese periodo (en el mes o en el año)
        if ultimo_anio == 0 or ultimo_mes == 0:
            pass  # con la sentencia pass nos saltamos este if y continuamos con los de más abajo
        elif ultimo_anio != anio:
            # Año 2001 n= 8 m = 10 p= 0 k= 8
            print(
                f"Año: {ultimo_anio} n= {naranjas} m= {manzanas} p= {peras} k= {kiwis}"
            )
        elif ultimo_mes != mes:
            # Total mes 1/2001 n= 8 m= 10 p= 0 k= 8
            print(
                f"Total mes {ultimo_mes}/{ultimo_anio} n= {naranjas} m= {manzanas} p= {peras} k= {kiwis}"
            )

        # Sumamos todas las frutas vendidas
        total_vendido = manzanas + peras + kiwis + naranjas

        # Actualizamos los años con el ultimo ingresado por el usuario para una nueva iteración
        ultimo_anio, ultimo_mes = anio, mes


if __name__ == "__main__":
    estadistica()
