# Program untuk menentukan kategori usia

def tentukan_kategori_usia(usia):
    if 0 <= usia <= 5:
        return "Balita"
    elif 6 <= usia <= 12:
        return "Anak-anak"
    elif 13 <= usia <= 17:
        return "Remaja"
    elif 18 <= usia <= 59:
        return "Dewasa"
    elif usia >= 60:
        return "Lansia"
    else:
        return "Usia tidak valid"

def main():
    print("=== Program Kategori Usia ===")
    
    while True:
        try:
            usia = int(input("Masukkan usia Anda (dalam tahun): "))
            if usia >= 0:
                break
            else:
                print("Usia tidak boleh negatif! Harap masukkan angka yang valid.")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")

    kategori = tentukan_kategori_usia(usia)
    print(f"\nKategori usia Anda: {kategori}")

if __name__ == "__main__":
    main()
