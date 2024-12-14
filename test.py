from module.clear import clear
from utils.interface import time_interface

class TimeConverter:
    def __init__(self):
        self.konversi = {
            "1": {"detik": lambda x: {"menit": x / 60, "jam": x / 3600, "hari": x / 86400}},
            "2": {"menit": lambda x: {"detik": x * 60, "jam": x / 60, "hari": x / 1440}},
            "3": {"jam": lambda x: {"detik": x * 3600, "menit": x * 60, "hari": x / 24}},
        }

    def clear_screen(self):
        clear()

    def interface(self):
        time_interface()

    def get_operation(self):
        while True:
            try:
                data_input = input("Pilih opsi [1]/[2]/[3]: ")
                if data_input in self.konversi:  # Memeriksa jika input valid
                    return data_input
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")

    def convert_time(self):
        while True:
            self.clear_screen()
            self.interface()

            data_input = self.get_operation()
            satuan_waktu, fungsi_konversi = list(self.konversi[data_input].items())[0]

            try:
                nilai_waktu = float(input(f"Masukkan waktu dalam {satuan_waktu}: "))
                hasil = fungsi_konversi(nilai_waktu)

                for satuan, nilai in hasil.items():
                    print(f"{satuan_waktu} => {satuan} = {nilai}")
            except ValueError:
                print("Input harus berupa angka!")
            except KeyboardInterrupt:
                print("\nProgram dimatikan secara paksa.")
                break

            pilihan_lanjut = input("Apakah Anda ingin melanjutkan? [Y/N]: ").upper()
            if pilihan_lanjut == "N":
                print("Terima kasih telah menggunakan program!")
                break

# Cara menjalankan program
if __name__ == "__main__":
    converter = TimeConverter()
    converter.convert_time()
