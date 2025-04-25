## dictionary -> memiliki workflow yang mirip dengan array, sehingga biasa disebut asosiatif array 
# dan dictionary terdiri dari key and value. Untuk mengakses dictionary kita tinggal memanggil key 
# untuk menampilkan value##

import datetime


sekolah = {
    'smp1':'latifa',
    'smp8':'timo',
    'smklabor':'arif',
    'smk':'dewe'
}

sekolah['smp7'] = 'fikri'
print(sekolah)
print(sekolah['smklabor'])


# operasi dictionary


kota = {
    'riau':'pekanbaru',
    'jakarta':'jakarta pusat',
    'sumatra utara':'medan',
    'jateng':'bandung'
}

# menambahkan elemen pada dictionary
kota['china'] = 'shanghai'
print(kota) 
print(kota['jakarta'])

# mengukur panjang data dictionary kota
panjang = len(kota)
print(f"panjang data: {panjang}")

# mengecek key ada atau tidak
KEY = "papua"
check = KEY in kota
print(check)


LENDICT = len(kota)
print(f"panjang dari dictionary = {LENDICT}")


KEY = "smp8"
ch = KEY in sekolah
print(f"disini pernyataan = {ch}")

# mengakses value pada dictionary engan get 
print(sekolah["smp1"])
print(sekolah.get("smp8"))
print(sekolah.get("sma", "key tidak ditemukan"))


# update value pada dictionary
kota["china"] = "kota impian"
print(kota)
kota.update({"jakarta":"banjir"})
kota.update({"jateng":"skena abiiz"})
print(kota)

# delete value pada dictionary

del kota["china"]
print(kota)


## looping dictionary

teman_teman = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung",
	"sep":"asep si kasyep",
	"cuy":"ucuy surucuy"
}

# looping first try (yangk keluar adalah keynya)
for data in teman_teman:
    print(data)


# operator untuk mengambil item/iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

value = teman_teman.values()
print(value)

for key, value in teman_teman.items():
    print(f"key : {key}, value : {value}")



# multi keys & nesting dictionary

laptop = {
    'nama':'thinkpad p15 v3 gen 4',
    'harga':25000000,
    'stock':5
}

mouse = {
    'nama':'Logitech G903 HERO',
    'harga':2000000,
    'stock':10
}

keyboard = {
    'nama':'Razer Huntsman V2',
    'harga':2800000,
    'stock':15
}

Headset = {
    'nama':'Logitech G Pro X Wireless',
    'harga':2500000,
    'stock':20
}


barang = {
    'laptop':laptop,
    'mouse':mouse,
    'keyboard':keyboard,
    'headset':Headset
}

print(f"berikut adalah peralatan game \n{barang['laptop']}\n{barang['mouse']}\n{barang['keyboard']}\n{barang['headset']}")

mahasiswa1 = {
	'nama':'Ucup Surucup',
	'nim':'19022001',
	'sks_lulus':130,
	'beasiswa':False,
	'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
	'nama':'Otong Surotong',
	'nim':'19022002',
	'sks_lulus':140,
	'beasiswa':True,
	'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
	'nama':'Asep Si Kasyep',
	'nim':'19022003',
	'sks_lulus':100,
	'beasiswa':False,
	'lahir':datetime.datetime(2000,2,29)
}

data_mahasiswa = {
	'MAH001':mahasiswa1,
	'MAH002':mahasiswa2,
	'MAH003':mahasiswa3
}

for mahasiswa in data_mahasiswa:
	KEY = mahasiswa

	NAMA = data_mahasiswa[KEY]['nama']
	NIM = data_mahasiswa[KEY]['nim']
	SKS = data_mahasiswa[KEY]['sks_lulus']
	BEASISWA = data_mahasiswa[KEY]['beasiswa']
	LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

	print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")


# latihan dictionary 

data_siswa = {
    'nama':'nama',
    'sim':00000,
    'kelas':0,
    'jurusan':'jurusan'
}

data =  dict.fromkeys(data_siswa)# fromkeys berfungsi untuk mengambil key pada dictionary dan menggabungkannya pada value 
print(data)
data['nama'] = input("masukkan nama siswa/siswi\t:")
data['sim'] = int(input("masukkan sim siswa/siswi\t:"))
data['kelas'] = int(input("masukkan kelas siswa/siswi\t:"))
data['jurusan'] = input("masukkan jurusan siswa/siswi\t:")

print(data)

## program dictionary

data_siswa = {
    'nama':'nama',
    'sim':00000,
    'kelas':0,
    'jurusan':'jurusan'
}

tambahan_data ={}
while True:
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA SISWA LABOR':^20}")
    print("-"*20)

    data =  dict.fromkeys(data_siswa)
    data['nama'] = input("masukkan nama siswa/siswi\t:")
    data['sim'] = int(input("masukkan sim siswa/siswi\t:"))
    data['kelas'] = int(input("masukkan kelas siswa/siswi\t:"))
    data['jurusan'] = input("masukkan jurusan siswa/siswi\t:")
    print("_"*70)
    print(data)

    tambahan_data.update({'key':data})
    
    print('_'*70)

    for siswa in tambahan_data:
        KEY = siswa

    NAME = tambahan_data[KEY]['nama']
    SIM = tambahan_data[KEY]['sim']
    KELAS = tambahan_data[KEY]['kelas']
    JURUSAN = tambahan_data[KEY]['jurusan']

    print(f"{KEY:<6} {SIM:<17} {KELAS:<3} {JURUSAN:^9}")

    print("\n")
    done = input("sudah atau belum bro yes/no\t:")

    if done == 'no':
        print("selamat tinggal")
        break


