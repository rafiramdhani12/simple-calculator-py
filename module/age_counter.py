from module.clear import clear
import os
from dotenv import load_dotenv
import datetime
from groq import Groq

load_dotenv()

ai_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=ai_key)

def ai_call(year):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role" : "user" , "content" : f"berikan saya 2 fakta unik dan menarik yg terjadi di tahun {year}"}],
            model="llama-3.2-1b-preview",
            stream=False
        )
        ai_output = chat_completion.choices[0].message.content
        return ai_output
    except Exception as e:
        return f"\nmaaf fitur ai saat ini sedang tidak bisa digunakan , ERROR: {e}"


def age_counter():
    clear()    
    while True:
        try:
            tahun_lahir = int(input("masukan tahun lahir mu : "))
            tahun_sekarang = datetime.datetime.now().year
            usia = tahun_sekarang - tahun_lahir
            
            ai_output = ai_call(tahun_lahir)
            
            print(f"usia mu skrg adalah {usia}")
            print(f"fakta menarik di tahun {tahun_lahir} adalah {ai_output}")
            
        except KeyboardInterrupt:
            print("\nanda telah keluar paksa dari program")
        
        option = input("apakah anda ingin melanjutkan ? [Y?N]").upper()
        if option == "N":
            break
        