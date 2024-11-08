# program menghitung jumlah kata dalam kalimat
def hitung_kalimat_kata(kalimat):
    kata = kalimat.split() # memisahkan kalimat berdasarkan spasi
    return len(kata)

kalimat = input("masukan kalimat: ")
jumlah_kata = hitung_kalimat_kata(kalimat)
print(f"jumlah kata dalam kalimat adalah : {jumlah_kata}")