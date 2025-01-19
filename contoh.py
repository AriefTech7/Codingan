#latihan kalkulator sederhana#

#angka1 =int(input("Masukkan angka pertama:"))
#operasi = input("Masukan operasi (+, -, *, /) :")
#angka2 =int(input("Masukkan angka kedua:"))

#if operasi == "+":
#    hasil = angka1 + angka2
#    print(f"Hasil : {angka1} + {angka2} = {hasil}")
#elif operasi == "-":
#    hasil = angka1 - angka2
#   print(f"Hasil : {angka1} - {angka2} = {hasil}")
#elif operasi == "*":
#    hasil = angka1 * angka2
#    print(f"Hasil : {angka1} * {angka2} = {hasil}")
#elif operasi == "/":
#  if angka2 != 0:
 #   hasil = angka1 / angka2
#    print(f"Hasil : {angka1} / {angka2} = {hasil}")
# #   print("Kesalahan : tidak dapat dibagi dengan nol!")
#else: 
 #  print("Operasi tidak dikenali")

#latihan menentukan tipe data#

#data =   input("Masukkan data:")
#if data.isdigit():
#   tipe_data = type(int(data))
#elif data.replace(".", "", 1).isdigit() and data.count(".") < 2:
#   tipe_data = type(float(data))
#else:
#   tipe_data = type(data)

#print (f"Anda memasukkan data bertipe {tipe_data}")

#klasifikasi umur#

#usia = int(input("Masukkan usia anda:"))
#if usia <= 12:#
#    print("Anda termasuk kategori Anak-anak")
#elif usia <= 18:
#    print("Anda termasuk kategori Remaja")
#elif usia <= 60:
#    print("Anda termasuk kategori Dewasa")
#else:   
#    print("Anda termasuk kategori Lansia")

#ganjil & genap#

#bilangan = int(input("Masukkan sebuah angka:"))

#if bilangan % 2 == 0:
#    print(f"Angka {bilangan} adalah bilangan ganjil")
#else:
#    print(f"Angka {bilangan} adalah bilangan genap")

#penentu kelulusan#

nilai = int(input("Masukkan nilai anda:"))

if nilai >= 75:
    print("Status : Lulus")
elif nilai >= 50:
    print("Status : Remedial")
elif nilai <= 50:
    print("Status : Gagal")