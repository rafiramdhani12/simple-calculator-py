nilai_tukar = {
    "rupiah_to_dollar": 0.000065,
    "rupiah_to_yen": 0.009,
    "rupiah_to_poundsterling": 0.000054,
    "rupiah_to_ringgit": 0.00029,
    "dollar_to_rupiah": 15380,
    "dollar_to_yen": 145.3,
    "dollar_to_poundsterling": 0.81,
    "dollar_to_ringgit": 4.43,
    "yen_to_rupiah": 147.5,
    "yen_to_dollar": 0.0069,
    "yen_to_poundsterling": 0.0056,
    "yen_to_ringgit": 0.031,
    "poundsterling_to_rupiah": 18500,
    "poundsterling_to_dollar": 1.23,
    "poundsterling_to_yen": 178.5,
    "poundsterling_to_ringgit": 5.47,
    "ringgit_to_rupiah": 3483,
    "ringgit_to_dollar": 0.23,
    "ringgit_to_yen": 22.33,
    "ringgit_to_poundsterling": 0.18
}


def rupiah(amount):
    return{
        "dollar" : amount * nilai_tukar["rupiah_to_dollar"],
        "yen" : amount * nilai_tukar["rupiah_to_yen"],
        "poundsterling" : amount * nilai_tukar["rupiah_to_poundsterling"],
        "ringgit" : amount * nilai_tukar["rupiah_to_ringgit"]
    }

def dollar(amount):
    return{
        "rupiah" : amount * nilai_tukar["dollar_to_rupiah"],
        "yen": amount* nilai_tukar["dollar_to_yen"],
        "poundsterling": amount * nilai_tukar["dollar_to_poundsterling"],
        "ringgit" : amount * nilai_tukar["dollar_to_ringgit"]
    }

def yen(amount):
    return{
        "rupiah" : amount * nilai_tukar["yen_to_rupiah"],
        "dollar" : amount * nilai_tukar["yen_to_dollar"],
        "ringgit" : amount * nilai_tukar["yen_to_ringgit"],
        "poundsterling" : amount * nilai_tukar["yen_to_poundsterling"]
    }

def poundsterling(amount):
    return{
        "rupiah" : amount * nilai_tukar["poundsterling_to_rupiah"],
        "dollar" : amount * nilai_tukar["poundsterling_to_dollar"],
        "ringgit" : amount * nilai_tukar['poundsterling_to_ringgit'],
        "yen" : amount * nilai_tukar["poundsterling_to_yen"]
    }

def ringgit(amount):
    return{
        "rupiah" : amount * nilai_tukar["ringgit_to_rupiah"],
        "yen": amount* nilai_tukar["ringgit_to_yen"],
        "poundsterling": amount * nilai_tukar["ringgit_to_poundsterling"],
        "dollar" : amount * nilai_tukar["ringgit_to_dollar"]
    }

def currency_conversion():
    print("konversi mata uang")
    
    while True:
        from_currency = input("masukan mata uang asal (rupiah/dollar/yen/poundsterling/ringgit) : ")
        amount =  float(input(f"masukan jumlah uang dalam {from_currency} : "))
        to_currency = input("masukan mata uang tujuan (rupiah/dollar/yen/poundsterling/ringgit) : ")
        
        if from_currency == "rupiah":
            result = rupiah(amount)
        elif from_currency == "dollar":
            result = dollar(amount)
        elif from_currency == "yen":
            result= yen(amount)
        elif from_currency == "poundsterling":
            result = poundsterling(amount)
        elif from_currency == "ringgit":
            result = ringgit(amount)
        else:
            print("mata uang tidak ada / tidak valid")
            continue
        
        if to_currency in result:
            print(f"{amount} {from_currency} = {result[to_currency]:.2f} {to_currency}")
        else:
            print("mata uang tujuan tidak valid")
        
        continue_option = input("apakah masih ingin dilanjut : [y/n]").lower()
        if continue_option == "n":
            return
