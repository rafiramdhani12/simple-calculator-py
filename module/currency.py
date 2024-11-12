import requests

def currency_convert(api_key,from_currency,to_currency):
    url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    
    try:
        # ! request dari api
        res = requests.get(url)
        res.raise_for_status() # ! akan memunculkan error jika terjadi gagal
        
        # ! parsing data json dari response
        
        data =res.json()
        
        if "conversion_rates" in data and to_currency in data["conversion_rate"]:
            exchange_rate = data["conversion_rate"][to_currency]
            print(f"nilai tukar {from_currency} ke {to_currency} adalah {exchange_rate}")
            return exchange_rate
        else:
            print(f"mata uang {from_currency} tidak ditemukan")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"error : {e}")
        return None

while True:
    try:
        api_key = "ac4b392da76559bf767d4408"
        from_currency = input("masukkan mata uang awal : ")
        to_currency = input("masukkan mata uang tujuan : ")
        rate = currency_convert(api_key,from_currency,to_currency)

        if rate:
            amount = input("masukan nilai nya : ")
            convert_amount = amount * rate
            print(f"{amount} {from_currency} = {convert_amount} {to_currency}")
        else:
            print("input tidak valid")
    except KeyboardInterrupt:
        print(f"proggram dihentikan dengan paksa")
        
        
    continue_option = input("apakah kamu ingin melanjutkan ? :  [y]/[n]").upper()
    if continue_option == "N":
        break
