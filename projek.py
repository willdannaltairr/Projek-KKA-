daftar_mapel = []

def display_menu():
    print("\n Menu:")
    print("1. Lihat Seluruh Data")
    print("2. Tambah Data")
    print("3. Hapus Data")
    print("4. Jumlahkan Seluruh Nilai")
    print("5. Hitung Rata-rata Nilai")
    print("6. Keluar")

def lihat_data():
    print("\n Daftar Nilai Mata Pelajaran:")

    if not daftar_mapel:
        print("Data kosong.")
        return

    for mapel, nilai in daftar_mapel:
        print(f"- {mapel}: {nilai}")

def tambah_data():
    nama_mapel = input("Masukkan nama mata pelajaran : ")
    nilai      = float(input("Masukkan nilai               : "))
    daftar_mapel.append([nama_mapel, nilai])
    print(f"{nama_mapel} dengan nilai {nilai} berhasil ditambahkan.")

def hapus_data():
    mapel_hapus = input("Masukkan nama mata pelajaran yang ingin dihapus: ")
    for mapel in daftar_mapel:
        if mapel[0].lower() == mapel_hapus.lower():
            daftar_mapel.remove(mapel)
            print(f"{mapel_hapus} berhasil dihapus.")
            return
    print(f"{mapel_hapus} tidak ditemukan dalam data.")

def jumlah_nilai():
    print("\n Jumlah Seluruh Nilai:")

    if not daftar_mapel:
        print("Data kosong.")
        return

    total = 0
    for mapel, nilai in daftar_mapel:
        total = total + nilai

    print(f"Total seluruh nilai: {total}")

def rata_rata_nilai():
    print("\n Rata-rata Nilai:")

    if not daftar_mapel:
        print("Data kosong.")
        return

    total = 0
    for mapel, nilai in daftar_mapel:
        total = total + nilai

    rata_rata = total / len(daftar_mapel)
    print(f"Rata-rata nilai: {rata_rata}")

def main():
    while True:
        display_menu()
        choice = input("Pilih menu (1-6): ")

        if choice == '1':
            lihat_data()
        elif choice == '2':
            tambah_data()
        elif choice == '3':
            hapus_data()
        elif choice == '4':
            jumlah_nilai()
        elif choice == '5':
            rata_rata_nilai()
        elif choice == '6':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()