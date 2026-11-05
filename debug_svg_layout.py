#!/usr/bin/env python3
"""Cek banget logo SVG di file output. Cari SVG di header, lihat ukuran, kelas, dll."""
import re, sys, os

START = r"C:\Users\M ROSIFUL AQLI\medalis-live-preview"
def scan():
    for fname in sorted(os.listdir(START)):
        if not fname.endswith(".html"): 
            continue
        if fname.startswith("index"): 
            continue
        with open(os.path.join(START, fname), encoding="utf-8", errors="ignore") as fp:
            html = fp.read()
        # Cari <svg ...> di dalam header
        svg_search = re.search(r'(<svg[^>]*>.*?</svg>)', html, re.S | re.I)
        if svg_search:
            svg_block = svg_search.group(1)
            attrs = svg_search.group(1)
            # extract class dari svg tag
            m_class = re.search(r'class="([^"]*)"', attrs)
            classes = m_class.group(1) if m_class else "NO CLASS"
            # extract height, width, viewBox
            h_match = re.search(r'height="([^"]*)"', attrs)
            w_match = re.search(r'width="([^"]*)"', attrs)
            vb_match = re.search(r'viewBox="([^"]*)"', attrs)
            h = h_match.group(1) if h_match else "NO HEIGHT"
            w = w_match.group(1) if w_match else "NO WIDTH"
            vb = vb_match.group(1) if vb_match else "NO VIEWBOX"
            print(f"\n{fname}:")
            print(f"  SVG CLASS: {classes}")
            print(f"  ATTR:  height={h}, width={w}, viewBox={vb}")
            # Cari wrapper div (flex, height-full, dll)
            # Cari wrapper antara header dan svg
            wrappers = re.findall(r'<div[^>]*class="([^"]*?)"[^>]*>\s*(<svg[^>]*>)', html, re.S | re.I)
            wrapper_classes = [w[0] for w in wrappers]
            if wrapper_classes:
                print(f"  WRAPPERS SEBELUM SVG:")
                for wc in wrapper_classes[:3]:
                    print(f"    - {wc}")
            else:
                print("  TIDAK ADA WRAPPER DIV SEBELUM SVG (mungkin langsung di dalam header)")
        else:
            print(f"\n{fname}: TIDAK ADA <SVG>")

scan()
