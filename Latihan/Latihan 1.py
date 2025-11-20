# 1. Buat Dictionary daftar kontak
daftar_kontak = {
    'Ari': '081267888',
    'Dina': '087677776'
}
print("--- 1. Dictionary Awal ---")
print(daftar_kontak)
print("-" * 30)

# 2. Tampilkan kontaknya Ari
print("\n--- 2. Tampilkan kontak Ari ---")
print(f"Nomor kontak Ari: {daftar_kontak['Ari']}")
print("-" * 30)

# 3. Tambah kontak baru dengan nama Riko, nomor 087654544
daftar_kontak['Riko'] = '087654544'
print("\n--- 3. Setelah Tambah Riko ---")
print(daftar_kontak)
print("-" * 30)

# 4. Ubah kontak Dina dengan nomor baru 088999776
daftar_kontak['Dina'] = '088999776'
print("\n--- 4. Setelah Ubah Dina ---")
print(daftar_kontak)
print("-" * 30)

# 5. Tampilkan semua Nama (Keys)
print("\n--- 5. Tampilkan semua Nama (Keys) ---")
print("Daftar Nama:")
for nama in daftar_kontak.keys():
    print(f"- {nama}")
print("-" * 30)

# 6. Tampilkan semua Nomor (Values)
print("\n--- 6. Tampilkan semua Nomor (Values) ---")
print("Daftar Nomor:")
for nomor in daftar_kontak.values():
    print(f"- {nomor}")
print("-" * 30)
# 7. Tampilkan daftar Nama dan nomornya
print("\n--- 7. Tampilkan daftar Nama dan Nomornya (Items) ---")
print("Daftar Kontak Lengkap:")
for nama, nomor in daftar_kontak.items():
    print(f"- Nama: {nama}, Nomor: {nomor}")
print("-" * 30)
# 8. Hapus kontak Dina
del daftar_kontak['Dina']
print("\n--- 8. Setelah Hapus Dina ---")
print("Daftar Kontak Akhir:")
print(daftar_kontak)
print("-" * 30)