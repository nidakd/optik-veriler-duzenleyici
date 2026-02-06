# 🔍 Optik Veriler Düzenleyici

Web sayfalarından toplanan optik firma verilerini otomatik olarak düzenleyen Python script'i.

## 📋 Özellikler

- ✅ Birden fazla HTML/metin dosyasından veri okuma
- ✅ Otomatik veri temizleme ve düzenleme
- ✅ Tekrar eden kayıtları kaldırma
- ✅ Excel uyumlu CSV çıktısı (UTF-8 BOM ile)
- ✅ Türkçe karakter desteği
- ✅ Alfabetik sıralama

## 🚀 Kurulum

### Gereksinimler

- Python 3.6 veya üzeri
- Ek kütüphane gerektirmez (standart kütüphane kullanır)

### Klasör Yapısı

```
optik_veriler/
├── veri_duzenleyici.py       # Ana script
├── kaynaklar/                 # Kaynak dosyaları buraya koyun
│   └── veri_sayfa1.txt       # Örnek kaynak dosya
├── cikti_excel.csv           # Oluşturulan çıktı (otomatik)
├── KULLANIM.md               # Detaylı kullanım kılavuzu
└── BASLANGIC.txt            # Hızlı başlangıç rehberi
```

## 💻 Kullanım

### Adım 1: Veri Toplama

1. Web sayfasında **Sağ tık → Sayfa Kaynağını Görüntüle** (veya `Cmd+U` / `Ctrl+U`)
2. Tüm içeriği kopyalayın (`Cmd+A` / `Ctrl+A`, sonra `Cmd+C` / `Ctrl+C`)
3. Metin editöründe yeni dosya açın
4. Yapıştırın ve `kaynaklar` klasörüne kaydedin (örn: `sayfa1.txt`)

### Adım 2: Script'i Çalıştırma

```bash
cd optik_veriler
python3 veri_duzenleyici.py
```

### Adım 3: Sonucu Görüntüleme

- `cikti_excel.csv` dosyası oluşturulur
- Excel'de çift tıklayarak açın
- Tüm Türkçe karakterler düzgün görünecektir

## 📊 Çıktı Formatı

CSV dosyası şu sütunları içerir:

| Şirket Adı | Şahıs Adı | Telefon | Adres |
|------------|-----------|---------|-------|
| ... | ... | ... | ... |

## 🛠️ Teknik Detaylar

- **Encoding:** UTF-8 with BOM (Excel uyumluluğu için)
- **Veri Yapısı:** Dictionary kullanarak otomatik tekrar temizleme
- **Hata Yönetimi:** Birden fazla encoding desteği
- **Sıralama:** Şirket adına göre alfabetik

## 📝 Notlar

- Script boş kayıtları otomatik atlar
- Birden fazla dosyayı aynı anda işleyebilir
- Her çalıştırmada önceki `cikti_excel.csv` dosyasının üzerine yazar

## 📄 Lisans

Bu proje kişisel kullanım için geliştirilmiştir.

## 👤 Geliştirici

Kişisel otomasyon projesi - 2026

---

**⚠️ Dikkat:** Bu araç veri toplamak için kullanılırken, telif hakları ve gizlilik politikalarına uyulması gerekmektedir.
