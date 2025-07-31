from datetime import datetime

birth = input("Enter birth date (DD/MM/YYYY HH:MM:SS): ")
birth_date = datetime.strptime(birth, "%d/%m/%Y %H:%M:%S")
now = datetime.now()

age = now - birth_date

years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30
days = remaining_days % 30
hours = age.seconds // 3600
minutes = (age.seconds % 3600) // 60
seconds = age.seconds % 60

print(f"Your exact age is: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
