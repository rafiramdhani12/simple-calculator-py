konversi = {
   "1" : {"detik":lambda x: {"menit" : x / 60 , "jam" : x / 3600 , "hari" : x / 86400}},
   "2" : {"menit" : lambda x: {"detik" : x * 60 , "jam" : x / 60 , "hari" : x / 1440}},
   "3" : {"jam" : lambda x : {"detik" : x * 3600 , "menit" : x * 60 , "hari" : x / 24}},
}

from module.clear import clear
from utils.interface import time_interface
  
def waktu():
    print("Konversi Waktu")

    while True:
        clear()
        try:
            time_interface()
            data_input = input('pilih opsi [1]/[2]/[3] : ')

            if data_input in konversi: #! memeriksa apakah ada apakah data_input ada di konversi 
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
            
            
        pilihan_lanjut = input("Apakah Anda ingin melanjutkan? [Y/N] ").upper()
        if pilihan_lanjut == "N":
            break


