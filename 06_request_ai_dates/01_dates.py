# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale # Para establecer la localización (traduce meses, días al idioma local)

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

# Operaciones con fechas (sumar/restar días, minutos, etc.)
yesterday = datetime.now() - timedelta(days=1)
print("Ayer fue:", yesterday.strftime("%d/%m/%Y"))

tomorrow = datetime.now() + timedelta(days=1)
print("Mañana será:", tomorrow.strftime("%d/%m/%Y"))

# Obtener componentes individuales de una fecha
year = fecha_actual.year
month = fecha_actual.month
day = fecha_actual.day
hour = fecha_actual.hour
minute = fecha_actual.minute

print("Año:", year)
print("Mes:", month)
print("Día:", day)
print("Hora:", hour)
print("Minuto:", minute)

# Calcular la diferencia entre dos fechas
date_one = datetime.now()
date_two = datetime(2004, 12, 23)
diferencia = date_one - date_two
print("Diferencia entre fechas:", diferencia)

# Establecer la localización para formatear fechas en español
locale.setlocale(locale.LC_TIME, 'es_CO.UTF-8')  # LC_TIME -> local processing time
# Formatear fecha en español
fecha_formateada_es = fecha_actual.strftime("%A, %d de %B de %Y")
print("Fecha actual formateada en español:", fecha_formateada_es)
