# 🌟 Project akhir samester 1

![Status](https://img.shields.io/badge/status-Act/ive-blue)

ini adalah projek akhir semester tema sains (matematika) dengan menggunakan python kami kelompok 8 membuat proggram
kalkulator sederhana sekali

## Nama Kelompok

| Nama                     | nim      | kelas    |
| ------------------------ | -------- | -------- |
| Muhammad Rafi Ramdhani   | 15240411 | 15.1A.04 |
| Maeyumedi Davi           | 15240975 | 15.1A.04 |
| Muhammad Akbar Ghozali   | 15240313 | 15.1A.04 |
| Jeremy Febrian Manuputty | 15240505 | 15.1A.04 |
| Arya Kurniawan           | 15240661 | 15.1A.04 |

## 📸 Screenshot

![Tampilan Proyek](/projek.jpg)

## 🚀 Fitur

- ⚡ mudah dimengerti karena masih menggunakan py native dan menggunakan sintaks yg mudah dibaca

## 🛠 Instalasi

```bash
git clone https://github.com/username/proyek.git
cd proyek
py main.py
```

## 📝 Notes

- currency tidak akan bisa dipakai oleh orang lain karena itu menggunakan api dan api key nya milik creator
- jika kalian tetap ingin mencoba silahkan kalian kunjungi web v6.exchangerate-api.com untuk membuat api key
- berikut adalah cara menggunakanya

  ```bash
  pip install python-dotenv requests
  setelah itu lakukan seperti ini
  import requests
  from dotenv import load_dotenv
  from module.clear import clear
  import os

  # ! muat / memanggil variable lingkungan dari .env
  load_dotenv()

  def currency_conversion():
    clear()
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("api key tidak ditemukan , pastikan disimpan di .env")
        return
    try:
        while True:
            from_currency = input("masukan mata uang asal (contoh USD) : ").upper()
            to_currency = input("masukan mata uang tujuan (contoh IDR) : ").upper()
            url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
            


  ```

⬜⬜⬛⬛⬛⬛  
⬜⬜⬜⬛⬛⬛  
⬜🔳⬜⬜🔳⬜  
⬜⬜⬜⬜⬜⬜  
⬜⬜⬛⬛⬜⬜  
⬜⬜⬜⬜⬜⬜
