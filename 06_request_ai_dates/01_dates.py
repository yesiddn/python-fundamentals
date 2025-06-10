# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta

# Obtener la fecha y hora actual
fecha_actual = datetime.now()
print("Fecha y hora actual:", fecha_actual)

# Crear una fecha específica
fecha_especifica = datetime(2023, 10, 6, 12, 0, 0) # Año, mes, día, hora, minuto, segundo
print("Fecha y hora específica:", fecha_especifica)

# Formatear fechas
# strftime() se le pasa el objeto datetime y un formato (ver documentación)
format_date = fecha_actual.strftime("%d/%m/%Y")
print("Fecha actual formateada:", format_date)
