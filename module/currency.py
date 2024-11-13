import os 
import requests
from dotenv import load_dotenv

# ! muat / memanggil variable lingkungan dari .env
load_dotenv()

def currency_conversion():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("api key tidak ditemukan , pastikan disimpan di .env")
        return
    
    from_currency = input("masukan mata uang asal (contoh USD) : ").upper()
    to_currency = input("masukan mata uang tujuan (contoh IDR) : ").upper()
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    
    try:
        
        res = requests.get(url)
        res.raise_for_status()
        data= res.json()
        
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
