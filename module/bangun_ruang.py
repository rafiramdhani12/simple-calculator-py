from module.clear import clear
from utils.bangun_ruang import *
from utils.interface import geometry_interface

def bangun_ruang():
    clear()
    try:
        while True:
            
            geometry_interface()
            
            opsi = int(input("masukan opsi [1]/[2]/[3]/[4]/[5] atau [0] untuk keluar: "))
            
            clear()
            if opsi == 0:
                print("anda telah keluar dari proggram")
                break
            
            match opsi:
                case 1:
                    kubus()
                case 2:
                    balok()
                case 3:
                    tabung()
                case 4:
                    kerucut()
                case 5:
                    bola()
                    
            lanjut = input("Apakah Anda ingin melanjutkan? (Y/N): ").upper()
            if lanjut == 'N':
                print("Anda telah keluar dari program.")
                break
            
    except KeyboardInterrupt:
        print("anda telah keluar paksa dari proggram")
