"""
Lee ventas_sucio.csv, que contiene filas con campos vacíos, números con coma y fechas mal formadas.
1 · Valida cada fila y convierte los tipos; captura ValueError sin abortar el proceso.
2 · Acumula las filas rechazadas con su número de línea y el motivo.
3 · Escribe ventas_limpio.csv con las filas válidas y errores.json con el informe de rechazos.
4 · Reparte el código en carga.py, limpieza.py e informe.py, con main.py como punto de entrada.
"""