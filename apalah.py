def test()->int:
   while True:
      print(eval(input("masukkan angka dan operasi : ")))
      opsi = input("apakah anda ingin lanjut ? [Y/N] ").upper()
      
      if opsi == "N":
         break
    
test()
