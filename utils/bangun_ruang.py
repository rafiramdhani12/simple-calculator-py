import math

def kubus():
    print("Menghitung Volume dan Luas Permukaan Kubus")
    try:
        sisi = float(input("Masukkan panjang sisi kubus: "))
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        print(f"Volume kubus: {volume:.2f}")
        print(f"Luas permukaan kubus: {luas_permukaan:.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def balok():
    print("Menghitung Volume dan Luas Permukaan Balok")
    try:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = panjang * lebar * tinggi
        luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        print(f"Volume balok: {volume:.2f}")
        print(f"Luas permukaan balok: {luas_permukaan:.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def tabung():
    print("Menghitung Bangun Ruang Tabung")
    print('1. Volume Tabung \n2. Luas Permukaan Tabung \n3. Tinggi Tabung \n4. Jari-jari Tabung')
    try:
        option = int(input("Masukkan pilihan [1]/[2]/[3]/[4]: "))
        match option :
            case 1:
                radius = float(input("Masukkan jari-jari: "))
                tinggi = float(input("Masukkan tinggi tabung: "))
                volume = math.pi * (radius ** 2) * tinggi
                print(f"Volume tabung: {volume:.2f}")
            case 2:
                radius = float(input("Masukkan jari-jari: "))
                tinggi = float(input("Masukkan tinggi tabung: "))
                luas_permukaan = 2 * math.pi * radius * (radius + tinggi)
                print(f"Luas permukaan tabung: {luas_permukaan:.2f}")
            case 3:
                volume = float(input("Masukkan volume tabung: "))
                radius = float(input("Masukkan jari-jari: "))
                tinggi = volume / (math.pi * radius**2)
                print(f"Tinggi tabung: {tinggi:.2f}")
            case 4:
                volume = float(input("Masukkan volume tabung: "))
                tinggi = float(input("Masukkan tinggi tabung: "))
                radius = math.sqrt(volume / (math.pi * tinggi))
                print(f"Jari-jari tabung: {radius:.2f}")
            case _:
                print("pilihan tidak valid")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def kerucut():
    print("Menghitung Bangun Ruang Kerucut")
    print('1. Volume Kerucut \n2. Luas Permukaan Kerucut \n3. Tinggi Kerucut')
    try:
        option = int(input("Masukkan pilihan [1]/[2]/[3]: "))
        
        match option :
            case 1 :
                radius = float(input("Masukkan jari-jari: "))
                tinggi = float(input("Masukkan tinggi: "))
                volume = (1/3) * math.pi * (radius ** 2) * tinggi
                print(f"Volume kerucut: {volume:.2f}")
            case 2 :
                radius = float(input("Masukkan jari-jari: "))
                garis_pelukis = float(input("Masukkan panjang garis pelukis: "))
                luas_permukaan = math.pi * radius * (radius + garis_pelukis)
                print(f"Luas permukaan kerucut: {luas_permukaan:.2f}")
            case 3 :
                radius = float(input("Masukkan jari-jari: "))
                garis_pelukis = float(input("Masukkan panjang garis pelukis: "))
                tinggi = math.sqrt(garis_pelukis**2 - radius**2)
                print(f"Tinggi kerucut: {tinggi:.2f}")
            case _:
                print("pilihan tidak valid")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def bola():
    print("Menghitung Bangun Ruang Bola")
    print('1. Volume Bola \n2. Luas Permukaan Bola')
    try:
        option = int(input("Masukkan pilihan [1]/[2]: "))
        
        match option:
            case 1:
                radius = float(input("Masukkan jari-jari bola: "))
                volume = (4/3) * math.pi * (radius ** 3)
                print(f"Volume bola: {volume:.2f}")
            case 2:
                radius = float(input("Masukkan jari-jari bola: "))
                luas_permukaan = 4 * math.pi * (radius ** 2)
                print(f"Luas permukaan bola: {luas_permukaan:.2f}")
            case _:
                print("pilihan tidak valid")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
