import os
import re
from collections import defaultdict

work_dir = r"C:\Users\M ROSIFUL AQLI\medalis-live-preview"
files = [f for f in sorted(os.listdir(work_dir)) if f.endswith(".html") and f != "index.html"]

navbar_data = {}

for f in files:
    p = os.path.join(work_dir, f)
    with open(p, "r", encoding="utf-8") as fp:
        html = fp.read()
    
    header_m = re.search(r"<header[^>]*>(.*?)</header>", html, re.S)
    nav_m = re.search(r"<nav[^>]*>(.*?)</nav>", html, re.S)
    
    header_cls = ""
    header_tag = ""
    if header_m:
        h_open = re.search(r"<header[^>]*>", html)
        header_tag = h_open.group(0) if h_open else ""
        c = re.search(r'class="([^"]*)"', header_tag)
        header_cls = c.group(1) if c else ""
        
    nav_links = []
    active_nav = ""
    if nav_m:
        links = re.findall(r'<a([^>]*)>(.*?)</a>', nav_m.group(0), re.S)
        for attrs, l in links:
            t = " ".join(re.sub(r'<[^>]+>', ' ', l).split()).strip()
            nav_links.append(t)
            if 'aria-current="page"' in attrs or 'bg-' in attrs or 'font-bold' in attrs:
                active_nav = t
            
    has_switcher = bool(re.search(r"Terang.*?Gelap.*?Sistem", html))
    
    # Check right actions in header
    right_actions = []
    if header_m:
        hdr = header_m.group(0)
        if "Masuk" in hdr: right_actions.append("Masuk")
        if "Coba Gratis" in hdr: right_actions.append("Coba Gratis")
        if "person" in hdr: right_actions.append("Avatar")
        if "Selesai Ujian" in hdr: right_actions.append("Selesai Ujian")
    
    navbar_data[f] = {
        "header_cls": header_cls,
        "nav_links": nav_links,
        "active_nav": active_nav,
        "right_actions": right_actions,
        "has_switcher": has_switcher
    }

print("=== NAVBAR CATEGORIES & INCONSISTENCIES ===")
groups = defaultdict(list)
for f, d in navbar_data.items():
    links_str = " | ".join(d["nav_links"]) if d["nav_links"] else "[NO NAV LINKS]"
    groups[links_str].append((f, d["active_nav"], d["right_actions"]))

for links_str, flist in groups.items():
    print(f"\nGroup: {links_str}")
    print(f"Total screens: {len(flist)}")
    for f, act, r in flist:
        print(f"  - {f:30s} | Active: {act:15s} | Right: {r}")
