def derajat():
    print("Konversi Suhu")
    
    while True:
        data_input = input('''
        Pilih suhu yang ingin dikonversi:
        1. Celcius
        2. Fahrenheit
        3. Kelvin
        4. Reamur
        Pilih salah satu: [1]/[2]/[3]/[4]
        ''')

        if data_input == "1":
            c = float(input("Masukkan derajat Celcius: "))
            f = (c * 9/5) + 32
            k = c + 273.15
            r = 4/5 * c
            print(f"Celcius => Fahrenheit = {f} \nCelcius => Kelvin = {k} \nCelcius => Reamur = {r}")
            
        elif data_input == "2":
            f = float(input("Masukkan derajat Fahrenheit: "))
            c = (f - 32) * 5/9
            k = (f - 32) * 5/9 + 273.15
            r = (f - 32) * 4/9
            print(f"Fahrenheit => Celcius = {c} \nFahrenheit => Kelvin = {k} \nFahrenheit => Reamur = {r}")

        elif data_input == "3":
            k = float(input("Masukkan derajat Kelvin: "))
            c = k - 273.15
            f = (k - 273.15) * 9/5 + 32
            r = (k - 273.15) * 4/5
            print(f"Kelvin => Celcius = {c} \nKelvin => Fahrenheit = {f} \nKelvin => Reamur = {r}")

        elif data_input == "4":
            r = float(input("Masukkan derajat Reamur: "))
            c = r * 5/4
            f = (r * 9/4) + 32
            k = (r * 5/4) + 273.15
            print(f"Reamur => Celcius = {c} \nReamur => Fahrenheit = {f} \nReamur => Kelvin = {k}")

        else:
            print("Pilihan tidak valid.")
            continue

        # Ask user if they want to continue or exit
        continue_choice = input("Apakah Anda ingin melakukan konversi lagi? (y/n): ")
        if continue_choice.lower() == 'n':
            return
