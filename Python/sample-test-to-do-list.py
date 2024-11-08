import json

# File penyimpanan data
filename = "tasks.json"

# Fungsi untuk memuat tugas dari file JSON
def load_tasks():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan tugas ke file JSON
def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Fungsi untuk menampilkan semua tugas
def show_tasks(tasks):
    if not tasks:
        print("Tidak ada tugas.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Fungsi untuk menambah tugas baru
def add_task(tasks):
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    print("Tugas berhasil ditambahkan!")

# Fungsi untuk menghapus tugas berdasarkan nomor
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Tugas '{removed_task}' telah dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid. Harus angka.")

# Fungsi utama program
def main():
    tasks = load_tasks()
    while True:
        print("\nAplikasi Manajemen Tugas")
        print("1. Lihat semua tugas")
        print("2. Tambah tugas")
        print("3. Hapus tugas")
        print("4. Keluar")
        choice = input("Pilih opsi: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
