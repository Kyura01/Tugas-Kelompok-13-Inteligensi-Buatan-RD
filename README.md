# Tugas-Kelompok-13-Inteligensi-Buatan-RD

Proyek ini adalah implementasi dan perbandingan dua algoritma pencarian rute terpendek, yaitu **Uniform Cost Search (UCS)** dan **$A^{*}$ Search**, sebagai bagian dari Tugas Mata Kuliah Inteligensi Buatan (IB).

## Anggota Kelompok

Laporan ini disusun oleh Kelompok 13 dari Program Studi Teknik Informatika, Institut Teknologi Sumatera (ITERA), tahun 2025.

| Nama | NIM |
| :--- | :--- |
| Anisah Octa Rohila | 123140137 |
| Ahmad Ali Mukti | 123140155 |
| Jefri Wahyu Fernando Sembiring | 123140206 |

## Deskripsi Tugas

Tujuan dari tugas ini adalah untuk mengimplementasikan dan membandingkan efektivitas serta optimalitas algoritma UCS dan $A^{*}$ dalam menemukan rute terpendek pada graf peta jalan di Pulau Jawa.Studi kasus yang digunakan adalah pencarian rute dari **Cilegon** ke **Banyuwangi**.

## Struktur Repositori

| File/Folder | Deskripsi |
| :--- | :--- |
| **`UCS.py`** |Implementasi algoritma Uniform Cost Search (UCS) dalam bahasa Python. |
| **`A_Star.py`** |Implementasi algoritma $A^{*}$ Search dalam bahasa Python. |
| **`csv/`** |Berisi file data CSV yang digunakan sebagai input graf peta jalan dan nilai heuristik. |
| **`123140137_123140155_123140206_Tugas 4.pdf`** |File laporan lengkap tugas ini (LAPORAN IB RD METODE SEARCHING). |

## Hasil Singkat

| Algoritma | Rute yang Ditemukan | Total Jarak (km) |
| :--- | :--- | :--- |
| **UCS** |Cilegon $\rightarrow$ ... $\rightarrow$ Situbondo $\rightarrow$ Banyuwangi  |**1153 km**|
| **$A^{*}$ Search** |Cilegon $\rightarrow$ ... $\rightarrow$ Probolinggo $\rightarrow$ Lumajang $\rightarrow$ Jember $\rightarrow$ Banyuwangi |**1205 km**  |

**Kesimpulan Hasil:** Dalam studi kasus ini, **UCS terbukti lebih optimal** karena berhasil menemukan jalur dengan total jarak terendah (1153 km) dibandingkan dengan $A^{*}$ Search (1205 km).

## Lampiran

1. **Laporan Lengkap:** Laporan ini 123140137_123140155_123140206_Tugas 4.pdf menjelaskan detail pseudocode, implementasi, dan analisis hasil perbandingan.
2. **Video Penjelasan:** Demonstrasi program dan penjelasan alur implementasi serta analisis hasil telah diunggah melalui video YouTube.
