import subprocess, sys, os, base64, json

CHROMIUM = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
OUT_PNG = r"C:\Users\M ROSIFUL AQLI\AppData\Local\hermes\images\navbar_mock.png"
NAVBAR_HTML = r"C:\Users\M ROSIFUL AQLI\AppData\Local\hermes\navbar_mock.html"
API_KEY = os.environ.get("OPENAI_API_KEY", "")

def main():
    # Re-screenshot
    if not os.path.exists(CHROMIUM):
        print("Chrome not found")
        sys.exit(1)
    
    print("Re-screenshot...")
    cmd = [CHROMIUM, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--disable-dev-shm-usage", "--window-size=1920,1080",
           "--screenshot=" + OUT_PNG, "file://" + NAVBAR_HTML]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"Error: {result.stderr[:200]}")
        sys.exit(1)
    
    if not os.path.exists(OUT_PNG):
        print("No output")
        sys.exit(1)
    
    print(f"Saved: {OUT_PNG} ({os.path.getsize(OUT_PNG)} bytes)")
    
    # Encode for API
    with open(OUT_PNG, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    
    payload = json.dumps({
        "model": "gpt-4o",
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "Analisis screenshot navbar mock ini. Apakah logo MEDALIS SVG sejajar secara horizontal dengan menu navigasi (Beranda, Modul, dll)? Atau logo melompong ke atas? Perhatikan posisi relatif logo terhadap menu dan tombol kanan. Berikan deskripsi detail tentang alignment."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}}
            ]
        }],
        "max_tokens": 600
    }).encode()
    
    if not API_KEY:
        print("OPENAI_API_KEY not set. Skipping vision analysis.")
        print("\nManual analysis:")
        print("File size:", os.path.getsize(OUT_PNG))
        print("HTML template used navbar_mock.html — check if logo alignment is correct by inspecting the HTML.")
        return
    
    print("Calling GPT-4o vision...")
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=payload,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    )
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read())
        print(data["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"API error: {e}")

if __name__ == "__main__":
    main()
