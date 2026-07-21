import os
import yt_dlp

# 1. Şarkı listesini text dosyasından oku
txt_dosyasi = "songs.txt"

if not os.path.exists(txt_dosyasi):
    # Dosya yoksa örnek bir tane oluşturalım
    with open(txt_dosyasi, "w", encoding="utf-8") as f:
        f.write("Duman - Senden Daha Güzel\n")
    print(f"'{txt_dosyasi}' dosyası bulunamadı, boş bir tane oluşturuldu. İçini doldurup tekrar çalıştır.")
    exit()

with open(txt_dosyasi, "r", encoding="utf-8") as f:
    # Boş satırları ve satır başı/sonu boşluklarını temizleyerek listeye al
    sarki_isimleri = [satir.strip() for satir in f if satir.strip()]

# 2. yt-dlp Ayarları
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # 'ytsearch1:' kullandığımızda dosya adı bazen garip olabiliyor, o yüzden temiz bir isimlendirme yapıyoruz
    'outtmpl': '%(title)s.%(ext)s', 
}

# 3. Döngüye al ve ara-indir
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for sarki in sarki_isimleri:
        try:
            print(f"\n[Arama Yapılıyor ve İndiriliyor]: {sarki}")
            # 'ytsearch1:' ifadesi YouTube'da arayıp ilk sonucu seçmesini söyler
            ydl.download([f"ytsearch1:{sarki}"])
        except Exception as e:
            print(f"Hata oluştu ({sarki}): {e}")