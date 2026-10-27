#Víctor Daniel Rodríguez Figueroa
#3. Dado un conjunto data de observaciones, ajusta una normal usando la media y desviación poblacional del conjunto. Crea una función normal_tasks(data, x, p) que:
#Cree un NormalDist ajustado a data.
#Calcule la probabilidad P(X <= x) (CDF).
#Calcule el percentil (inversa) inv_cdf(p): el valor y tal que P(X <= y) = p.
#Devuelva además el z-score de x usando (x - mean)/stdev.
#Usa statistics.NormalDist.

import statistics
from statistics import NormalDist

def AjusteNormal (data, x, p) -> dict:
    media = statistics.mean(data)
    desviacion = statistics.pstdev(data)
    
    dist = NormalDist(mu=media, sigma=desviacion)

    cdf = dist.cdf(x)

    inv_cdf = dist.inv_cdf(p)

    z_score = (x - media) / desviacion

    return {
        "dist": dist,
        "cdf": cdf,
        "inv_cdf": inv_cdf,
        "z_score": z_score
    }

resultado=AjusteNormal([10,2,3,5,57,123,567,78],1,0.8)

print(resultado)
