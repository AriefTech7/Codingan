print("=========format string=============")

nama ="gentar"
format = f"hello, {nama}"# f = format string
print(format)

#angka
angka = 25
format = f"angka = {angka}"
print(format)

#boolean
bool = False
format = f"boolean = {bool}"
print(format)

#bilangan ribuan
angka = 5000
format = f"ribuan = {angka:,}"
print(format)
angka = 5000000
format = f"jutaan = {angka:,}"
print(format)

#desimal
angka = 2023.22692
format = f"desimal = {angka:.3f}"
print(format)
angka = 2023.22692
format = f"desimal = {angka:09.2f}"
print(format)

#menampilkan tanda + dan -
angka_minus = -10
print(f"minus : {angka_minus:+d}" )
angka_plus = 10
print(f"minus : {angka_plus:+d}" )

#format persen
persen = 0.45
format_persen = f"persen = {persen:.0%}"
print(format_persen)

# melakukan operasi aritmatika dalam format string
harga = 50000
jumlah= 100
print(f"harga total = {harga*jumlah:,}")
harga = 100000
jumlah= 100
print(f"harga total = {harga*jumlah:,}")

#format angka lain
angka = 224
print(f"biner = {bin(angka)}")
print(f"octal = {oct(angka)}")
print(f"hexa = {hex(angka)}")

angka = 2007
tanggal = f"saya lahir 29 january {angka}"
print(tanggal)


#angka yang ribuan
ribu = 2000000
uang =f"uang cuma {ribu:,}"
print(uang)

# menampilkan beberapa dari belakang koma 
angka = 2007.21712 
tanggal = f"saya lahir 29 january {angka:1.1f}"
print(tanggal)

print( 4 > 3)

color = "blue"
lucky_number = 7

print(f"My favorite color is {color}, and my lucky number is {lucky_number}.")

value = 123.456789

# Mengatur presisi angka desimal
print(f"Value: {value:.2f}")  # Dua angka desimal

""""
Penjelasan:

{value:.2f} artinya:
- : memulai pengaturan format.
- .2 membatasi hingga 2 angka desimal.
- f berarti angka tersebut adalah angka floating-point.
"""

text = "Hello"

# Align kanan dengan lebar total 10
print(f"{text:>10}")

# Align kiri dengan lebar total 10
print(f"{text:<10}")

# Align tengah dengan lebar total 10
print(f"{text:^10}")

"""
Penjelasan:

 {text:>10}:
- > artinya teks rata kanan.
- 10 adalah panjang total string (termasuk padding).
 {text:<10}:
- < artinya teks rata kiri.
 {text:^10}:
- ^ artinya teks rata tengah.
"""