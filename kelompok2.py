daftar_genre = ["Action", "Drama", "Komedi", "Horor", "Thriller"]

for genre in daftar_genre:
    print(f"{genre}")

genre_pilihan = input("Pilih genre film: ")

if genre_pilihan not in daftar_genre:
    print("Genre tidak valid!")
    exit()

film_action = ["Lift", "Fast & Furious", "John Wick"]

if genre_pilihan == "Action":
    for film in film_action:
        print(f"- {film}")

film_pilihan = input("Pilih film: ")

if film_pilihan not in film_action:
    print("Film tidak valid!")
    exit()

detail_film = {
    "nama_film": "Lift",
    "waktu": "15:00 - 17:00 WIT",
    "harga_tiket": {
        "hari_biasa": 35000,
        "sabtu": 45000,
        "minggu": 50000
    }
}

hari = input("Masukkan hari (hari biasa/sabtu/minggu): ")

if hari not in detail_film["harga_tiket"]:
    print("Hari tidak valid!")
    exit()

harga_tiket = detail_film["harga_tiket"][hari]

print(f"Nama film: {detail_film['nama_film']}")
print(f"Waktu: {detail_film['waktu']}")
print(f"Harga Tiket: Rp{harga_tiket}")

konfirmasi = input("Apakah anda ingin membeli tiket? (Y/T) ")

if konfirmasi.lower() != "y":
    print("Pembelian dibatalkan!")
    exit()

jumlah_tiket = int(input("Masukkan jumlah tiket: "))

nama_pembeli = []
usia_pembeli = []

for i in range(jumlah_tiket):
    nama = input(f"Masukkan nama pembeli ke-{i+1}: ")
    usia = int(input(f"Masukkan usia pembeli ke-{i+1}: "))
    
    nama_pembeli.append(nama)
    usia_pembeli.append(usia)

for i in range(jumlah_tiket):
    if usia_pembeli[i] <= 17:
        print(f"{nama_pembeli[i]} tidak bisa membeli tiket karena usianya di bawah 17 tahun.")
        exit()

print("Invoice Tiket")

for i in range(jumlah_tiket):
    print(f"{i+1}. Nama: {nama_pembeli[i]}")
    print(f"   Usia: {usia_pembeli[i]} Tahun")
    print(f"   Film: {detail_film['nama_film']}")
    print(f"   Waktu: {detail_film['waktu']}")
    print(f"   Harga Tiket: Rp{harga_tiket}")
    print()

print(f"Total: Rp{jumlah_tiket * harga_tiket}")