def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    kelas = data[1]
    umur = data[2]

    print(f"{nama} adalah siswa dikelas {kelas} dan baru menginjak umur {umur}")

fungsi(["andi",12,19])


def data(*args):
    nama = args[0]
    kelas = args[1]
    umur = args[2]

    print(f"{nama} adalah siswa dikelas {kelas} dan baru menginjak umur {umur}")

data("udin",11,18)


def proses(*data):
    nama = data[0]
    sekolah = data[1]
    status = data[2]
    kelas = data[3]

    print(f"{nama} adalah siswa biasa yang bersekolah di smk {sekolah} dan sudah menginjak {kelas} dari smp ia masih berstatus {status}")

proses("wahyu","labor","single",12)


def contoh_fungsi(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

contoh_fungsi(nama="John", umur=25, kota="Jakarta")


=======
def program():
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

program()
