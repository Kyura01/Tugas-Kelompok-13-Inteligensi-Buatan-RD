# Tugas-Kelompok-13-Inteligensi-Buatan-RD

[cite_start]Proyek ini adalah implementasi dan perbandingan dua algoritma pencarian rute terpendek, yaitu **Uniform Cost Search (UCS)** dan **$A^{*}$ Search**, sebagai bagian dari Tugas Mata Kuliah Inteligensi Buatan (IB)[cite: 1, 16].

## Anggota Kelompok

[cite_start]Laporan ini disusun oleh Kelompok 13 [cite: 3] [cite_start]dari Program Studi Teknik Informatika, Institut Teknologi Sumatera (ITERA), tahun 2025[cite: 5, 6].

| Nama | NIM |
| :--- | :--- |
| Anisah Octa Rohila | 123140137 |
| Ahmad Ali Mukti | 123140155 |
| Jefri Wahyu Fernando Sembiring | 123140206 |

## Deskripsi Tugas

[cite_start]Tujuan dari tugas ini adalah untuk mengimplementasikan dan membandingkan efektivitas serta optimalitas algoritma UCS dan $A^{*}$ dalam menemukan rute terpendek pada graf peta jalan di Pulau Jawa[cite: 18]. [cite_start]Studi kasus yang digunakan adalah pencarian rute dari **Cilegon** ke **Banyuwangi**[cite: 40, 41, 111, 112, 187, 188, 239, 240, 244].

## Struktur Repositori

| File/Folder | Deskripsi |
| :--- | :--- |
| **`UCS.py`** | [cite_start]Implementasi algoritma Uniform Cost Search (UCS) dalam bahasa Python[cite: 152]. |
| **`A_Star.py`** | [cite_start]Implementasi algoritma $A^{*}$ Search dalam bahasa Python[cite: 191]. |
| **`csv/`** | [cite_start]Berisi file data CSV yang digunakan sebagai input graf peta jalan dan nilai heuristik[cite: 185, 233, 234, 235, 236]. |
| **`123140137_123140155_123140206_Tugas 4.pdf`** | [cite_start]File laporan lengkap tugas ini (LAPORAN IB RD METODE SEARCHING)[cite: 1]. |

## Hasil Singkat

| Algoritma | Rute yang Ditemukan | Total Jarak (km) |
| :--- | :--- | :--- |
| **UCS** | [cite_start]Cilegon $\rightarrow$ ... $\rightarrow$ Situbondo $\rightarrow$ Banyuwangi [cite: 246, 248] | [cite_start]**1153 km** [cite: 245] |
| **$A^{*}$ Search** | [cite_start]Cilegon $\rightarrow$ ... $\rightarrow$ Probolinggo $\rightarrow$ Lumajang $\rightarrow$ Jember $\rightarrow$ Banyuwangi [cite: 253] | [cite_start]**1205 km** [cite: 252] |

[cite_start]**Kesimpulan Hasil:** Dalam studi kasus ini, **UCS terbukti lebih optimal** karena berhasil menemukan jalur dengan total jarak terendah (1153 km) dibandingkan dengan $A^{*}$ Search (1205 km)[cite: 258, 259].

## Lampiran

1.  [cite_start]**Laporan Lengkap:** Laporan ini (LAPORAN IB.pdf) [cite: 1] [cite_start]menjelaskan detail pseudocode [cite: 19, 78][cite_start], implementasi, dan analisis hasil perbandingan[cite: 243].
2.  [cite_start]**Video Penjelasan:** Demonstrasi program dan penjelasan alur implementasi serta analisis hasil telah diunggah melalui video YouTube[cite: 268].
