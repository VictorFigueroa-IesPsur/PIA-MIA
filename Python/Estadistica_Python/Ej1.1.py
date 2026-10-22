#Víctor Daniel Rodríguez Figueroa
#1. Crea five_number_summary(nums) que devuelva (min, Q1, median, Q3, max) usando statistics. Usa statistics.quantiles para los cuartiles y statistics.median para la mediana.

import statistics

nums=[]

def five_number_summary(nums):

    if len(nums) == 0:
        return ("Ingrese algun numero de argumentos")
    
    sorted_nums=sorted(nums)

    valor_min=sorted_nums[0]
    valor_max=sorted_nums[-1]
    q1=statistics.quantiles(sorted_nums,n=4)[0]
    mediana=statistics.median(sorted_nums)
    q3=statistics.quantiles(sorted_nums,n=4)[2]

    print(f"min:{valor_min}")
    print(f"1ºQ: {q1},")
    print(f"mediana: {mediana}")
    print(f"3ºQ: {q3}")
    print(f"max: {valor_max}")


five_number_summary([2,3,3,5,6,7,7,7,8,7,7,5,2,5,5,3,4,6,6,7,6,6,4,4,2,5])


