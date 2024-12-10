from module.clear import clear

def calculator():
    while True:
        clear()
        print("=== KALKULATOR ===")
        
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")
            continue

        operasi = int(input("Pilih operasi: \n1. +  (penjumlahan)\n2. -  (pengurangan)\n3. *  (perkalian)\n4. /  (pembagian)\nMasukkan pilihan: "))
        
        match operasi:
            case 1:
                result = angka1 + angka2
            case 2:
                result = angka1 - angka2
            case 3:
                result = angka1 * angka2
            case 4:
                result = angka1 / angka2
                if angka2 == 0:
                    print("tidak dapat membagi dengan nol")
                    print("tekan enter untuk melanjutkan")
                    continue
            case _:
                print("operasi tidak valid")
                input("Tekan Enter untuk melanjutkan...")
                continue
                

        print(f"Hasil: {result}")

        # Lanjutkan operasi dengan hasil sementara
        while True:
            lanjut = input("Apakah ingin melanjutkan operasi dengan hasil ini? [y/n]: ") 
            if lanjut == "n":
                break
            elif lanjut == "y":
                try:
                    operasi_lanjutan = input("Masukkan operasi (+, -, *, /): ")
                    angka_baru = float(input("Masukkan angka: "))
                    
                    if operasi_lanjutan == "+":
                        result += angka_baru
                    elif operasi_lanjutan == "-":
                        result -= angka_baru
                    elif operasi_lanjutan == "*":
                        result *= angka_baru
                    elif operasi_lanjutan == "/":
                        if angka_baru == 0:
                            print("Tidak dapat membagi dengan nol!")
                            continue
                        result /= angka_baru
                    else:
                        print("Operasi tidak valid.")
                        continue
                    
                    print(f"Hasil sementara: {result}")
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
            else:
                print("Input tidak valid. Masukkan 'y' atau 'n'.")
                continue
        
        opsi = input("Apakah ingin menghitung lagi? [y/n]: ").lower()
        if opsi == "n":
            print("Terima kasih telah menggunakan kalkulator!")
            break

