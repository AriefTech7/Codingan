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
#def gg(angka):
#    if angka % 2 ==0:
#        return "genap"
#    else:
#        return"ganjil"
    
    
##nomor = 10    
##bilangan = gg(nomor)
##print(f"bilangan {nomor} adalah bilangan {bilangan}")

#menghitung faktorial#
##def faktorial(n):
##    if n == 0 or n == 1:
##        return 1  # Faktorial 0 dan 1 adalah 1
##    else:
##        hasil = 1
##        for i in range(1, n + 1):
##            hasil *= i  # Perkalian bertahap
##        return hasil

# Memanggil fungsi
#angka = 8
#hasil = faktorial(angka)
#print(f"Faktorial dari {angka} adalah {hasil}")

### fungsi dengan argument (input)


def pembukaan(nama):
    print(f"selamat datang pada dunia wahai {nama}")

pembukaan("udin")

def operasi(x ,y):
    hasil = x + y
    print(f"ini adalah hasil {hasil}")

operasi(20 , 2)

def say_hi(list_kamyu):
    data = list_kamyu.copy()
    for elemen in data:
        print(f"kesukaan {elemen}")

list_kamyu = ["suka makan", "suka mobil", "suka duit"]
say_hi(list_kamyu)


## fungsi dengan return/respons

def kuadrat(angka):
    operasi = angka**2
    return operasi

print(kuadrat(3))


def mesin_minum(uang, choice):
    if choice == "coca cola":
        harga = 7000
    elif choice == "sprit":
        harga = 8000
    elif choice == "chimori":
        harga = 12000
    
    operasi_nya = uang - harga
    return operasi_nya

mulai_mesin = mesin_minum(20000, "chimori")
print(f"ini adalah kembaliannya {mulai_mesin}")


def toko(uang, barang, makanan):
    if barang == "sapu":
        harga_barang = 25000
    elif barang == "ember":
        harga_barang = 16000
    elif barang == "tong sampah":
        harga_barang = 19000
    elif barang == "gunting kuku":
        harga_barang = 7000
    else:
        return "barang tidak dikenali"


    if makanan == "sate":
        harga_makanan = 15000
    elif makanan == "kebab":
        harga_makanan = 10000
    elif makanan == "bakso":
        harga_makanan = 12000
    else:
        return "barang tidak dikenali"
    
    total = harga_barang + harga_makanan
    kembalian = uang - total

    return kembalian

beli = toko(100000, "sapu", "kebab")
print(beli)

## default argument fungsi

def say (nama= "kamyu"):
    print(f"hallo {nama}")

say("udin")
say()

def operasinya (angka_1=2, angka_2=3):
    hasil = angka_1 + angka_2
    return hasil

print(operasinya())

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())

def cek(angka):
    if angka % 2 == 0:
        print("genap")
    else:
        print("ganjil")

angka = (input("masukkan nomor kamu\t:"))
angka_int = int(angka)


print(f"ini adalah cek genap ganjilnya {cek(angka_int)}")

## type hints for function

# use case

'''
def function(parameter):
    hasil = parameter**2
    print(hasil)

function(1)
function("udin")
function(True)
'''


## *args for fungsi

def tambah(*data):
    if data == "1":
        print(f"data{data[0]}")
    else:
        print(f"data{data[1]}")
