from module.clear import clear

def calculator()->int:
    while True:
        try:
            clear()
            print("=== KALKULATOR ===")
            
            print(eval(input("masukkan angka dan operasi yg ingin anda lakukan = ")))
            
        except KeyboardInterrupt:
            print("\nkeluar dari proggram secara paksa")
        
        
        opsi = input("Apakah ingin menghitung lagi? [Y/N]: ").upper()
        if opsi == "N":
            print("Terima kasih telah menggunakan kalkulator!")
            break

