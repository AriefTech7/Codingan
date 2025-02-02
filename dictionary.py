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

kota['china'] = 'shanghai'# menambahkan elemen pada dictionary
print(kota) 
print(kota['jakarta'])

panjang = len(kota)
print(f"panjang data: {panjang}")# mengukur panjang data dictionary kota

KEY = "papua"# mengecek key ada atau tidak
check = KEY in kota
print(check)