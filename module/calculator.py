from module.clear import clear

class Calculator:
    def __init__(self):
        self.result = 0

    def clear_screen(self):
        clear()

    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Input harus berupa angka!")

    def get_operation(self):
        while True:
            try:
                operasi = int(input("Pilih operasi: \n1. +  (penjumlahan)\n2. -  (pengurangan)\n3. *  (perkalian)\n4. /  (pembagian)\nMasukkan pilihan: "))
                if operasi in [1, 2, 3, 4]:
                    return operasi
                else:
                    print("Operasi tidak valid.")
            except ValueError:
                print("Input harus berupa angka!")

    def perform_operation(self, operasi, angka1, angka2):
        try:
            match operasi:
                case 1:
                    return angka1 + angka2
                case 2:
                    return angka1 - angka2
                case 3:
                    return angka1 * angka2
                case 4:
                    if angka2 == 0:
                        print("Tidak dapat membagi dengan nol!")
                        return None
                    return angka1 / angka2
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            return None

    def continue_with_result(self):
        while True:
            lanjut = input("Apakah ingin melanjutkan operasi dengan hasil ini? [y/n]: ").lower()
            if lanjut == "n":
                return False
            elif lanjut == "y":
                try:
                    operasi_lanjutan = input("Masukkan operasi (+, -, *, /): ")
                    angka_baru = self.get_number("Masukkan angka: ")

                    if operasi_lanjutan == "+":
                        self.result += angka_baru
                    elif operasi_lanjutan == "-":
                        self.result -= angka_baru
                    elif operasi_lanjutan == "*":
                        self.result *= angka_baru
                    elif operasi_lanjutan == "/":
                        if angka_baru == 0:
                            print("Tidak dapat membagi dengan nol!")
                            continue
                        self.result /= angka_baru
                    else:
                        print("Operasi tidak valid.")
                        continue

                    print(f"Hasil sementara: {self.result}")
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
            else:
                print("Input tidak valid. Masukkan 'y' atau 'n'.")
                continue

    def run(self):
        while True:
            self.clear_screen()
            print("=== KALKULATOR ===")

            angka1 = self.get_number("Masukkan angka pertama: ")
            angka2 = self.get_number("Masukkan angka kedua: ")
            operasi = self.get_operation()

            result = self.perform_operation(operasi, angka1, angka2)
            if result is None:
                input("Tekan Enter untuk melanjutkan...")
                continue

            self.result = result
            print(f"Hasil: {self.result}")

            if not self.continue_with_result():
                break

            opsi = input("Apakah ingin menghitung lagi? [Y/N]: ").upper()
            if opsi == "N":
                print("Terima kasih telah menggunakan kalkulator!")
                break


