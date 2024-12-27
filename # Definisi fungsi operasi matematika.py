# Definisi fungsi operasi matematika
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Kesalahan: Pembagian dengan nol tidak diperbolehkan!"
    return a / b

def main():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    # Meminta pengguna memilih operasi
    while True:
        try:
            pilihan = int(input("Masukkan pilihan Anda (1/2/3/4): "))
            if pilihan in [1, 2, 3, 4]:
                break
            else:
                print("Pilihan tidak valid! Harap pilih antara 1 hingga 4.")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    # Meminta pengguna memasukkan dua angka
    while True:
        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    # Melakukan operasi berdasarkan pilihan pengguna
    if pilihan == 1:
        hasil = tambah(a, b)
        operasi = "Penjumlahan"
    elif pilihan == 2:
        hasil = kurang(a, b)
        operasi = "Pengurangan"
    elif pilihan == 3:
        hasil = kali(a, b)
        operasi = "Perkalian"
    elif pilihan == 4:
        hasil = bagi(a, b)
        operasi = "Pembagian"
    
    # Menampilkan hasil
    print(f"\nHasil {operasi}: {hasil}")

if __name__ == "__main__":
    main()
