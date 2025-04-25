def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Memanggil fungsi untuk konversi suhu
print(f"25°C = {celsius_to_fahrenheit(2.3)}°F")
print(f"77°F = {fahrenheit_to_celsius(2.3)}°C")
print(f"25°C = {celsius_to_kelvin(2.3)}K")
print(f"298K = {kelvin_to_celsius(2.3)}°C")

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah",celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "Kelvin")
