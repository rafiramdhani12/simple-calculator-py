from module.calculator import calculator
from module.currency import currency_conversion
from module.bangun_ruang import bangun_ruang
from module.clear import clear
from utils.interface import main_interface


def main():
    try:
        while True:
                clear()
                main_interface()
                option = int(input("Masukan opsi yang anda ingin lakukan, pilih opsi [1]/[2]/[3] [0] untuk keluar : ")) 
                match option:
                    case 1:
                        calculator()
                    case 2:
                        currency_conversion()
                    case 3:
                        bangun_ruang()
                    case 0:
                        exit()
                    case _:
                        print("opsi yg anda masukkan tidak valid / tidak ada")
                        continue        
                opsi_lanjut = input("kamu telah kembali ke halaman utama apakah kamu ingin melanjutkan ? [Y/N]").upper()
                
                if opsi_lanjut == "N":
                    break
    except KeyboardInterrupt:
        print("\nanda telah keluar paksa dari proggram")

print("proggram sudah selesai")

if __name__ == ("__main__"):
    main()
  