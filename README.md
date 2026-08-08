# MathVerse

Aplikasi Matematik interaktif untuk **KSSR Semakan Tahun 1–6**, dalam Bahasa Melayu.
Berpandukan Buku Teks dan DSKP KPM/DBP.

**Cuba di sini: https://semanjohn.github.io/mathverse/**

Buka pautan itu di Safari iPhone/iPad → Kongsi → **Tambah ke Skrin Utama**,
dan ia berjalan skrin penuh seperti aplikasi biasa.

---

## Fail dalam repositori ini

| Fail | Guna untuk |
|---|---|
| `index.html` | Versi utama. Inilah yang disiarkan oleh GitHub Pages, dan yang patut disunting. |
| `mathverse-luar-talian.html` | Satu fail tunggal dengan semua gambar dibenamkan. Untuk dihantar melalui WhatsApp/Telegram atau digunakan tanpa internet. |
| `assets/wang-malaysia/` | Foto duit syiling dan wang kertas Malaysia (WebP). |
| `bina-luar-talian.py` | Menjana semula `mathverse-luar-talian.html` selepas `index.html` disunting. |

---

## Struktur kod (untuk ChatGPT / Claude)

Semuanya dalam satu fail HTML: tiada `npm`, tiada langkah bina, tiada kebergantungan luar.
Buka terus dalam pelayar untuk menguji.

### Dua struktur utama

**1. `CURR` — data kurikulum**

```js
const CURR = {
  1: { nama:"Tahun 1", hadNombor:100, unit:[
    { id:"T1_U1", n:"Nombor Hingga 100", s:[
      { id:"S1", n:"Banyak dan Sedikit", p:2, a:"banding", c:{max:12} }
    ]}
  ]}
};
```

| Medan | Maksud |
|---|---|
| `n` | Nama subtopik yang dipaparkan |
| `p` | Muka surat Buku Teks (rujukan cikgu) |
| `a` | Nama enjin dalam `ENJIN` yang menjana soalan |
| `c` | Tetapan yang dihantar kepada enjin itu |

**2. `ENJIN` — penjana soalan**

Setiap enjin menerima tetapan dan memulangkan fungsi penjana:

```js
ENJIN.namaEnjin = c => () => ({
  q:      "Ayat soalan (HTML dibenarkan)",
  vis:    "HTML gambar/rajah",
  opts:   ["A","B","C","D"],   // aneka pilihan
  ans:    -1,                  // -1 = padan ikut ansVal
  ansVal: "B",                 // jawapan betul
  hint:   "Penerangan selepas menjawab",
  mod:    "interaktif",        // jika guna mekanik sendiri
  cek:    () => true           // penyemak sendiri bagi mod interaktif
});
```

### Mekanik interaktif sedia ada

| Mekanik | Kegunaan |
|---|---|
| `LZM` | Bentuk lazim tambah/tolak, termasuk kumpul semula langkah demi langkah |
| `JKR` | Jalan kerja berlangkah dengan gelembung panduan |
| `PINP` | Kotak pengangka/penyebut untuk pecahan |
| `MANGKUK` / `MANGKUKC` | Teknik mangkuk (bahagi panjang) |
| `SLOT` | Ruang perkataan dengan papan kekunci QWERTY |
| `ISI` | Lengkapkan susunan/pola daripada bank nombor |
| `SUAI` | Suaikan / padankan |
| `WLT` | Dompet duit syiling |
| `B2L` / `GARIS2` | Lukis bentuk 2D dan garis lurus |

### Fungsi penting

- `bersih(it)` — membersihkan pilihan jawapan: buang pendua, hormati had nombor tahun,
  hadkan kepada 4 pilihan. **Semua soalan aneka pilihan mesti melaluinya.**
- `seragamkanKotak()` — menyamakan lebar semua kotak dalam satu baris.
- `muatSatuMuka()` — mengecilkan kandungan jika melebihi satu skrin.

---

## Peraturan reka bentuk (jangan dilanggar)

1. **Satu skrin, tiada tatal.** `#app` ialah `100dvh`; papan kekunci dipaku ke bawah
   dengan `margin-top:auto`.
2. **Kelas `isi` hanya untuk bekas kandungan.** Untuk kotak yang sudah diisi, guna `terisi`.
   (Pernah menyebabkan kotak jawapan mengembang besar.)
3. **Tiada soalan berulang dalam satu set 6** — dikawal oleh tandatangan soalan dalam `vMain()`.
4. **Had nombor mengikut tahun** — T1 ≤ 100, T2 ≤ 1 000, dan seterusnya.
   `bersih()` yang menguatkuasakannya.
5. **Sistem 24 jam ditulis empat digit tanpa titik bertindih:** `Jam 1805`.
   Sistem 12 jam guna titik bertindih dan mesti nyatakan a.m./p.m.: `6:05 p.m.`
   (Buku Teks Tahun 4, m/s 139–142.)
6. **Pengecoh mesti munasabah** — jangan jana waktu yang tidak wujud seperti `30:02`,
   dan jangan ulang nilai yang sudah ada dalam senarai pilihan.

---

## Menjana semula versi luar talian

Selepas menyunting `index.html`:

```bash
python3 bina-luar-talian.py
```

---

## Lesen

Untuk kegunaan pendidikan.
Foto wang Malaysia adalah hak milik Bank Negara Malaysia.
