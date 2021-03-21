from plyer import notification
import time
import random
import webbrowser
from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.GREEN+"""
+----------------------------------------------------------+
|                                                          |
|    '||''''|                   '||           ||    .      |
|     ||  .    ... ... ... ...   ||    ...   ...  .||.     |
|     ||''|     '|..'   ||'  ||  ||  .|  '|.  ||   ||      |
|     ||         .|.    ||    |  ||  ||   ||  ||   ||      |
|    .||.....| .|  ||.  ||...'  .||.  '|..|' .||.  '|.'    |
|                       ||                                 |
|                      ''''   Coded By EYLL' - arda6       |
+----------------------------------------------------------+                   
""")
print(Style.RESET_ALL)
print(Fore.BLUE+"""


8888888b.                                                888                              
888   Y88b                                               888                              
888    888                                               888                              
888   d88P .d88b. 888  888 .d88b. 888d888.d8888b  .d88b. 888      .d88b. 888  888 .d88b.  
8888888P" d8P  Y8b888  888d8P  Y8b888P"  88K     d8P  Y8b888     d88""88b888  888d8P  Y8b 
888 T88b  88888888Y88  88P88888888888    "Y8888b.88888888888     888  888Y88  88P88888888 
888  T88b Y8b.     Y8bd8P Y8b.    888         X88Y8b.    888     Y88..88P Y8bd8P Y8b.     
888   T88b "Y8888   Y88P   "Y8888 888     88888P' "Y8888 88888888 "Y88P"   Y88P   "Y8888  
                                                                                          
                                                                                        
                                                                            Coded By EYLL' - arda6        
                                                                               
""")
print(Style.RESET_ALL)
name = str(Fore.WHITE+input("O'nun Adı Nedir ? "))
str(name)
time.sleep(3)
print("Sızılcak Kalp "+name+ " Olarak Ayarlandı .")
love = str(input("Senin Adın Nedir ? "))
str(love)
time.sleep(3)
print("Geri Bağlantı " +love+" Olarak Ayarlandı . Bol Şans =)")
print(Style.RESET_ALL)
exploit = str(random.randint(1,2))
print(exploit)
if exploit == '1':
    print(Fore.YELLOW+"Istek Gönderildi.")
    print("Yanıt Bekleniyor......")
    time.sleep(3)
    print("Yanıt Geldi. Paket Inceleniyor....")
    time.sleep(4)
    print("Paket İncelendi. Güvenlik Duvarı Kontrol Ediliyor....")
    time.sleep(5)
    print("Kontrol Edildi. Her Şey Yolunda. Istek Gönderiliyor....")
    time.sleep(3)
    print("Gelen Paket İncelendi. Şifrelenmiş Giriş Bulunmakta. Şifre Kırma Işlemi Başlatılıyor... ")
    time.sleep(4)
    print("İşlemler Tamamlandı.\nŞifre :")
    print(love)
    print(Fore.GREEN + "Exploit İşlemi Başarılı.... \U0001F600 \n")
    time.sleep(3)
    notification.notify(
        title = "Exploit",
        message = "Exploit Işlemi Başarılı",
        timeout = 10
    )
    print("Onu Daha Fazla Bekletmeden DM At ")
    webbrowser.open("https://wwww.instagram.com")
elif exploit == '2':
    print(Fore.YELLOW + "Istek Gönderildi.")
    print("Yanıt Bekleniyor......")
    time.sleep(3)
    print("Yanıt Geldi. Paket Inceleniyor....")
    time.sleep(4)
    print("Paket İncelendi. Güvenlik Duvarı Kontrol Ediliyor....")
    time.sleep(5)
    print("Kontrol Edildi. Düşük Şans . Istek Gönderiliyor....")
    time.sleep(3)
    print("Gelen Paket İncelendi. Şifrelenmiş Giriş Bulunmakta. Şifre Kırma Işlemi Başlatılıyor... ")
    time.sleep(4)
    print("İşlemler Tamamlanamadı.\nHata :")
    sayac = 0
    sad = "Ismın Ile Şifre Eşleşmedi. Üzgünüm."
    print(sad)
    print(Fore.GREEN + "Exploit İşlemi Başarısız. Başkası Daha Önce Girmiş Ve "" " +name+ " "" Seni İçeri Almıyor. ""\U0001F62A \n")
    time.sleep(3)
    notification.notify(
        title="Exploit",
        message="Işlem Başarısız. Üzgünüm.",
        timeout=10
    )
    time.sleep(4)
    webbrowser.open("https://www.youtube.com/watch?v=CZjdL6bC3wg")






