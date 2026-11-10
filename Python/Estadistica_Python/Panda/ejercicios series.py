import numpy as np
import pandas as pd

def t(n):
    print(f"\n=== Ejercicio {n} ===")

# 1
t(1); s = pd.Series([10, 20, 30, 40, 50]); print(s)
# 2
t(2); print(s.tolist())
# 3
t(3)
a = pd.Series([2, 4, 6]); b = pd.Series([1, 2, 3])
print(a + b, a - b, a * b, a / b, sep="\n")
# 4
t(4); print(a > b, a == b, a <= b, sep="\n")
# 5
t(5); print(pd.Series({"a": 100, "b": 200, "c": 300}))
# 6
t(6); print(pd.Series(np.array([5, 6, 7, 8])))
# 7
t(7)
s7 = pd.Series(["1", "2", "3"]); print(s7.dtype)
s7 = s7.astype(int); print(s7.dtype)
# 8
t(8)
lista = pd.Series([["Colombia", "Perú", "Argentina"], ["Bolivia", "Uruguay"], ["Chile"]])
print(lista.explode(ignore_index=True))
# 9
t(9); print(pd.Series([3, 1, 2]).sort_values())
# 10
t(10)
s10 = pd.Series([1, 2, 3])
s10 = pd.concat([s10, pd.Series([4, 5])], ignore_index=True); print(s10)
# 11
t(11); n = pd.Series([1, 5, 8, 12, 15]); print(n[n > 6])
# 12
t(12); s12 = pd.Series([1, 2, 3], index=["a", "b", "c"]); print(s12.reindex(["c", "a", "b"]))
# 13
t(13); d = pd.Series([2, 4, 4, 4, 5, 5, 7, 9]); print(d.std(), d.mean())
# 14
t(14); print(d.min(), d.max())
# 15
t(15); print(d.describe())
# 16
t(16); print("Pares:\n", d[d % 2 == 0], "\nImpares:\n", d[d % 2 != 0])
# 17
t(17); print(d.to_numpy(), type(d.to_numpy()))
# 18
t(18); sn = pd.Series([1, np.nan, 3]); print(sn.isnull().any(), sn.hasnans)
# 19
t(19); print(d.nbytes, "bytes")
# 20
t(20); print(sn.dropna())
# 21
t(21); print(pd.Series([-3, 2, -1]).abs())
# 22
t(22); print(d.agg(["min", "max", "mean", "sum"]))
# 23
t(23); print(sn.fillna(0))
# 24
t(24); print(d.head(3), d.tail(3), sep="\n")
# 25
t(25); print(d.where(d > 4, 0))   # mantiene los que cumplen, reemplaza el resto
# 26
t(26); print(d[d > 4])
# 27
t(27); print(d.value_counts())
# 28
t(28); print(d.to_csv(index=False))
# 29
t(29); print(d.apply(lambda x: x ** 2))
# 30
t(30); print(d[d.between(4, 7)])
# 31
t(31); print(d.drop_duplicates())
# 32
t(32); print(pd.Series([1, 2, 3]).equals(pd.Series([1, 2, 3])),
pd.Series([1, 2, 3]).equals(pd.Series([1, 2, 4])))
# 33  (método del rango intercuartílico, IQR)
t(33)
datos = pd.Series([10, 12, 11, 13, 12, 11, 10, 95, 12, -40])
q1, q3 = datos.quantile(0.25), datos.quantile(0.75)
iqr = q3 - q1
print(datos[datos.between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)])
# 34
t(34)
fechas = pd.date_range("2021-01-01", periods=36, freq="MS")
ventas = pd.Series(np.random.default_rng(0).integers(100, 500, 36), index=fechas)
print(ventas.groupby(ventas.index.month).mean())
