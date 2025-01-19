print("=========function=============")

#def sapa():
#   print("Halo, selamat belajar python !")

#sapa()
#sapa()

#parameter
#def nama_sapa(nama):
#   print(f"halo, {nama} selamat belajar python!")


#nama_sapa("wahyu")
#nama_sapa("arif")

# Definisi fungsi
#def hitung_luas_persegi(panjang, lebar):
#    # Menghitung luas
#    luas = panjang * lebar
 #   return luas  # Mengembalikan hasil perhitungan

# Memanggil fungsi
#hasil = hitung_luas_persegi(5, 3)  # Memberi nilai panjang=5 dan lebar=3
##print(f"Luas persegi panjang adalah: {hasil}")

#def tambah(a, b):
#    hasil = a + b
#    return hasil  # Mengembalikan hasil penjumlahan

# Memanggil fungsi dan menyimpan hasilnya di variabel 'total'
#total = tambah(3, 5)
#print(total)  # Output: 8#


#fungsi bilangan genap dan ganjil#
def gg(angka):
    if angka % 2 ==0:
        return "genap"
    else:
        return"ganjil"
    
    
nomor = 10    
bilangan = gg(nomor)
print(f"bilangan {nomor} adalah bilangan {bilangan}")

#menghitung faktorial#
def faktorial(n):
    if n == 0 or n == 1:
        return 1  # Faktorial 0 dan 1 adalah 1
    else:
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i  # Perkalian bertahap
        return hasil

# Memanggil fungsi
angka = 8
hasil = faktorial(angka)
print(f"Faktorial dari {angka} adalah {hasil}")
