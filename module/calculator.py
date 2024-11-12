def calculator():
    while True:
        
        print("calculator")
        angka1 = int(input("masukan angka pertama : ")) 
        angka2 = int(input("masukan angka kedua : ")) 
    
        input_data = int(input("pilih operasi yg ingin kamu lakukan \n1,tambah  \n2.kurang  \n3.kali \n4.bagi : "))
        
        if input_data == 1:
            tambah = angka1 + angka2
            print(f"hasil penjumlahan {angka1} + {angka2} adalah = {tambah} ")
        elif input_data == 2:
            kurang = angka1 - angka2
            print(f"hasil pengurangan {angka1} - {angka2} adalah = {kurang}")
        elif input_data == 3:
            kali = angka1 * angka2
            print(f"hasil perkalian {angka1} x {angka2} adalah = {kali}")
        elif input_data == 4:
            bagi = angka1 / angka2
            print(f"hasil pembagian pembagian {angka1} / {angka2} adalah = {bagi}")
        else :
            print("tidak ada opsi yg diinputkan")
    
        opsi = input("apakah ingin lanjut ? [y/n]")
        
        if opsi == "n":
           break

