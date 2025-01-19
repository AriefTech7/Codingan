print("=========if, elif & else statement=============")

#nilai = int(input("masukan nilai mtk:"))

#if nilai >= 90 : 
#    print ("kamu yang terbaik")
#    print("selamat, anda lulus")
#else:
#    print(f"anda tidak lulus dengan nilai ini {nilai}")
#    print("kamu mah main terus")


#nama = input("nama kamu siapa nisch :")

#if nama == "wahyu" :
#    print("kamu si manis")
#    print("kamu paling santun dan sopan")
#else:
#    print(f"ahhh kok {nama} sih")

#menentukan angka positif, negatif atau nol#

#angka = int(input("masukkan sebuah angka :"))
#if angka >= 1:
#    print("angka tersebut adalah positif")
#elif angka == 0:
#    print("angka tersebut adalah nol")
#else:
#    print("angka tersebut negatif")

#menentukan nilai huruf berdasarkan skor#

#skor = int(input("masukkan skor ujian:"))
#if skor >= 95:
#    print("nilai huruf : A ++")
#elif skor  >= 90:
#    print("nilai huruf: A")
#elif skor >= 80:
#    print("nilai  huruf: B")
#elif skor >= 70:
#    print("nilai huruf: C")
#elif skor >= 60:
#    print("nilai huruf : D")
#else:
#    print("nilai huruf : F")

#menentukan bilangan genap atau ganjil#

#bilangan = int(input("masukkan bilangan :"))
#if bilangan % 2 == 0: # % = operasi modulus -> operasi yang menghasilkan sisa pembagian dari 2 angka
#    print(f"bilangan {bilangan} adalah genap")
#else:
#   print(f"bilangan {bilangan} adalah ganjil")

#menentukan harga tiket berdasarkan usia#

#bioskop = int(input("masukkan usia :"))
#if bioskop <= 5:
#    print("harga tiket : gratis")
#elif bioskop <= 17:
#    print("harga tiket : Rp20.000")
#else:
#   print("harga tiket : Rp50.000")

#permainan tebak warna#

#warna = input("tebak warna fav saya:")
#if warna == "ungu":
#    print("Benar!")
#else:
#    print("coba lagi!")

#menentukan tahun kabisat#

#kabisat  = int(input("masukkan tahun :"))
#if kabisat % 4 == 0:
#    print("tahun tersebut adalah tahun kabisat")
#else:
#    print("coba lagi!")

#Game batu, gunting, kertas#

#game = input("masukkan pilihan anda (batu, gunting, kertas):")
#bot = "batu"

#if game == bot:
#    print(f"bot memilih : {bot}. hasil : seri!")
#elif (game == "batu" and bot == "gunting") or (game == "gunting" and bot == "kertas") or (game == "kertas" and bot == "batu"):
#    print(f"bot memilih: {bot}. anda menang!")
#else:
#    print(f"bot memilih: {bot}. anda kalah!")

#data = (input("masukkan nama kamu:"))

#if data == "udin":
#    print("halo udin")
#elif data == "marcus":
 #   print("halo marcis")
#elif data == "wahyu":
#    print("halo wahyuuu!")
#else:
#    print("nama kamu tidak ada pada database")

username = input("masukan username:")
password = int(input("masukkan password:"))

if username == "admin" or password == "098":
    print("Login berhasil!")
else:
    print("Login gagal.")

x = float(input("masukkan angka : "))
if (x>0 and x<5) or (x>8 and x<11) :
	print(True)
else :
	print(False)

