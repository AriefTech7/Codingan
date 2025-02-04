## dictionary -> memiliki workflow yang mirip dengan array, sehingga biasa disebut asosiatif array 
# dan dictionary terdiri dari key and value. Untuk mengakses dictionary kita tinggal memanggil key 
# untuk menampilkan value##

buah = ['apel', 'mangga', 'pisang', 'jeruk', 'anggur']


sekolah = {
    'smp1':'latifa',
    'smp8':'timo',
    'smklabor':'arif',
    'smk':'dewe',
    "sehat":buah
}

print(sekolah['smklabor'])
print(sekolah['sehat'])

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