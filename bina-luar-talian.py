#!/usr/bin/env python3
"""Benamkan foto wang ke dalam HTML supaya jadi SATU fail yang boleh
dihantar melalui WhatsApp/Telegram dan digunakan tanpa internet.

Guna:  python3 bina-luar-talian.py
Hasil: mathverse-luar-talian.html
"""
import base64, io, os, re, json

ASAS = os.path.dirname(os.path.abspath(__file__))
SUMBER = os.path.join(ASAS, "index.html")
HASIL = os.path.join(ASAS, "mathverse-luar-talian.html")
GAMBAR = os.path.join(ASAS, "assets", "wang-malaysia")

def main():
    html = io.open(SUMBER, encoding="utf-8").read()

    peta = {}
    for nama in sorted(os.listdir(GAMBAR)):
        if not nama.lower().endswith(".webp"):
            continue
        with open(os.path.join(GAMBAR, nama), "rb") as f:
            data = base64.b64encode(f.read()).decode()
        peta[nama[:-5]] = "data:image/webp;base64," + data

    mula = html.index("const WANG_FOTO=")
    # blok Proxy berakhir dengan "});"
    tamat = html.index("});", mula) + 3
    baharu = "const WANG_FOTO=" + json.dumps(peta, separators=(",", ":")) + ";"
    html = html[:mula] + baharu + html[tamat:]

    io.open(HASIL, "w", encoding="utf-8").write(html)
    print("%d gambar dibenamkan -> %s (%d KB)"
          % (len(peta), os.path.basename(HASIL), len(html) // 1024))

if __name__ == "__main__":
    main()
