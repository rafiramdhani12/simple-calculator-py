konversi = {
   "1" : {"detik":lambda x: {"menit" : x / 60 , "jam" : x / 3600 , "hari" : x / 86400}},
   "2" : {"menit" : lambda x: {"detik" : x * 60 , "jam" : x / 60 , "hari" : x / 1440}},
   "3" : {"jam" : lambda x : {"detik" : x * 3600 , "menit" : x * 60 , "hari" : x / 24}},
}

from module.clear import clear
def tampilan():
    print(
        '''
        -------------------------------------
        |           Konversi Waktu          |
        |===================================|
        |   1.Detik     2.Menit     3.Jam   |   
        -------------------------------------   
        '''
    )
def waktu():
    print("Konversi Waktu")

    while True:
        clear()
        try:
            tampilan()
            data_input = input('pilih opsi [1]/[2]/[3] :')

            if data_input in konversi:
                satuan_waktu, fungsi_konversi = list(konversi[data_input].items())[0]
                nilai_waktu = float(input(f"Masukkan waktu dalam {satuan_waktu}: "))
                hasil = fungsi_konversi(nilai_waktu)

                for satuan, nilai in hasil.items():
                 print(f"{satuan_waktu} => {satuan} = {nilai}")
            else:
                 print("Pilihan tidak valid")
                 continue
        except KeyboardInterrupt:
            print("proggram dimatikan secara paksa")
            
            
        pilihan_lanjut = input("Apakah Anda ingin melanjutkan? [y/n] ").lower()
        if pilihan_lanjut == "n":
            return


