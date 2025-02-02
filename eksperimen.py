
list_buku = []

while True:
     judul = input("masukkan judul buku\t:")
     penulis = input("masukkan nama penulis\t:")

     buku = [judul, penulis]
     list_buku.append(buku)

     for index, buku in enumerate(list_buku, start=1):
          print(f"{index} | {buku[0]} | {buku[1]}")

     lanjut = input("Apakah lanjut (y/n)")

     if lanjut == "n":
          break
print("PROGRAM SELESAI")
