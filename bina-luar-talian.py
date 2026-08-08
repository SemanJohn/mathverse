#!/usr/bin/env python3
"""Selepas menyunting index.html, jalankan skrip ini.

Ia melakukan DUA perkara:
  1. Membenamkan foto wang ke dalam HTML -> mathverse-luar-talian.html
     (satu fail yang boleh dihantar melalui WhatsApp dan digunakan tanpa internet)
  2. Menyalin nombor VERSI dari index.html ke versi.json
     supaya aplikasi di Skrin Utama tahu ada kemas kini dan memuat semula sendiri.

PENTING: naikkan `const VERSI="x.y"` dalam index.html setiap kali anda
membuat perubahan. Jika tidak, telefon akan terus memakai salinan lama.

Guna:  python3 bina-luar-talian.py
"""
import base64, io, json, os, re

ASAS   = os.path.dirname(os.path.abspath(__file__))
SUMBER = os.path.join(ASAS, "index.html")
HASIL  = os.path.join(ASAS, "mathverse-luar-talian.html")
VERSI  = os.path.join(ASAS, "versi.json")
GAMBAR = os.path.join(ASAS, "assets", "wang-malaysia")


def main():
    html = io.open(SUMBER, encoding="utf-8").read()

    # ---- 1. versi.json ----
    padan = re.search(r'const VERSI="([^"]+)"', html)
    if not padan:
        raise SystemExit('Ralat: const VERSI="..." tidak dijumpai dalam index.html')
    versi = padan.group(1)
    io.open(VERSI, "w", encoding="utf-8").write(json.dumps({"versi": versi}))
    print("versi.json -> %s" % versi)

    # ---- 2. benamkan gambar ----
    peta = {}
    for nama in sorted(os.listdir(GAMBAR)):
        if not nama.lower().endswith(".webp"):
            continue
        with open(os.path.join(GAMBAR, nama), "rb") as f:
            peta[nama[:-5]] = "data:image/webp;base64," + base64.b64encode(f.read()).decode()

    mula  = html.index("const WANG_FOTO=")
    tamat = html.index("});", mula) + 3      # blok Proxy berakhir dengan "});"
    html  = html[:mula] + "const WANG_FOTO=" + json.dumps(peta, separators=(",", ":")) + ";" + html[tamat:]

    io.open(HASIL, "w", encoding="utf-8").write(html)
    print("%d gambar dibenamkan -> %s (%d KB)"
          % (len(peta), os.path.basename(HASIL), len(html) // 1024))


if __name__ == "__main__":
    main()
