from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# 1. Crea una variable con la fecha y hora actual.

now = datetime.now()

# 2. Imprime solo el año, mes y día de la fecha actual.

today = (f"Hoy es {now.day} del {now.month} del año {now.year}.")
print(today)

# 3. Crea una fecha específica: 25 de diciembre de 2025 y muéstrala.

date_2025 = datetime(2025, 12, 25)
print(date_2025)

# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.

start_time = time(12, 15, 26)
print(start_time)

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.

date_2026 = datetime(2026, 1, 1)

diff = date_2026 - now
print(diff)

# 6. Crea una función que reciba una fecha y devuelva su timestamp.

def get_timestamp(date):
  return (date.timestamp())

print(get_timestamp(now))

# 7. Suma 30 días a la fecha actual usando timedelta.

thirty_days_from_now = now + timedelta(days = 30)
print(thirty_days_from_now)

# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 días como simplificación).

thirty_days_from_2025 = date_2025 + timedelta(days = 30)
print(thirty_days_from_2025)

# 9. Compara dos fechas y muestra cuál es anterior.

def compare_dates(date1, date2):
  print(date1, date2)
  if (date1 > date2):
    print(f"{date1} es posterior a {date2}")
  elif (date1 < date2):
    print(f"{date1} es anterior a {date2}")
  else: print("Las fechas deben ser diferentes")

compare_dates(now, thirty_days_from_now)

# 10. Crea una lista con varias fechas y ordénalas cronológicamente.

dates_list = [now, date_2026, date_2025]
dates_list.sort()
for date in dates_list:
    print(date.strftime("%Y-%m-%d")) # .strftime sirve para dar formato a un objeto date