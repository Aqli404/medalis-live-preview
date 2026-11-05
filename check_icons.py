import os, re
from pathlib import Path

base = r"C:\Users\M ROSIFUL AQLI\medalis-live-preview"
count = 0
for root, _, files in os.walk(base):
    for fn in files:
        if fn.endswith(".html") and fn != "index.html":
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, base)
            with open(p, "r", encoding="utf-8") as fp:
                html = fp.read()
            if "home Beranda" in html or "menu_book Modul" in html or "fact_check Tryout" in html:
                print("TROUBLE: " + rel)
                count += 1

print(f"\nTotal: {count} files with raw icon label")
