#E3.2 · Carga iris.csv con DictReader, convierte las medidas a float y calcula la media por clase.

import csv
from pathlib import Path

RUTA = Path(__file__).parent / "Datos" / "iris.csv"

with open(RUTA, newline="") as f:
    filas = list(csv.DictReader(f))
#datos setosa
lpet_setosa=0
lsep_setosa=0
apet_setosa=0
asep_setosa=0
#datos versicolor
lpet_versicolor=0
lsep_versicolor=0
apet_versicolor=0
asep_versicolor=0
#datos virginica
lpet_virginica=0
lsep_virginica=0
apet_virginica=0
asep_virginica=0
#Contadores
contador_setosa=0
contador_versicolor=0
contador_virginica=0
Lineas= filas.count(any)

for fila in filas:
    fila["largo_pet"] = float(fila["largo_pet"])
    fila["ancho_pet"] = float(fila["ancho_pet"])
    fila["largo_sep"] = float(fila["largo_sep"])
    fila["ancho_sep"] = float(fila["ancho_sep"])

    
    if fila["clase"] == "setosa":
        contador_setosa= contador_setosa + 1
        lpet_setosa= fila["largo_pet"] + lpet_setosa
        lsep_setosa= fila["largo_sep"] + lsep_setosa
        apet_setosa= fila["ancho_pet"] + apet_setosa
        asep_setosa= fila["ancho_sep"] + asep_setosa
    if fila["clase"] == "versicolor":
        contador_versicolor= contador_versicolor + 1
        lpet_versicolor= fila["largo_pet"] + lpet_versicolor
        lsep_versicolor= fila["largo_sep"] + lsep_versicolor
        apet_versicolor= fila["ancho_pet"] + apet_versicolor
        asep_versicolor= fila["ancho_sep"] + asep_versicolor
    if fila["clase"] == "virginica":
        contador_virginica= contador_virginica + 1
        lpet_virginica= fila["largo_pet"] + lpet_virginica
        lsep_virginica= fila["largo_sep"] + lsep_virginica
        apet_virginica= fila["ancho_pet"] + apet_virginica
        asep_virginica= fila["ancho_sep"] + asep_virginica

print(f"Medias")
print("=======")
print("                   Setosas                 Virginicas               Versicolor")
print(f"Longitud Petalo:    {lpet_setosa / contador_setosa:.2f}                    {lpet_virginica/contador_virginica:.2f}                     {lpet_versicolor/contador_versicolor:.2f}")
print(f"Ancho Petalo:       {apet_setosa / contador_setosa:.2f}                    {apet_virginica/contador_virginica:.2f}                     {apet_versicolor/contador_versicolor:.2f}")
print(f"Longitud Sepalo:    {lsep_setosa / contador_setosa:.2f}                    {lsep_virginica/contador_virginica:.2f}                     {lsep_versicolor/contador_versicolor:.2f}")
print(f"Ancho Sepalo:       {asep_setosa / contador_setosa:.2f}                    {asep_virginica/contador_virginica:.2f}                     {asep_versicolor/contador_versicolor:.2f}")



#########################################################################################################

#Correción





