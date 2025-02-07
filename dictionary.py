## dictionary -> memiliki workflow yang mirip dengan array, sehingga biasa disebut asosiatif array 
# dan dictionary terdiri dari key and value. Untuk mengakses dictionary kita tinggal memanggil key 
# untuk menampilkan value##




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