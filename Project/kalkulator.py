print('\n===================kalkulator====================')
def kalkulator():
    print("pilih operasi:")
    print("1. tambah")
    print("2. kurang")
    print("3. kali")
    print("4. bagi")

    operasi = input ("masukan pilihan (1/2/3/4): ")

    num1 = float(input("masukan angka pertama: "))
    num2 = float(input("masukan angka kedua: "))

    if operasi == '1':
        hasil = num1 + num2
        print (f"hasil: {num1} + {num2} = {hasil}")
    elif operasi == '2':
        hasil = num1 - num2
        print (f"hasil: {num1} - {num2} = {hasil}")
    elif operasi == '3':
        hasil = num1 * num2
        print (f"hasil: {num1} * {num2} = {hasil}")
    elif operasi == '4':
        if num2 != 0:
            hasil = num1 / num2
            print (f"hasil: {num1} / {num2} = {hasil}")
        else:
            print("pembagian dengan nol tidak diperbolehkan")
    else:
            sprint("operasi tidak valid!")
kalkulator()