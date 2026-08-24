# -*- coding: utf-8 -*-
"""
NSosyal Erişilebilir Destek - Görsel Alternatif Metin (Alt-Text) PoC Demosu
Görev Sorumlusu: Zeynep Ecren (Yazılım ve Backend)
Teknoloji: Google GenAI Yeni SDK (google-genai)

Bu script, yüklenen bir görseli analiz ederek W3C ve ekran okuyucu standartlarına
uygun Türkçe alternatif metin (alt-text) üretir. 

Gerekli Kütüphaneler:
    pip install google-genai pillow

Çalıştırma Öncesi API Key Tanımlama:
    Windows CMD: set GEMINI_API_KEY="api_keyiniz"
    Windows PowerShell: $env:GEMINI_API_KEY="api_keyiniz"
    Linux/Mac/Colab: export GEMINI_API_KEY="api_keyiniz"
"""

import os
import sys
import time
from PIL import Image
from google import genai
from google.genai.errors import APIError

def setup_client():
    # API anahtarını ortam değişkenlerinden okur ve doğrular
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[HATA] GEMINI_API_KEY ortam değişkeni bulunamadı!")
        print("Lütfen terminalde API keyinizi ayarlayın.")
        print("Örnek (PowerShell): $env:GEMINI_API_KEY='AIzaSy...'")
        sys.exit(1)
        
    try:
        # Yeni Google GenAI istemcisini başlatır (otomatik olarak GEMINI_API_KEY'i kullanır)
        client = genai.Client()
        print("[BİLGİ] Yeni Google GenAI İstemcisi başarıyla başlatıldı.")
        return client
    except Exception as e:
        print(f"[HATA] İstemci başlatılırken hata oluştu: {str(e)}")
        sys.exit(1)

def generate_turkish_alt_text(client, image_path):
    # Görselin varlığını kontrol et
    if not os.path.exists(image_path):
        print(f"[HATA] Belirtilen görsel bulunamadı: {image_path}")
        return None

    print(f"[BİLGİ] Görsel yükleniyor: {image_path}")
    img = Image.open(image_path)

    # W3C Standartlarına tam uyumlu Prompt
    w3c_prompt = (
        "Bu görseli, ekran okuyucu kullanan görme engelli bir sosyal medya kullanıcısı için Türkçe olarak betimle. "
        "Betimleme kuralları:\n"
        "1. Kısa, öz ve nesnel ol (en fazla 2-3 cümle).\n"
        "2. Asla 'Resimde...', 'Bu görselde...', 'Bir fotoğraf...' gibi ifadelerle başlama (ekran okuyucular görsel olduğunu zaten belirtir).\n"
        "3. Görselin ana odağını, ortamı, varsa insanları ve gerçekleştirdikleri eylemleri betimle.\n"
        "4. Görselin içinde veya üzerinde okunabilir herhangi bir yazı, logo metni veya afiş başlığı varsa, bunları alternatif metne mutlaka dahil et (OCR yeteneği)."
    )

    print("[BİLGİ] Gemini 3.6 Flash modeli çağrılıyor...")
    start_time = time.time()
    
    try:
        # Yeni SDK model çağrısı
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=[img, w3c_prompt]
        )
        end_time = time.time()
        
        latency = end_time - start_time
        alt_text = response.text.strip()
        
        print(f"[BİLGİ] Analiz tamamlandı. Gecikme Süresi (Latency): {latency:.2f} saniye")
        return alt_text
        
    except APIError as ae:
        print(f"[HATA] Gemini API Servis Hatası (Yeni SDK): {ae.message}")
        try:
            print("\n[HATA AYIKLAMA] API anahtarınızın erişebildiği modeller listeleniyor:")
            for m in client.models.list():
                print(f" - {m.name}")
        except Exception as list_err:
            print(f"[HATA AYIKLAMA] Modeller listelenemedi: {str(list_err)}")
            print("İpucu: API anahtarınızı Google Cloud Console yerine Google AI Studio'dan (https://aistudio.google.com/) aldığınızdan ve 'Generative Language API' servisinin etkin olduğundan emin olun.")
        return None
    except Exception as e:
        print(f"[HATA] Beklenmeyen bir hata oluştu: {str(e)}")
        return None

if __name__ == "__main__":
    client = setup_client()
    
    # Test için görsel yolu (Gönderdiğiniz TEKNOFEST 2026 Şanlıurfa görselini test edelim)
    test_image = r"c:\Users\zeyne\OneDrive\Masaüstü\my-agy-projects\teknofest_test.jpg"
    
    # Alternatif metin üretimi
    alt_text_result = generate_turkish_alt_text(client, test_image)
    
    if alt_text_result:
        print("\n" + "="*50)
        print("ÜRETİLEN ERİŞİLEBİLİR TÜRKÇE ALTERNATİF METİN:")
        print("="*50)
        print(alt_text_result)
        print("="*50 + "\n")
