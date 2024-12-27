# Program untuk menghitung gaji bulanan karyawan

def hitung_gaji_bulanan(tarif_per_jam, jumlah_hari_kerja, jam_kerja_harian):
    gaji_normal_per_hari = 8 * tarif_per_jam  # Gaji untuk jam kerja normal
    total_gaji = 0

    for hari in range(1, jumlah_hari_kerja + 1):
        if jam_kerja_harian[hari - 1] <= 8:
            # Jam kerja normal
            gaji_harian = jam_kerja_harian[hari - 1] * tarif_per_jam
        else:
            # Jam lembur
            lembur = jam_kerja_harian[hari - 1] - 8
            gaji_harian = gaji_normal_per_hari + (lembur * tarif_per_jam * 1.5)
        
        total_gaji += gaji_harian

    return total_gaji

def main():
    print("Program Penghitung Gaji Bulanan Karyawan")
    
    # Input tarif per jam
    while True:
        try:
            tarif_per_jam = float(input("Masukkan tarif gaji per jam (Rp): "))
            if tarif_per_jam > 0:
                break
            else:
                print("Tarif gaji per jam harus positif!")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")

    # Input jumlah hari kerja
    while True:
        try:
            jumlah_hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
            if jumlah_hari_kerja > 0:
                break
            else:
                print("Jumlah hari kerja harus positif!")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    # Input jam kerja per hari
    jam_kerja_harian = []
    print("Masukkan jumlah jam kerja harian untuk setiap hari:")
    for i in range(jumlah_hari_kerja):
        while True:
            try:
                jam_kerja = float(input(f"  Hari ke-{i+1}: "))
                if jam_kerja >= 0:
                    jam_kerja_harian.append(jam_kerja)
                    break
                else:
                    print("Jam kerja tidak boleh negatif!")
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
    
    # Hitung total gaji
    total_gaji = hitung_gaji_bulanan(tarif_per_jam, jumlah_hari_kerja, jam_kerja_harian)
    
    print("\n=== Rincian Gaj
