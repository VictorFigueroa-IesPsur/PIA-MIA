#Víctor Daniel Rodríguez Figueroa
#2. Escribe compare_means(nums) que reciba una lista de números positivos y devuelva un dict con: 
#media aritmética (mean), media armónica (harmonic_mean), media geométrica (geometric_mean), desviación poblacional (pstdev) y coeficiente de variación (cv = pstdev/mean). 

import statistics

def compare_means(nums):

    sorted_nums=sorted(nums)
    if any(nums) < 0 :
        return("Solo numeros positivos")

    if len(sorted_nums) == 0:
        return ("Ingrese un numero de elementos")

    media= statistics.mean(sorted_nums)
    media_har= statistics.harmonic_mean(sorted_nums)
    media_geo= statistics.geometric_mean(sorted_nums)
    desviacion= statistics.pstdev(sorted_nums)
    cv= desviacion/media

    return {
        "media":media,
        "armonica":media_har,
        "Geometrica":media_geo,
        "desviacion":desviacion,
        "variacion":cv
    }

datos=compare_means([2,3,3,5,6,7,7,7,8,7,7,5,2,5,5,3,4,6,6,7,6,6,4,4,2,5])

print(datos)