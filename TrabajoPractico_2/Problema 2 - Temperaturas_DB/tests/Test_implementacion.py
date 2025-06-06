from modules.Implementacion import*

db = Temperatura_DB() # Crear una instancia de la base de datos de temperaturas

# Guardar algunas temperaturas con fechas específicas
db.guardar_temperatura(25.5, "01/01/2023")
db.guardar_temperatura(27.8, "02/01/2023")
db.guardar_temperatura(30.2, "03/01/2023")
db.guardar_temperatura(22.1, "04/01/2023")
db.guardar_temperatura(24.0, "05/01/2023")
db.guardar_temperatura(26.5, "06/01/2023")
db.guardar_temperatura(28.3, "07/01/2023")
db.guardar_temperatura(29.9, "08/01/2023")
db.guardar_temperatura(23.4, "09/01/2023")
db.guardar_temperatura(21.0, "10/01/2023")

# Se muestran las temperaturas guardadas
print("Temperaturas guardadas:")
db.devolver_todas_temperaturas()

# Consulta en fecha específica
fecha = "08/01/2023"
print(f"Temperatura en la fecha {fecha}:", db.devolver_temperatura(fecha), '°C')

# Consultas en rango de fechas
fecha_inicio = "04/01/2023"
fecha_fin = "09/02/2023"
print("Temperaturas en rango:")
db.devolver_temperaturas(fecha_inicio, fecha_fin)
print("Temperatura máxima en rango:", db.max_temp_rango(fecha_inicio, fecha_fin), '°C')
print("Temperatura mínima en rango:", db.min_temp_rango(fecha_inicio, fecha_fin), '°C')
print("Temperaturas extremas en rango:", db.temp_extemos_rango(fecha_inicio, fecha_fin), '°C')

# Consultar cantidad de muestras
print("Cantidad de muestras:", db.cantidad_muestras())

# Borrar algunas temperaturas
db.borrar_temperatura("08/01/2023")
db.borrar_temperatura("04/01/2023")

# Se muestran las temperaturas después de borrar algunas
print("Temperaturas después de borrar:")
db.devolver_todas_temperaturas()

# Cantidad de muestras después de borrar
print("Cantidad de muestras después de borrar:", db.cantidad_muestras())