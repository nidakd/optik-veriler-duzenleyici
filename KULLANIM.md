# Veri Düzenleyici - Kullanım Kılavuzu

## 📋 Ne İşe Yarar?

Bu script, birden fazla web sayfasından kopyaladığınız optik firma verilerini:
- Otomatik olarak okur
- Temizler ve düzenler
- Tekrar eden kayıtları kaldırır
- Excel'de düzgün açılabilecek CSV dosyası oluşturur

## 🚀 Nasıl Kullanılır?

### Adım 1: Sayfa Kaynaklarını Kaydedin

1. Web sayfasında **Sağ tık → Sayfa Kaynağını Görüntüle** (veya Ctrl+U / Cmd+U)
2. Tüm içeriği kopyalayın (Ctrl+A / Cmd+A, sonra Ctrl+C / Cmd+C)
3. Bir metin editöründe yeni dosya açın
4. Yapıştırın ve kaydedin (örnek: `sayfa1.txt`, `sayfa2.html`, vb.)
5. Tüm dosyaları `kaynaklar` klasörüne koyun

### Adım 2: Script'i Çalıştırın

Terminal'de şu komutu çalıştırın:

```bash
cd /Users/hnidakd/Desktop/optik_veriler
python3 veri_duzenleyici.py
```

### Adım 3: Sonucu Açın

- `cikti_excel.csv` dosyası oluşturulacak
- Bu dosyayı **çift tıklayarak** Excel'de açın
- Tüm Türkçe karakterler düzgün görünecek!

## 📁 Klasör Yapısı

```
optik_veriler/
├── veri_duzenleyici.py       # Ana script
├── kaynaklar/                 # Sayfa kaynaklarını buraya koyun
│   ├── sayfa1.txt
│   ├── sayfa2.html
│   ├── sayfa3.txt
│   └── ...
└── cikti_excel.csv           # Oluşturulan sonuç dosyası
```

## ✨ Özellikler

- ✅ Birden fazla dosyayı aynı anda işler
- ✅ Tekrar eden kayıtları otomatik kaldırır
- ✅ Farklı karakter kodlamalarını otomatik algılar
- ✅ Excel uyumlu UTF-8 BOM formatında çıktı verir
- ✅ Verileri alfabetik sıraya göre düzenler
- ✅ Türkçe karakterler tam destek

## 🔧 Sorun Giderme

**Soru:** "kaynaklar klasörü bulunamadı" hatası alıyorum?
**Cevap:** Script ilk çalıştırmada klasörü otomatik oluşturur. Dosyalarınızı oraya koyup tekrar çalıştırın.

**Soru:** Excel'de Türkçe karakterler bozuk görünüyor?
**Cevap:** Dosyayı Excel'de şöyle açın:
1. Excel'i açın
2. Veri → Metin/CSV'den
3. Dosyayı seçin
4. "Dosya Kaynağı: 65001: Unicode (UTF-8)" seçin
5. Yükle

**Soru:** Hiç veri bulunamadı diyor?
**Cevap:** Kaynak dosyalarınızın formatını kontrol edin. CSV formatında (virgülle ayrılmış) olmalı.

## 📊 Çıktı Formatı

```csv
Şirket Adı,İsim,Telefon,Adres
ATASUN OPTİK,Mehmet Yılmaz,0242 123 45 67,"Merkez Mah. Atatürk Cad. No:1 Antalya"
BETA OPTİK,Ayşe Demir,0242 765 43 21,"Cumhuriyet Mah. İnönü Sok. 5/A Kepez, Antalya"
...
```

## 💡 İpuçları

- Sayfa kaynaklarını `.txt`, `.html`, `.csv` gibi farklı uzantılarla kaydedebilirsiniz
- Script tüm formatları okuyabilir
- Her yeni veri toplama işleminden önce `kaynaklar` klasörünü temizleyin
- Eski çıktı dosyası varsa üzerine yazılır

## 🆘 Yardım

Sorun yaşarsanız terminal çıktısını kontrol edin. Script hangi dosyaları işlediğini ve kaç kayıt eklediğini gösterir.

İyi çalışmalar! 🎉
