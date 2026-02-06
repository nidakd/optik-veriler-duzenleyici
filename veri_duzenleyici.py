#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optik Verilerini Düzenleyici Script
====================================
Birden fazla HTML/metin dosyasından optik firma verilerini okur,
temizler, tekrarları kaldırır ve Excel uyumlu CSV dosyası oluşturur.

Kullanım:
1. Tüm sayfa kaynaklarını 'kaynaklar' klasörüne koyun
2. Script'i çalıştırın: python3 veri_duzenleyici.py
3. Sonuç 'cikti_excel.csv' dosyasında olacak
"""

import os
import re
import codecs
from pathlib import Path

class VeriDuzenleyici:
    def __init__(self, kaynak_klasor='kaynaklar', cikti_dosya='cikti_excel.csv'):
        self.kaynak_klasor = kaynak_klasor
        self.cikti_dosya = cikti_dosya
        self.veriler = {}  # Tekrarları önlemek için dictionary kullanıyoruz
        
    def klasor_olustur(self):
        """Kaynak klasörü yoksa oluştur"""
        if not os.path.exists(self.kaynak_klasor):
            os.makedirs(self.kaynak_klasor)
            print(f"✓ '{self.kaynak_klasor}' klasörü oluşturuldu.")
            print(f"  Lütfen sayfa kaynaklarınızı bu klasöre koyun.\n")
            return False
        return True
    
    def dosyalari_listele(self):
        """Kaynak klasöründeki tüm dosyaları listele"""
        dosyalar = []
        for dosya in os.listdir(self.kaynak_klasor):
            dosya_yolu = os.path.join(self.kaynak_klasor, dosya)
            if os.path.isfile(dosya_yolu):
                dosyalar.append(dosya_yolu)
        return dosyalar
    
    def satir_ayikla(self, satir):
        """Bir satırdan firma bilgilerini çıkar"""
        # CSV formatındaki satırları parse et
        # Format: Şirket Adı,Şahıs Adı,Telefon,"Adres"
        
        # Boş satırları atla
        if not satir or satir.strip() == '':
            return None
        
        # Başlık satırlarını atla
        if 'Şirket Adı' in satir or 'Şahıs Adı' in satir:
            return None
            
        # Virgülle ayrılmış değerleri al (tırnak içindeki virgülleri koruyarak)
        parts = []
        current = ''
        in_quotes = False
        
        for char in satir:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                parts.append(current.strip())
                current = ''
                continue
            current += char
        
        # Son parçayı ekle
        if current:
            parts.append(current.strip())
        
        # En az 4 alan olmalı (Şirket, İsim, Telefon, Adres)
        if len(parts) < 4:
            return None
        
        sirket = parts[0].strip().strip('"')
        isim = parts[1].strip().strip('"')
        telefon = parts[2].strip().strip('"')
        adres = parts[3].strip().strip('"')
        
        # Boş kayıtları atla
        if not sirket or sirket == '-':
            return None
            
        return {
            'sirket': sirket,
            'isim': isim,
            'telefon': telefon,
            'adres': adres
        }
    
    def dosya_oku(self, dosya_yolu):
        """Dosyayı farklı encoding'lerle okumayı dene"""
        encodings = ['utf-8', 'utf-8-sig', 'latin1', 'iso-8859-9', 'windows-1254']
        
        for encoding in encodings:
            try:
                with open(dosya_yolu, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
            except Exception as e:
                print(f"  ⚠ Hata ({encoding}): {e}")
                continue
        
        print(f"  ✗ Dosya okunamadı: {dosya_yolu}")
        return None
    
    def dosyayi_isle(self, dosya_yolu):
        """Bir dosyayı işle ve verileri çıkar"""
        print(f"  → İşleniyor: {os.path.basename(dosya_yolu)}")
        
        icerik = self.dosya_oku(dosya_yolu)
        if not icerik:
            return 0
        
        satirlar = icerik.split('\n')
        eklenen = 0
        
        for satir in satirlar:
            veri = self.satir_ayikla(satir)
            if veri:
                # Anahtar olarak şirket adı + telefon kullan (tekrarları önlemek için)
                anahtar = f"{veri['sirket']}_{veri['telefon']}"
                if anahtar not in self.veriler:
                    self.veriler[anahtar] = veri
                    eklenen += 1
        
        print(f"    ✓ {eklenen} yeni kayıt eklendi")
        return eklenen
    
    def csv_yaz(self):
        """Verileri Excel uyumlu CSV formatında yaz"""
        if not self.veriler:
            print("✗ Hiç veri bulunamadı!")
            return False
        
        # Verileri şirket adına göre sırala
        sirali_veriler = sorted(self.veriler.values(), key=lambda x: x['sirket'])
        
        # UTF-8 BOM ile dosya oluştur (Excel uyumluluğu için)
        with codecs.open(self.cikti_dosya, 'w', 'utf-8-sig') as f:
            # Başlık satırı
            f.write('Şirket Adı,İsim,Telefon,Adres\n')
            
            # Veri satırları
            for veri in sirali_veriler:
                # Adres virgül içerdiği için tırnak içine al
                satir = f'{veri["sirket"]},{veri["isim"]},{veri["telefon"]},"{veri["adres"]}"\n'
                f.write(satir)
        
        print(f"\n✓ Toplam {len(sirali_veriler)} benzersiz kayıt '{self.cikti_dosya}' dosyasına yazıldı")
        print(f"  Dosyayı Excel'de çift tıklayarak açabilirsiniz.\n")
        return True
    
    def calistir(self):
        """Ana işlem"""
        print("\n" + "="*60)
        print("  OPTİK VERİLERİNİ DÜZENLEYICI")
        print("="*60 + "\n")
        
        # Klasör kontrolü
        if not self.klasor_olustur():
            return
        
        # Dosyaları listele
        dosyalar = self.dosyalari_listele()
        if not dosyalar:
            print(f"✗ '{self.kaynak_klasor}' klasöründe dosya bulunamadı!")
            print(f"  Lütfen sayfa kaynaklarınızı bu klasöre koyun.\n")
            return
        
        print(f"✓ {len(dosyalar)} dosya bulundu\n")
        
        # Her dosyayı işle
        toplam = 0
        for dosya in dosyalar:
            toplam += self.dosyayi_isle(dosya)
        
        # CSV'ye yaz
        if toplam > 0:
            self.csv_yaz()
        else:
            print("\n✗ İşlenebilir veri bulunamadı!")
            print("  Dosyaların formatını kontrol edin.\n")


if __name__ == '__main__':
    duzenleyici = VeriDuzenleyici()
    duzenleyici.calistir()
