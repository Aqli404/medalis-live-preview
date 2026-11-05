import subprocess, sys, os
from pathlib import Path

CHROMIUM = Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
OUT_PNG = Path(r"C:\Users\M ROSIFUL AQLI\AppData\Local\hermes\images\navbar_mock.png")
NAVBAR_HTML = Path(r"C:\Users\M ROSIFUL AQLI\AppData\Local\hermes\navbar_mock.html")

if not CHROMIUM.exists():
    print("Chrome not found")
    sys.exit(1)

print(f"Re-screenshotting: {NAVBAR_HTML}")
cmd = [
    str(CHROMIUM),
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--window-size=1920,1080",
    "--screenshot=" + str(OUT_PNG),
    "file://" + str(NAVBAR_HTML)
]
print(f"Command: {cmd[0]} ...")
result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
if result.returncode != 0:
    print(f"Error exit {result.returncode}: {result.stderr[:300]}")
    sys.exit(1)
if OUT_PNG.exists():
    print(f"Saved: {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
else:
    print("No output")
    sys.exit(1)
