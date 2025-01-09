from module.clear import clear
from utils.bangun_ruang import *
from utils.interface import geometry_interface

def bangun_ruang():
    clear()
    while True:
        try:
            
            geometry_interface()
            
            try:
                opsi = int(input("masukan opsi [1]/[2]/[3]/[4] atau [0] untuk keluar: "))
            
                clear()
                
                match opsi:
                    case 1:
                        kubus()
                    case 2:
                        balok()
                    case 3:
                        tabung()
                    case 4:
                        bola()
                    case 0:
                        break
                    case _:
                        print("opsi tidak ada silahkan masukan nomor yg ada")
            except ValueError:
                break
            
        except KeyboardInterrupt:
         print("anda telah keluar paksa dari proggram")

        lanjut = input("Apakah Anda ingin melanjutkan proggram hitung bangun ruang ? [Y/N]: ").upper()
        if lanjut == 'N':
            print("Anda telah keluar dari program.")
            break
