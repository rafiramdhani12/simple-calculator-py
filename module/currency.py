import requests
from dotenv import load_dotenv
from module.clear import clear
from utils.interface import curreny_interface
import os

# ! muat / memanggil variable lingkungan dari .env
load_dotenv()

def currency_conversion()->float:
    clear()
    api_key = os.getenv("API_KEY")
    
    # ! jika tidak ada api key nya maka akan error
    if not api_key:
        print("api key tidak ditemukan , pastikan disimpan di .env")
        return
    
    while True:
            try:
                curreny_interface()
                from_currency = input("masukan mata uang asal (contoh USD) : ").upper()
                to_currency = input("masukan mata uang tujuan (contoh IDR) : ").upper()
                url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
                
                try:
                    res = requests.get(url)
                    res.raise_for_status()
                    data= res.json()
                    
                    # ! melakukan pencarian di api jika ada maka lakukan perintah dibawah
                    if "conversion_rates" in data and to_currency in data["conversion_rates"]:
                        exchange_rate = data["conversion_rates"][to_currency]
                        print(f"Kurva nilai tukar {from_currency} ke {to_currency} adalah {exchange_rate}")
                        
                        # ! lakukan konversi
                        amount = float(input("masukkan nilai yg ingin di konversi : "))
                        converted_amount = amount * exchange_rate
                        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
                    else:
                        print("mata uang tujuan tidak ditemukan")
                    
                    
                except requests.exceptions.RequestException as e:
                    print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nanda telah keluar paksa dari proggram")
                
            opsi = input("apakah anda ingin melanjutkan proggram konversi nya ? [Y/N] : ").upper()

            if opsi == "N":
                break
                    
