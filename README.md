# Studi_Kasus_6_Adhwa_Maysura
Nama : Adhwa Maysura<br>
Nim : 2609116103 (Ganjil)<br>
Kelas : C

# Sistem Pencatatan Nilai Mahasiswa
## Penjelasan Singkat Kode Python

<img width="1581" height="223" alt="6 1" src="https://github.com/user-attachments/assets/3ca923aa-b985-4660-85dc-95ab1e98d950" />

1. **import json** memanggil modul bawaan Python agar file JSON bisa dibaca dan ditambahkan.
2. **path = r"C:\..."** menyimpan lokasi file JSON. Awalan r (raw string) membuat tanda \ dapat dibaca, bukan sebagai karakter khusus.
3. **with open(...) as f: data = json.load(f)** with menutup file otomatis setelah selesai.

<img width="1563" height="162" alt="6 2" src="https://github.com/user-attachments/assets/2c2e0659-e9bb-49f2-b353-9fc36ea2ec62" />

- **baca_data()** membuka file dengan mode "r" (read), mengubah isinya menjadi list Python lewat json.load(), menutup file, lalu mengembalikan list itu dengan **return**.

<img width="1564" height="164" alt="6 3" src="https://github.com/user-attachments/assets/f7c70803-8b1e-412f-9d6d-b6d1002be5e9" />

- **simpan_data(data)** membuka file dengan mode "w" (write) dan menulis data ke file lewat json.dump(). lalu untuk **indent=4** membuat isi file rapi dan mudah dibaca.

<img width="1547" height="355" alt="6 6" src="https://github.com/user-attachments/assets/b3f10502-706d-48d0-8e20-69174983d1d5" />

- **hitung_predikat(nilai)** menentukan predikat dengan if-elif-else: A untuk nilai ≥ 85, B ≥ 75, C ≥ 60, D ≥ 50, dan E untuk sisanya.

<img width="1564" height="437" alt="6 5" src="https://github.com/user-attachments/assets/370fad63-aa89-40a8-8967-69148368082e" />

- **lihat_nilai()** memanggil **baca_data().** Jika list kosong, program menampilkan pesan data kosong. Jika ada, for menampilkan data satu per satu, dan nomor bertambah 1 tiap baris.

<img width="1484" height="778" alt="6 7" src="https://github.com/user-attachments/assets/179adf82-91f2-40b8-be26-f46bb4a1bbc1" />

- **tambah_data()** meminta input nama, NIM, mata kuliah, dan nilai. untuk **float()** mengubah nilai menjadi angka desimal. Setelah itu program memeriksa apakah nilai berada di antara 0 dan 100. Nilai bulat seperti 95.0 diubah menjadi 95 dengan kode **int()**. Data baru dibuat sebagai dictionary, lalu proses simpannya melalui 3 langkah yaitu baca data lama, append() data baru, dan simpan_data() ke file.

<img width="1568" height="550" alt="6 8" src="https://github.com/user-attachments/assets/7f703a49-630e-4335-b6c0-841346e82039" />

- **while True** membuat menu tampil terus-menerus (pengulangan).
- **input()** menerima pilihan menu dari user, atau agar pengguna dapat mengisi menu pada sistem.
- **break** untuk menghentikan pengulangan dari kode **while true**
- **if-elif-else** memanggil fungsi sesuai pilihan:<br>
1. memanggil **lihat_nilai()**,
2. memanggil **tambah_data()**, dan
3. menampilkan pesan lalu **break** untuk menghentikan program.
4. Pilihan lain menampilkan pesan tidak valid.

## Hasil Run Kode Python
<img width="1610" height="707" alt="6 9 run" src="https://github.com/user-attachments/assets/01300b94-a705-4b79-9c3a-0d422d966224" />

<img width="1604" height="552" alt="7 0run" src="https://github.com/user-attachments/assets/95c5e6d5-e5a7-4ca0-a27f-c0fd99eb0af0" /> 

## File JSON Before - After

- Before 
<img width="1484" height="747" alt="Screenshot (120)" src="https://github.com/user-attachments/assets/034181ca-52df-456b-a6ba-b7cf27995793" />


- After
<img width="1585" height="904" alt="Screenshot (127)" src="https://github.com/user-attachments/assets/6477ddb4-fbc7-4664-b0ff-8c910565af55" />















