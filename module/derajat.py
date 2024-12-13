konversi = {
    "1" : {"celcius": lambda x : {"fahrenheit" : (x * 9/5) +32 , "kelvin" : x + 273.15 , "reamur" : 4/5 * x}},
    "2" : {"fahrenheit": lambda x : {"celcius" : (x - 32) * 5/9 , "kelvin" : (x - 32 ) * 5/9 + 273.15 , "reamur" : (x - 32) * 4/5 }},
    "3" : {"kelvin": lambda x : {"celcius" : x - 273.15 , "fahrenheit" : (x - 273.15) * 5/9 + 32 , "reamur" :(x - 273.15) * 4/5  }},
    "4" : {"reamur": lambda x : {"celcius" : x * 5/4 , "kelvin" : (x * 5/4) + 273.15 , "fahrenheit" : (x * 5/4) + 32}},
}

from module.clear import clear

def derajat():
    while True:
        try:
            clear()
            print("Konversi Suhu")
            data_input = input('Pilih suhu yang ingin dikonversi \n1. Celcius \n2. Fahrenheit \n3. Kelvin \n4. Reamur \nPilih salah satu: [1]/[2]/[3]/[4] :')
            
            if data_input in konversi:
                    suhu , fungsi_konversi = list(konversi[data_input].items())[0]
                    nilai_suhu = float(input(f"masukan suhu dalam {suhu} : "))
                    hasil = fungsi_konversi(nilai_suhu)
                    
                    for satuan, nilai in hasil.items():
                        print(f"{suhu} => {satuan} = {nilai}")
            else:
                    print("Pilihan tidak valid.")
                    continue
        except KeyboardInterrupt:
            print("proggram dihentikan secara paksa")

        
        continue_choice = input("\nApakah Anda ingin melakukan konversi lagi? (Y/N): ").upper()
        if continue_choice.lower() == "N":
            break
    


