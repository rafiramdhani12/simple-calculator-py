def detik(d):
    return {
        "menit": d // 60,
        "jam": d // 3600,
        "hari": d // 86400,
        "minggu": d // 604800,
        "bulan": d // 2592000,  # asumsi 30 hari per bulan
        "tahun": d // 31536000  # asumsi 365 hari per tahun
    }

def menit(m):
    return {
        "detik": m * 60,
        "jam": m // 60,
        "hari": m // 1440,      # 1 hari = 1440 menit
        "minggu": m // 10080,   # 1 minggu = 10080 menit
        "bulan": m // 43200,    # asumsi 1 bulan = 43200 menit (30 hari)
        "tahun": m // 525600    # asumsi 1 tahun = 525600 menit (365 hari)
    }

def jam(j):
    return {
        "detik": j * 3600,
        "menit": j * 60,
        "hari": j // 24,
        "minggu": j // 168,     # 1 minggu = 168 jam
        "bulan": j // 720,      # asumsi 1 bulan = 720 jam (30 hari)
        "tahun": j // 8760      # asumsi 1 tahun = 8760 jam (365 hari)
    }

def hari(h):
    return {
        "detik": h * 86400,     # 1 hari = 86400 detik
        "menit": h * 1440,      # 1 hari = 1440 menit
        "jam": h * 24,          # 1 hari = 24 jam
        "minggu": h / 7,        # 1 minggu = 7 hari
        "bulan": h / 30,        # asumsi 1 bulan = 30 hari
        "tahun": h / 365        # asumsi 1 tahun = 365 hari
    }

def minggu(w):
    return {
        "detik": w * 604800,    # 1 minggu = 604800 detik
        "menit": w * 10080,     # 1 minggu = 10080 menit
        "jam": w * 168,         # 1 minggu = 168 jam
        "hari": w * 7,
        "bulan": w / 4.345,     # rata-rata bulan dalam minggu
        "tahun": w / 52.143     # rata-rata tahun dalam minggu
    }

def bulan(b):
    return {
        "detik": b * 2592000,   # 1 bulan = 2592000 detik (asumsi 30 hari)
        "menit": b * 43200,     # 1 bulan = 43200 menit
        "jam": b * 720,         # 1 bulan = 720 jam
        "hari": b * 30,
        "minggu": b * 4.345,    # rata-rata minggu dalam bulan
        "tahun": b / 12         # 1 tahun = 12 bulan
    }

def tahun(y):
    return {
        "detik": y * 31536000,  # 1 tahun = 31536000 detik (asumsi 365 hari)
        "menit": y * 525600,    # 1 tahun = 525600 menit
        "jam": y * 8760,        # 1 tahun = 8760 jam
        "hari": y * 365,
        "minggu": y * 52.143,   # rata-rata minggu dalam tahun
        "bulan": y * 12
    }

konversi = {
    "1": {"detik": detik},
    "2": {"menit": menit},
    "3": {"jam": jam},
    "4": {"hari": hari},
    "5": {"minggu": minggu},
    "6": {"bulan": bulan},
    "7": {"tahun": tahun}
}

def waktu():
    print("Konversi Waktu")

    while True:
        data_input = input('''
            Pilih yang ingin dikonversi:
            1. detik
            2. menit
            3. jam
            4. hari
            5. minggu
            6. bulan
            7. tahun
        ''')

        if data_input in konversi:
            satuan_waktu, fungsi_konversi = list(konversi[data_input].items())[0]
            nilai_waktu = float(input(f"Masukkan waktu dalam {satuan_waktu}: "))
            hasil = fungsi_konversi(nilai_waktu)

            for satuan, nilai in hasil.items():
                print(f"{satuan_waktu} => {satuan} = {nilai}")
        else:
            print("Pilihan tidak valid")
            continue

        pilihan_lanjut = input("Apakah Anda ingin melanjutkan? [y/n] ").lower()
        if pilihan_lanjut == "n":
            return
