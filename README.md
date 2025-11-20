Nama 		: Febryvia Deya Nur Havidtar Murti Aqsa

NIM 		: 312510194

Kelas 		: TI.25.A.2

Mata Kuliah 	: Pengantar Pemograman

# PRAKTIKUM 5

Dictionary Python adalah struktur data bawaan yang digunakan untuk menyimpan koleksi item dalam format pasangan kunci-nilai (key-value pairs)

Tujuan utama dari Dictionary Python adalah untuk menyimpan dan mengelola data yang memiliki hubungan logis antara satu bagian data (kunci) dengan bagian data lainnya (nilai) secara efisien

-Perintah Dictionary Perbaikan Sintaks dan Penjelasan

•	Membuat Dictionary

a= {}

•	Mengakses Dictionary

Print(a[‘n2’]) 	#print element with key ‘n2’

Print(a.keys()) 	#print all key from dict

Print(a.value() 	#print all value from dict

Print(a.item() 	#print list of tuple (key, value) from dict

-Dictionary

•	Mengubah element Dictionary

a[‘2’] = 10		 #change the item for kay ‘n2’

•	Menambahkan element Dictonary

a[‘n4’]			# add itemn with key ‘n4’

•	Loop Dictionary

for item in a.item():

	print(item) 	# print tuple (key, value)
  
	print(item[0]) 	#print key item

# Latihan 1

Program ini dibuat untuk memenuhi tugas Latihan Dictionary, yaitu membuat dan mengelola daftar kontak menggunakan struktur Dictionary pada Python.

#Program Daftar Mahasiswa (Dictionary)

Program data yang disimpan menggunakan dictionary

•	Tugas 30%

•	UTS 35%

•	UAS 35%

Penjelasan Kode:

#1. Membuat Dictionary Daftar Kontak

#Nama sebagai key, dan nomor sebagai value

#Data awal: Ari: 081267888, Dina: 08767777

daftar_kontak = {

    'Ari': '081267888',
    
    'Dina': '087677776'
}

#2. Menampilkan Dictionary Awal

1.	Tampilkan daftar_kontak

print("--- 1. Dictionary Awal ---")

print(daftar_kontak)

2.	print (“-“ * 30)

#3. Menampilkan kontak Ari

 print(f"Nomor kontak Ari: {daftar_kontak['Ari']}")

Mengambil value dari key ‘Ari’

dictionary[key]

Jadi daftar_kontak['Ari'] menghasilkan "081267888"

#4. Menambahkan kontak baru (Riko)

#Menggunakan key baru untuk menambah elemen Dictionary

daftar_kontak['Riko'] = '087654544'

#5. Ubah kontak Dina dengan nomor baru 088999776

#Menggunakan key yang sudah ada untuk mengubah nilai

daftar_kontak['Dina'] = '088999776'

#6. Tampilkan semua Nama (Keys)

#Menggunakan method .keys()

for nama in daftar_kontak.keys():

    print(f"- {nama}")

Output :

-Ari

-Dina

-Riko

Loop for menggunakan untuk mencetak satu-satu

#7. Menampilkan daftar Nama dan nomor

for nomor in daftar_kontak.values():

    print(f"- {nomor}")

value() mengambil semua nomor telepon

081267888

088999776

087654544

Pasangan key dan value dalam bentuk tuple:

('Ari', '081267888')

('Dina', '088999776')

('Riko', '087654544')

#8. Menghapus kontak Dina

#Menggunakan fungsi del

del daftar_kontak['Dina'] #del digunakan untuk menghapus elemen dictionary berdasarkan key

Menampilkan dictionary setelah dina dihapus

print("Daftar Kontak Akhir:")

print(daftar_kontak)

Hasilnya :
<img width="1718" height="842" alt="Hasil py" src="https://github.com/user-attachments/assets/c23e267e-ba2c-4362-995c-957c10af7466" />
<img width="1789" height="853" alt="Hasil py(2)" src="https://github.com/user-attachments/assets/dc2b5f72-2517-47ea-b7cc-f64240c6fe14" />


# Praktikum 5

#Program Input Nilai Mahasiswa

Program ini adalah aplikasi Command Line Interface (CLI) sederhana yang digunakan untuk mengelola data nilai mahasiswa. Program ini dibangun menggunakan struktur data Dictionary dalam Python

Program ini memiliki lima fungsi utama (CRUD + Cari) yang dapat diakses melalui menu:

1.	Lihat: Menampilkan semua data nilai dalam bentuk tabel.

2.	Tambah: Menambahkan data mahasiswa baru (NIM, Nama, Nilai).

3.	Ubah: Mengubah nilai Tugas, UTS, dan UAS berdasarkan NIM.

4.	Hapus: Menghapus data mahasiswa berdasarkan NIM.

5.	Cari: Mencari data berdasarkan NIM atau Nama.

6.	Keluar: Menghentikan program.

Struktur Data

•	Dictionary Utama (DATA_NILAI): Menyimpan seluruh data.

-	Key: NIM (Nomor Induk Mahasiswa), dipilih karena merupakan pengenal unik.

-	Value: Dictionary detail mahasiswa, contoh: {'Nama': 'Ari', 'Tugas': 99, 'UTS': 68, 'UAS': 88, 'Akhir': 84.30}.

Komponen Fungsionalitas (Menu Pilihan)

Program ini dioperasikan melalui menu interaktif yang mencakup lima fungsi utama3:

1.	Tambah Data (T):

- Fungsi ini meminta input NIM, Nama, Nilai Tugas, UTS, dan UAS.

-	Melakukan validasi sederhana untuk memastikan NIM tidak duplikat dan nilai berada dalam rentang 0-100.

-	Data disimpan menggunakan NIM sebagai kunci.

2.	Ubah Data (U):

-	Pengguna diminta memasukkan NIM yang datanya akan diubah

-	Jika NIM ditemukan, pengguna dapat memasukkan nilai baru untuk Tugas, UTS, dan UAS

-	Nilai yang tidak diisi akan mempertahankan nilai lama

3.	Hapus Data (H):
-	Fungsi ini meminta NIM data yang akan dihapus

-	Data dihapus dari DATA_NILAI menggunakan perintah del DATA_NILAI[nim]

4.	Tampilkan Data (L):

-	Fungsi ini mengiterasi (loop) seluruh elemen di DATA_NILAI dan menampilkannya dalam format tabel yang terstruktur, termasuk Nomor Urut

-	Jika Dictionary kosong, akan ditampilkan pesan "TIDAK ADA DATA"4

5.	Cari Data (C):

-	Fungsi ini memungkinkan pencarian data berdasarkan kata kunci yang cocok dengan NIM atau Nama mahasiswa

-	Hasil pencarian ditampilkan dalam format tabel yang sama dengan menu Lihat Data

IV. Mekanisme Perhitungan Nilai Akhir

Nilai Akhir dihitung secara otomatis saat data ditambahkan atau diubah, dengan menggunakan fungsi hitung_nilai_akhir(). Komposisi nilai yang digunakan adalah:

•	Nilai Tugas: 30%

•	Nilai UTS: 35%

•	Nilai UAS: 35%

Rumus yang diterapkan adalah:

Akhir = (0.30 x Tugas) + (0.35 x UTS) + (0.35 x UAS)

Hasilnya : 
 <img width="1547" height="717" alt="Hasil praktikum" src="https://github.com/user-attachments/assets/df4937c3-559e-4cc5-a884-45261250e190" />
<img width="1315" height="858" alt="Hasil praktikum(2)" src="https://github.com/user-attachments/assets/8b74bae8-eb07-446a-92d9-25e4b2aab54a" />


Algoritma
#1.	Mulai

#2.	Inilisialisasi Data: nilai_mahasiswa = {}
{

"Nama": {

      "tugas": ...,
      
      "uts": ...,
      
      "uas": ...,
      
      "nilai_akhir": ...
  }
}

#3.	Menampilkan loop while true

Menu:

1. Tambah Data

2. Ubah Data

3. Hapus Data

4. Tampilkan Data

5. Cari Data

6. Keluar

#4.	Percabangan menu
Program mengecek pilihan user:

•	"1" → jalankan tambah_data()

•	"2" → jalankan ubah_data()

•	"3" → jalankan hapus_data()

•	"4" → jalankan tampilkan_data()

•	"5" → jalankan cari_data()

•	"6" → keluar dari program

Jika pilihan salah: tampilkan “Pilihan tidak valid”

#5.	Fungsi tambah data

Langkah:

1.	Input nama mahasiswa.

2.	Jika nama sudah ada → tampilkan “Data sudah ada”.

3.	Jika belum ada:

o	Input nilai tugas

o	Input nilai UTS

o	Input nilai UAS

4.	Hitung nilai akhir:

nilai_akhir = tugas*0.3 + uts*0.35 + uas*0.35

5.	Simpan data ke dictionary:

nilai_mahasiswa[nama] = { ... }

6.   Munculkan pesan “Data berhasil ditambahkan”

#6.	Fungsi ubah data

Langkah:

1.	Input nama mahasiswa yang ingin diubah.

2.	Jika nama tidak ditemukan → tampilkan pesan.

3.	Jika ditemukan:

o	Input nilai tugas baru

o	Input nilai UTS baru

o	Input nilai UAS baru

4.	Hitung nilai akhir baru.

5.	Ganti seluruh data mahasiswa di dictionary.

6.	Tampilkan “Data berhasil diubah”.

#7.	Fungsi hapus data

1.	Input nama mahasiswa yang akan dihapus.

2.	Jika nama tidak ada → tampilkan pesan.

3.	Jika ada hapus data : del nilai_mahasiswa[nama]

4.	Tampilkan “Data berhasil dihapus”.

#8.	Fungsi tampilan data

Langkah:

1.	Jika dictionary kosong dengan  menampilkan “Data mahasiswa kosong”.

2.	Jika ada data: Tampilkan header tabel

-Loop setiap mahasiswa dalam dictionary

-Cetak nilai tugas, uts, uas, dan nilai akhir

#9.	Fungsi cari data

Langkah:

1.	Input nama mahasiswa yang dicari.

2.	Cek apakah nama ada dalam dictionary.

3.	Jika tidak ada → tampilkan “Data mahasiswa tidak ditemukan”.

4.	Jika ada:	Tampilkan data tugas, uts, uas, dan nilai akhir mahasiswa tersebut.

#10.	Keluar program

print("Keluar dari program.")

break

loop berhenti program selesai

#11. Selesai

Flowchart :

# Flowchart Program Nilai Mahasiswa

```
+---------------------+
|       Start         |
+---------------------+
          |
          V
+---------------------+
|   Tampilkan Menu    |
+---------------------+
          |
          V
+---------------------+
| Pilih Menu (1-6)    |
+---------------------+
          |
          +---------------------+---------------------+---------------------+
          |                     |                     |                     |
          V                     V                     V                     V
+---------------------+  +---------------------+  +---------------------+  +---------------------+
| Jika 1: Tambah Data |  | Jika 2: Ubah Data  |  | Jika 3: Hapus Data  |  | Jika 4: Tampilkan  |
+---------------------+  +---------------------+  +---------------------+  +---------------------+
          |                     |                     |                     |
          V                     V                     V                     V

(1) ----------------- TAMBAH DATA -----------------
+---------------------+
| Input Nama          |
+---------------------+
          |
          V
+---------------------+
| Cek Nama Ada?       |
+---------------------+
     | Ada     | Tidak
     V         V
+---------------------+   +---------------------+
| Nama Sudah Ada!     |   | Input Tugas, UTS,  |
| Kembali ke Menu     |   | dan UAS            |
+---------------------+   +---------------------+
                              |
                              V
                     +---------------------+
                     | Hitung Nilai Akhir |
                     +---------------------+
                              |
                              V
                     +---------------------+
                     | Simpan ke Dict      |
                     +---------------------+
                              |
                              V
                     +---------------------+
                     | Data Ditambahkan!   |
                     +---------------------+

(2) ------------------- UBAH DATA --------------------
+---------------------+
| Input Nama          |
+---------------------+
          |
          V
+---------------------+
| Cek Nama Ada?       |
+---------------------+
     | Ada     | Tidak
     V         V
+---------------------+   +---------------------+
| Input Nilai Baru    |   | Nama Tidak Ditemukan|
| (Tugas/UTS/UAS)     |   | Kembali ke Menu     |
+---------------------+   +---------------------+
          |
          V
+---------------------+
| Hitung Nilai Akhir |
+---------------------+
          |
          V
+---------------------+
| Update Dict         |
+---------------------+
          |
          V
+---------------------+
| Data Diubah!        |
+---------------------+

(3) ------------------- HAPUS DATA -------------------
+---------------------+
| Input Nama          |
+---------------------+
          |
          V
+---------------------+
| Cek Nama Ada?       |
+---------------------+
     | Ada     | Tidak
     V         V
+---------------------+   +---------------------+
| Hapus dari Dict     |   | Nama Tidak Ditemukan|
+---------------------+   | Kembali ke Menu     |
          |               +---------------------+
          V
+---------------------+
| Data Dihapus!       |
+---------------------+

(4) --------------- TAMPILKAN DATA -------------------
+---------------------+
| Cek Dict Kosong?    |
+---------------------+
     | Ya      | Tidak
     V         V
+---------------------+   +---------------------+
| Tidak Ada Data      |   | Tampilkan Semua     |
| Kembali ke Menu     |   +---------------------+
+---------------------+

(5) ------------------ CARI DATA ---------------------
+---------------------+
| Input Nama          |
+---------------------+
          |
          V
+---------------------+
| Cek Nama Ada?       |
+---------------------+
     | Ada     | Tidak
     V         V
+---------------------+   +---------------------+
| Tampilkan Detail    |   | Nama Tidak Ditemukan|
+---------------------+   | Kembali ke Menu     |
                          +---------------------+

(6) ------------------ KELUAR PROGRAM ----------------
+---------------------+
|       End           |
+---------------------+
```
