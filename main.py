from module.calculator import calculator
from module.derajat import derajat
from module.currency import currency_conversion
from module.waktu import waktu

def main():
      while True:
        option = int(input(" masukan opsi yang anda ingin lakukan \n1. calculator \n2. suhu \n3. waktu \n4. mata uang \npilih opsi [1]/[2]/[3]/[4] : "))    
        if option == 1 :
            calculator()
        elif option == 2 :
            derajat()
        elif option == 3:
            waktu()
        elif option == 4 :
            currency_conversion()
        else :
            print("opsi yg anda masukan tidak valid / tidak ada")
            continue
            
        opsi_lanjut = input("kamu telah kembali ke halaman utama apakah kamu ingin melanjutkan ? [y/n]").lower()
        
        if opsi_lanjut == "n":
            break

print("proggram sudah selesai")

if __name__ == ("__main__"):
    main()
  
