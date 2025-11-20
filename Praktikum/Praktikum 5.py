import os

# Dictionary utama untuk menyimpan data mahasiswa
# Key: NIM, Value: Dictionary detail mahasiswa (Nama, Tugas, UTS, UAS, Akhir)
DATA_NILAI = {}


# Fungsi untuk menghitung Nilai Akhir
def hitung_nilai_akhir(tugas, uts, uas):
    """
    Menghitung Nilai Akhir sesuai komposisi: Tugas 30%, UTS 35%, UAS 35%.
    """
    tugas = float(tugas)
    uts = float(uts)
    uas = float(uas)

    # Perhitungan Nilai Akhir
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    return round(nilai_akhir, 2)


# Fungsi untuk validasi dan input nilai dalam rentang 0-100
def input_nilai(prompt):
    while True:
        try:
            nilai = int(input(prompt))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus berada dalam rentang 0 sampai 100.")
        except ValueError:
            print("Input tidak valid. Masukkan nilai berupa angka bulat.")


## --- Fungsi Menu Program ---

# 1. Tampilkan Data (L)ihat
def tampilkan_data():
    """Menampilkan semua data nilai mahasiswa dalam format tabel yang terstruktur."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "=" * 70)
    print("Daftar Nilai".center(70))
    print("=" * 70)

    # Mendefinisikan struktur tabel
    header = "| NO | NIM     | NAMA                  | TUGAS | UTS | UAS | AKHIR |"
    separator = "=" * len(header)

    print(separator)
    print(header)
    print(separator)

    if not DATA_NILAI:
        # Menampilkan pesan jika Dictionary kosong
        print("|" + "TIDAK ADA DATA".center(len(header) - 2) + "|")
        print(separator)
        return

    # Iterasi dan menampilkan data
    no = 1
    for nim, data in DATA_NILAI.items():
        row = (
            f"| {no:<2} "
            f"| {nim:<7} "
            f"| {data['Nama']:<21} "
            f"| {data['Tugas']:<5} "
            f"| {data['UTS']:<3} "
            f"| {data['UAS']:<3} "
            f"| {data['Akhir']:>5.2f} |"
        )
        print(row)
        no += 1

    print(separator)
# 2. Tambah Data (T)ambah
def tambah_data():
    """
    Menerima input data mahasiswa baru dan menambahkannya ke dalam Dictionary.
    NIM digunakan sebagai kunci (key) unik.
    """
    print("\n" + "=" * 30)
    print("Tambah Data".center(30))
    print("=" * 30)

    while True:
        nim = input("NIM: ").strip()
        if nim in DATA_NILAI:
            print("NIM sudah terdaftar. Proses penambahan dibatalkan.")
        elif nim:
            break
        else:
            print("NIM tidak boleh kosong.")
    nama = input("Nama: ").strip()
    
    print("Masukkan Nilai Komponen:")
    nilai_tugas = input_nilai("Nilai Tugas: ")
    nilai_uts = input_nilai("Nilai UTS: ")
    nilai_uas = input_nilai("Nilai UAS: ")

    # Perhitungan nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

    # Memasukkan data ke dalam Dictionary
    DATA_NILAI[nim] = {
        'Nama': nama,
        'Tugas': nilai_tugas,
        'UTS': nilai_uts,
        'UAS': nilai_uas,
        'Akhir': nilai_akhir
    }

    print("\nInformasi: Data mahasiswa telah berhasil ditambahkan.")


# 3. Ubah Data (U)bah
def ubah_data():
    """Mengubah data nilai mahasiswa yang sudah ada berdasarkan NIM. """
    print("\n" + "=" * 30)
    print("Ubah Data".center(30))
    print("=" * 30)

    nim = input("Masukkan NIM data yang akan diubah: ").strip()

    if nim not in DATA_NILAI:
        print(f"Peringatan: NIM {nim} tidak ditemukan dalam daftar.")
        return

    data = DATA_NILAI[nim]
    print(f"\nData saat ini untuk NIM {nim} (Nama: {data['Nama']}):")
    print("  Tugas: {data['Tugas']}, UTS: {data['UTS']}, UAS: {data['UAS']}")

    # Proses input nilai baru (mempertahankan nilai lama jika input kosong/non-digit)
    print("\nMasukkan nilai baru (masukkan nilai yang sama atau kosongkan jika tidak ingin diubah):")

    tugas_str = input(f"Nilai Tugas Baru ({data['Tugas']}): ").strip()
    nilai_tugas = input_nilai("Nilai Tugas: ") if tugas_str.isdigit() else data['Tugas']

    uts_str = input(f"Nilai UTS Baru ({data['UTS']}): ").strip()
    nilai_uts = input_nilai("Nilai UTS: ") if uts_str.isdigit() else data['UTS']

    uas_str = input(f"Nilai UAS Baru ({data['UAS']}): ").strip()
    nilai_uas = input_nilai("Nilai UAS: ") if uas_str.isdigit() else data['UAS']

    # Perbarui dan hitung ulang nilai akhir
    data['Tugas'] = nilai_tugas
    data['UTS'] = nilai_uts
    data['UAS'] = nilai_uas
    data['Akhir'] = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

    print("\nInformasi: Data nilai mahasiswa telah berhasil diperbarui.")


# 4. Hapus Data (H)apus
def hapus_data():
    """Menghapus data mahasiswa dari Dictionary berdasarkan NIM. """
    print("\n" + "=" * 30)
    print("Hapus Data".center(30))
    print("=" * 30)

    nim = input("Masukkan NIM data yang akan dihapus: ").strip()

    if nim not in DATA_NILAI:
        print(f"Peringatan: NIM {nim} tidak ditemukan dalam daftar.")
        return

    nama = DATA_NILAI[nim]['Nama']

    # Menghapus elemen dari Dictionary
    del DATA_NILAI[nim]

    print(f"\nInformasi: Data mahasiswa atas nama {nama} (NIM: {nim}) telah berhasil dihapus.")


# 5. Cari Data (C)ari
def cari_data():
    """Melakukan pencarian data mahasiswa berdasarkan kata kunci NIM atau Nama. """
    print("\n" + "=" * 30)
    print("Cari Data".center(30))
    print("=" * 30)

    keyword = input("Masukkan NIM atau Nama yang ingin dicari: ").strip().lower()

    hasil_pencarian = {}

    # Proses pencarian
    for nim, data in DATA_NILAI.items():
        if keyword in nim.lower() or keyword in data['Nama'].lower():
            hasil_pencarian[nim] = data

    if not hasil_pencarian:
        print(f"\nInformasi: Data dengan kata kunci '{keyword}' tidak ditemukan.")
        return

    # Menampilkan hasil
    print("\n" + "=" * 70)
    print(f"Hasil Pencarian untuk '{keyword}'".center(70))
    print("=" * 70)

    header = "| NO | NIM     | NAMA                  | TUGAS | UTS | UAS | AKHIR |"
    separator = "-" * len(header)

    print(separator)
    print(header)
    print(separator)

    no = 1
    for nim, data in hasil_pencarian.items():
        row = (
            f"| {no:<2} "
            f"| {nim:<7} "
            f"| {data['Nama']:<21} "
            f"| {data['Tugas']:<5} "
            f"| {data['UTS']:<3} "
            f"| {data['UAS']:<3} "
            f"| {data['Akhir']:>5.2f} |"
        )
        print(row)
        no += 1

    print(separator)


## --- Fungsi Utama Program ---
def main():
    while True:
        print("\n" + "#" * 40)
        print("PROGRAM INPUT NILAI MAHASISWA".center(40))
        print("#" * 40)

        # Tampilkan menu pilihan
        pilihan = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ").strip().upper()

        if pilihan == 'L':
            tampilkan_data()
        elif pilihan == 'T':
            tambah_data()
        elif pilihan == 'U':
            ubah_data()
        elif pilihan == 'H':
            hapus_data()
        elif pilihan == 'C':
            cari_data()
        elif pilihan == 'K':
            print("\nProgram dihentikan. Terima kasih.")
            break
        else:
            print("\nKesalahan Input: Pilihan menu tidak valid. Silakan ulangi.")


if __name__ == "__main__":
    main()