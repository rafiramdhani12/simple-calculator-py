from module.calculator import calculator
from module.derajat import derajat
from module.currency import currency_conversion
from module.waktu import waktu
from module.bangun_ruang import bangun_ruang
from module.clear import clear

def main():
    try:
        while True:
                clear()
                print('''
                |=========================================================================================|
                |   1. Calculator       2.Suhu            3.Waktu       4.Mata uang     5.Bangun ruang    |
                |-----------------------------------------------------------------------------------------|
                |                                                                                         |
                |   -Perkalian          -Celcius          -Detik        -Rupiah         -Kubus            |
                |   -Pertambahan        -Kelvin           -Menit        -Dollar         -Balok            |
                |   -Pembagian          -Fahrenheit       -Jam          -Yen            -Tabung           |
                |   -Pengurangan        -Reamur                                         -Kerucut          |
                |                                                                                         |
                |=========================================================================================|
                ''')
                option = int(input("Masukan opsi yang anda ingin lakukan, pilih opsi [1]/[2]/[3]/[4]/[5] : "))    
                if option == 1 :
                    calculator()
                elif option == 2 :
                    derajat()
                elif option == 3:
                    waktu()
                elif option == 4 :
                    currency_conversion()
                elif option == 5 :
                    bangun_ruang()   
                else :
                    print("opsi yg anda masukan tidak valid / tidak ada")
                    continue
                    
                opsi_lanjut = input("kamu telah kembali ke halaman utama apakah kamu ingin melanjutkan ? [y/n]")
                
                if opsi_lanjut == "n":
                    break
    except KeyboardInterrupt:
        print("\nanda telah keluar paksa dari proggram")

print("proggram sudah selesai")

if __name__ == ("__main__"):
    main()
  