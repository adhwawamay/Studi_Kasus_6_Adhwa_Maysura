import json

path = r"C:\Users\Acer\OneDrive\Dasar Dasar Pemograman\studi kasus 6\studikasus6.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

def baca_data():
    file = open(path, "r")
    data = json.load(file)
    file.close()
    return data

def simpan_data(data):
    file = open(path, "w")
    json.dump(data, file, indent=4)
    file.close()

def hitung_predikat(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

def lihat_nilai():
    data = baca_data()

    print()
    if len(data) == 0:
        print("Data nilai mahasiswa kosong.")
    else:
        print("No | Nama | NIM | Mata Kuliah | Nilai | Predikat")
        print("---------- ---------- ---------- ---------- ----------")
        nomor = 1
        for mhs in data:
            print(nomor, "|", mhs["nama"], "|", mhs["nim"], "|", mhs["mata_kuliah"], "|", mhs["nilai"], "|", mhs["predikat"])
            nomor = nomor + 1

def tambah_data():
    nama = input("Nama          : ")
    nim = input("NIM           : ")
    mata_kuliah = input("Mata Kuliah   : ")
    nilai = float(input("Nilai (0-100) : "))

    if nilai < 0 or nilai > 100:
        print("Nilai harus antara 0 sampai 100!")
    else:
        if nilai == int(nilai):
            nilai = int(nilai)

        predikat = hitung_predikat(nilai)
        data_baru = {
            "nama": nama,
            "nim": nim,
            "mata_kuliah": mata_kuliah,
            "nilai": nilai,
            "predikat": predikat
        }

        data = baca_data()        
        data.append(data_baru)            
        simpan_data(data)         
        print("Data berhasil disimpan! Predikat:", predikat)

while True:
    print()
    print("--- --- SISTEM PENCATATAN NILAI MAHASISWA --- ---")
    print("1. Lihat semua nilai")
    print("2. Tambah data baru")
    print("3. Keluar")
    pilihan = input("Silahkan memilih menu berikut (1-3): ")

    if pilihan == "1":
        lihat_nilai()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        print("Terima kasih, program selesai dijalankan.")
        break
    else:
        print("Pilihan tidak valid, silahkan coba lagi.")