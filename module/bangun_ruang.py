from module.clear import clear
from utils.bangun_ruang import *
import math

def tampilan():
    print(
    '''
    ----------------------------------------------------------------------------
    |                                 Bangun ruang                             |
    ===========================================================================|
    |   1.Kubus         2.Balok     3.Tabung        4.Kerucut       5.Bola     |
    ----------------------------------------------------------------------------
    ''')

def bangun_ruang():
    clear()
    try:
        while True:
            
            tampilan()
            
            opsi = int(input("masukan opsi [1]/[2]/[3]/[4]/[5] atau [0] untuk keluar: "))
            
            clear()
            if opsi == 0:
                print("anda telah keluar dari proggram")
                break

            if opsi == 1:
               kubus()

            elif opsi == 2:
                balok()

            elif opsi ==3:
               tabung()
                    
            elif opsi == 4:
               kerucut()

            elif opsi == 5:
                bola()

            lanjut = input("Apakah Anda ingin melanjutkan? (Y/N): ").upepr()
            if lanjut == 'N':
                print("Anda telah keluar dari program.")
                break
            
    except KeyboardInterrupt:
        print("anda telah keluar paksa dari proggram")
