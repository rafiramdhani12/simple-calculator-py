import math 
def kubus():
    print("menghitung volume kubus")
    s = int(input("masukan panjang sisi kubus : "))
    V = s**3
    luas_permukaan = 6 * s ** 2
    print(f"volume kubus : {V}")
    print(f"luas permukaan kubus : {luas_permukaan}")

def balok():
    print("menghitung volume dan luas balok")
    p= int(input("masukkan panjang balok: "))
    l= int(input("masukkan lebar balok : "))
    t= int(input("masukkan tinggi balok : "))
    V = p * l * t
    luas_permukaan = 2 * (p * l + p * t + l *t)
    print(f"Volume balok : {V}")
    print(f"luas permukaan : {luas_permukaan}")
    
def tabung():
    print("menghitung bangun ruang tabung")
    print('''
          1.Volume tabung
          2.Luas permukaan tabung
          3.Tinggi tabung
          4.Jari-jari tabung
    ''')
    pilihan = int(input("Masukan pilihan [1]/[2]/[3]/[4] : "))

    if pilihan == 1:
        r = float(input("masukkan jari-jari : "))
        t = float(input("masukkan tinggi tabung : "))
        V =3.14 * (r ** 2) *t
        print(f"volume tabung : {V:.2f}")

    elif pilihan == 2:
        r = float(input("masukkan jari-jari : "))
        t = float(input("masukkan tinggi tabung : "))
        luas_permukaan = 2 * 3.14 * r * (r+t)
        print(f"luas permukaan : {luas_permukaan:.2f}")

    elif pilihan == 3 :
        volume = int(input("Masukan Volume tabung :"))
        r = float(input("Masukan jari-jari : "))
        tinggi = volume / (3.14 * r**2)
        print(f"tinggi tabung : {tinggi:.2f} ")
                
    elif pilihan == 4 :
        volume = int(input("Masukan Volume tabung : "))
        tinggi = float(input("Masukan tinggi tabung : "))
        r = math.sqrt (volume/(math.pi * tinggi))
        print(f"Jari-jari tabung : {r:.2f}")
                
    else:
        print("Input tidak sesuai!")

def kerucut():
    print("Menghitung bangun ruang kerucut")
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
        print(f"Tinggi kerucut adalah {h:.2f}")
                
    else:
        print("Opsi yang anda masukan salah!")

def bola():
    print("Menghitung bangun ruang Bola")
    print('''
                    1.Volume bola
                    2.Luas permukaan bola          
                ''')
    choice =int(input("Masukan pilihan [1]/[2] : "))
                
    if choice == 1:
        r = float(input("Masukan jari-jari bola : "))
        volume = (4/3) * math.pi * r**3
        print(f"Volume bola adalah : {volume:.2f}")

        if choice == 2:
            r = float(input("Masukan jari-jari bola : "))
            A = 4 * math.pi * (r**2)
            print(f"Luas permukaan bola adalah : {A:.2f}")
                
        else:
            print("opsi tidak valid silahkan masukan opsi yg lain")
                
    else:
        print("opsi tidak valid silahkan masukan opsi yg lain")
