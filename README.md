# Kalkulator Permutasi dan Kombinasi

Program Python untuk menghitung nilai matematika dari **Permutasi** dan **Kombinasi**, sekaligus menampilkan seluruh kemungkinan susunan / pasangan secara lengkap dalam tampilan terminal interaktif dan visual yang menarik menggunakan library `rich`.

## Fitur Utama

1. **Perhitungan Matematis Akurat**:
   - **Permutasi**: $P(n, r) = \frac{n!}{(n-r)!}$ (Urutan diperhatikan, contoh: $AB \neq BA$)
   - **Kombinasi**: $C(n, r) = \frac{n!}{r!(n-r)!}$ (Urutan tidak diperhatikan, contoh: $AB = BA$)
2. **Penampil Seluruh Kemungkinan**:
   - Menggunakan modul standar `itertools` (`permutations` & `combinations`).
   - Menyajikan setiap kemungkinan susunan lengkap dengan nomor urut.
3. **Antarmuka Terminal Modern & Estetis**:
   - Dibuat dengan library **`rich`** (tabel responsif, panel berwarna, border membulat).
   - Penataan grid/kolom otomatis menyesuaikan lebar layar dan panjang elemen agar rapi.
   - Dilengkapi proteksi kinerja jika kemungkinan mencapai ribuan kombinasi.
4. **Input yang Fleksibel**:
   - Bisa memasukkan nama elemen khusus (misal: `Merah, Kuning, Hijau` atau `A, B, C, D`).
   - Atau cukup memasukkan nilai angka $n$ (otomatis digenerate A, B, C... atau angka 1, 2, 3...).
5. **Mode Komparasi**:
   - Memungkinkan perbandingan langsung hasil Permutasi vs Kombinasi untuk elemen yang sama.

---

## Persyaratan & Instalasi

Program ini menggunakan Python 3.8+ dan library `rich`.

Pasang library yang dibutuhkan:
```bash
pip install rich
```

---

## Cara Menjalankan Program

Buka terminal di folder ini, lalu jalankan:
```bash
python main.py
```

---

## Contoh Tampilan Output

```text
┌──────────────────────── Ringkasan Permutasi P(n, r) ────────────────────────┐
│ Definisi: Urutan diperhatikan (AB != BA)                                    │
│ Himpunan Elemen (n=3): {Merah, Kuning, Hijau}                               │
│ Ukuran Susunan (r): 2                                                       │
│ Rumus: P(n, r) = n! / (n - r)!                                              │
│ Perhitungan: P(3, 2) = 3! / (3 - 2)! = 6 cara                               │
└─────────────────────────────────────────────────────────────────────────────┘
        Daftar Seluruh Kemungkinan Permutasi P(3, 2) (Total: 6)         
┌─────┬─────────────────┬─────┬────────────────┬─────┬─────────────────┐
│ No. │     Susunan     │ No. │    Susunan     │ No. │     Susunan     │
├─────┼─────────────────┼─────┼────────────────┼─────┼─────────────────┤
│  1. │ (Merah, Kuning) │  2. │ (Merah, Hijau) │  3. │ (Kuning, Merah) │
│  4. │ (Kuning, Hijau) │  5. │ (Hijau, Merah) │  6. │ (Hijau, Kuning) │
└─────┴─────────────────┴─────┴────────────────┴─────┴─────────────────┘
```

