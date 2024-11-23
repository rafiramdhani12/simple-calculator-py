from module.clear import clear

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
    try:
        clear()
        while True:
            
            tampilan()
            
            opsi = int(input("masukan opsi [1]/[2]/[3]/[4] : "))
            
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
                V =3.14 * r ** 2 *t
                luas_permukaan = 2 * 3.14 * r * (r+t)
                print(f"volume tabung : {V:.3f}")
                print(f"luas permukaan : {luas_permukaan:.3f}")
            elif opsi == 4:
                print("menghitung volume dan luas permukaan kerucut")
                r = float(input("jari-jari : "))
                t = float(input("tinggi : "))
                s = float(input(""))
                V = (1/3) * 3.14 *r **2 *t
                luas_permukaan = 3.14 * r* (r+s)
                print(f"Volume kerucut : {V:.3f}")
                print(f"luas permukaan : {luas_permukaan:.3f}")
            else:
                print("opsi tidak valid silahkan masukan opsi yg lain")
    except KeyboardInterrupt:
        print("anda telah keluar paksa dari proggram")
