# Program untuk mencetak pola bintang segitiga

def cetak_segitiga(baris):
    print("\n=== Pola Bintang Segitiga ===")
    for i in range(1, baris + 1):
        print("*" * i)

def main():
    print("Program Pola Bintang Segitiga")
    
    # Meminta jumlah baris dari pengguna
    while True:
        try:
            baris = int(input("Masukkan jumlah baris (angka positif): "))
            if baris > 0:
                break
            else:
                print("Masukkan harus berupa angka positif!")
        except ValueError:
            print("Masukkan tidak valid! Harap masukkan angka.")

    # Memanggil fungsi untuk mencetak pola segitiga
    cetak_segitiga(baris)

if __name__ == "__main__":
    main()
