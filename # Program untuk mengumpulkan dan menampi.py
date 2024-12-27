# Program untuk mengumpulkan dan menampilkan biodata

def tampilkan_biodata(nama, usia, alamat, hobi):
    print("\n=== Biodata Anda ===")
    print(f"Nama   : {nama}")
    print(f"Usia   : {usia} tahun")
    print(f"Alamat : {alamat}")
    print(f"Hobi   : {hobi}")

def main():
    print("Selamat datang! Masukkan informasi biodata Anda.")
    
    # Meminta input dari pengguna
    nama = input("Masukkan nama Anda: ")
    usia = input("Masukkan usia Anda: ")
    alamat = input("Masukkan alamat Anda: ")
    hobi = input("Masukkan hobi Anda: ")
    
    # Menampilkan biodata
    tampilkan_biodata(nama, usia, alamat, hobi)

if __name__ == "__main__":
    main()
