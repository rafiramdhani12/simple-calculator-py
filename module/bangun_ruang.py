from module.clear import clear
import math

def tampilan():
    print(
    '''
    -----------------------------------------------------------------
    |                         Bangun ruang                          |
    =================================================================
    |   1.Kubus         2.Balok     3.Tabung        4.Kerucut       |
    -----------------------------------------------------------------
    ''')

def bangun_ruang():
    clear()
    try:
        while True:
            
            tampilan()
            
            opsi = int(input("masukan opsi [1]/[2]/[3]/[4] : "))
            
            clear()
            if opsi == 0:
                print("anda telah keluar dari proggram")
                break

            if opsi == 1:
                print("menghitung volume balok")
                s = int(input("masukan panjang sisi kubus : "))
                V = s**3
                luas_permukaan = 6 * s ** 2
                print(f"volume kubus : {V}")
                print(f"luas permukaan kubus : {luas_permukaan}")

            elif opsi == 2:
                print("menghitung volume dan luas balok")
                p= int(input("masukkan panjang balok: "))
                l= int(input("masukkan lebar balok : "))
                t= int(input("masukkan tinggi balok : "))
                V = p * l * t
                luas_permukaan = 2 * (p * l + p * t + l *t)
                print(f"Volume balok : {V}")
                print(f"luas permukaan : {luas_permukaan}")

            elif opsi ==3:
                print("menghitung volume dan luas tabung")
                r = float(input("masukkan jari-jari : "))
                t = float(input("masukkan tinggi tabung : "))
                V =3.14 * (r ** 2) *t
                luas_permukaan = 2 * 3.14 * r * (r+t)
                print(f"volume tabung : {V:.2f}")
                print(f"luas permukaan : {luas_permukaan:.2f}")

            elif opsi == 4:
                print("Menghitung rumus kerucut")
                print('''
                        1.Volume kerucut
                        2.Luas permukaan kerucut
                        3.Tinggi kerucut
                        ''')
                pilihan = int(input("Bagian yang dicari [1]/[2]/[3]/[4] : "))

                if pilihan == 1:
                    r = float(input("jari-jari : "))
                    t = float(input("tinggi : "))
                    V = (1/3) * 3.14 *r **2 *t
                    print(f"Volume kerucut : {V:.2f}")

                elif pilihan == 2:
                    r = float(input("jari-jari : "))
                    s = float(input("Panjang garis pelukis : "))
                    l = float(input("Luas permukaan : "))
                    luas_permukaan = 3.14 * r* (r+s)
                    print(f"luas permukaan : {luas_permukaan:.2f}")

                elif pilihan == 3:
                    r = float(input("Jari-jari : "))
                    s = float(input("Panjang garis pelukis : "))
                    h = math.sqrt (s**2 - r**2)
                    # math.sqrt berfungsi sebagai akar kuadrat dari module math
                    print(f"Tinggi kerucut adalah {h}")
                
                else:
                    print("Opsi yang anda masukan salah!")

            else:
                print("opsi tidak valid silahkan masukan ops i yg lain")

    except KeyboardInterrupt:
        print("anda telah keluar paksa dari proggram")
