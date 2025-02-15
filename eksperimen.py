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






