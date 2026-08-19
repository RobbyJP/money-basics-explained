"""
Complete script to populate all 18 new pillar articles (10 Indonesian + 8 English).
"""
from pathlib import Path

ARTICLES = Path("articles")
ARTICLES.mkdir(parents=True, exist_ok=True)

# 10 Indonesian Articles
(ARTICLES / "id-bpjs-ketenagakerjaan-jht-jp-dijelaskan.md").write_text("""---
title: "BPJS Ketenagakerjaan: Panduan Lengkap JHT vs Jaminan Pensiun (JP) dan Cara Klaimnya"
description: "Pahami perbedaan Jaminan Hari Tua (JHT) dan Jaminan Pensiun (JP) BPJS Ketenagakerjaan: persentase iuran, simulasi saldo, dan syarat klaim pencairan 100%."
slug: "id-bpjs-ketenagakerjaan-jht-jp-dijelaskan"
keyword: "bpjs ketenagakerjaan jht vs jp cara klaim jmo"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# BPJS Ketenagakerjaan: Panduan Lengkap JHT vs. Jaminan Pensiun (JP) dan Skema Iurannya

Bagi setiap pekerja formal dan penerima upah di Indonesia, potongan **BPJS Ketenagakerjaan** pada slip gaji bulanan sering kali menimbulkan pertanyaan: ke mana perginya uang tersebut, apa perbedaan antara **JHT (Jaminan Hari Tua)** dan **JP (Jaminan Pensiun)**, serta bagaimana cara mencairkannya secara legal?

Memahami hak-hak jaminan sosial ketenagakerjaan ini sangat penting agar Anda dapat merencanakan masa pensiun dengan matang dan mengklaim hak finansial Anda saat terjadi pemutusan hubungan kerja (PHK) atau saat berpindah jalur karir.

---

## Perbedaan Pokok: JHT vs. Jaminan Pensiun (JP)

| Aspek | Jaminan Hari Tua (JHT) | Jaminan Pensiun (JP) |
| :--- | :--- | :--- |
| **Sifat Program** | **Tabungan Hari Tua (Investasi Akumulatif)** | **Asuransi Pendapatan Hari Tua (Anuitas)** |
| **Bentuk Manfaat** | **Lump-Sum (Uang Tunai Sekaligus)** + Hasil Pengembangan | **Uang Pensiun Bulanan Berkala** Seumur Hidup |
| **Iuran Karyawan** | **2,0%** dari Upah Bulanan | **1,0%** dari Upah Bulanan (Maks. batas plafon) |
| **Iuran Perusahaan** | **3,7%** dari Upah Bulanan | **2,0%** dari Upah Bulanan |
| **Total Iuran** | **5,7% per bulan** | **3,0% per bulan** |
| **Syarat Pencairan** | PHK / Resign (langsung bisa cair via aplikasi JMO) | Mencapai usia pensiun (59 tahun) & min. 15 tahun iuran |

---

## Skema Persentase Iuran BPJS Ketenagakerjaan Lengkap

Untuk pekerja penerima upah (PU), berikut rincian 5 program perlindungan BPJS Ketenagakerjaan:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RINCIAN IURAN BPJS KETENAGAKERJAAN                       │
├──────────────────────────┬──────────────────┬────────────────┬──────────────┤
│         PROGRAM          │ DIBAYAR KARYAWAN │ DIBAYAR KANTOR │ TOTAL IURAN  │
├──────────────────────────┼──────────────────┼────────────────┼──────────────┤
│ 1. Jaminan Hari Tua (JHT)│ **2,0%**         │ **3,7%**       │ **5,7%**     │
│ 2. Jaminan Pensiun (JP)  │ **1,0%**         │ **2,0%**       │ **3,0%**     │
│ 3. JKK (Kecelakaan Kerja)│ 0,0%             │ 0,24% - 1,74%  │ 0,24% - 1,74%│
│ 4. JKM (Kematian)        │ 0,0%             │ **0,30%**      │ **0,30%**    │
│ 5. JKP (Kehilangan Kerja)│ 0,0%             │ Rekomposisi APBN│ 0,46%        │
└──────────────────────────┴──────────────────┴────────────────┴──────────────┘
```

---

## Simulasi Saldo JHT Selama 10 Tahun Bekerja

Iuran JHT diinvestasikan oleh BPJS Ketenagakerjaan ke instrumen pasar modal yang aman (Surat Berharga Negara, Deposito Bank BUMN, dan Obligasi Korporasi) dengan imbal hasil rata-rata **5% hingga 6% per tahun**:

* **Gaji Pokok Konstan:** Rp10.000.000 / bulan.
* **Total Iuran JHT Bulanan (5,7%):** Rp570.000 / bulan (Rp200.000 dari karyawan + Rp370.000 dari kantor).
* **Total Iuran Bersih 10 Tahun (120 bulan):** Rp68.400.000.
* **Hasil Pengembangan Investasi (Compounding 5,5%/thn):** ~Rp25.600.000.
* **Estimasi Total Saldo JHT yang Bisa Dicairkan:** **~Rp94.000.000!**

---

## Cara Mencairkan Saldo JHT Secara Online (Aplikasi JMO & Lapak Asik)

1. **Saldo di Bawah Rp10 Juta (Aplikasi JMO):**
   * Download aplikasi **JMO (Jamsostek Mobile)** di Google Play Store atau App Store.
   * Pilih menu **Jaminan Hari Tua** &rarr; **Klaim JHT**.
   * Lakukan verifikasi biometrik wajah (face recognition).
   * Masukkan nomor rekening bank atas nama sendiri. Uang langsung cair dalam hitungan jam/maksimal 1 hari kerja.
2. **Saldo di Atas Rp10 Juta (Portal Lapak Asik):**
   * Buka portal resmi `lapakasik.bpjsketenagakerjaan.go.id`.
   * Unggah dokumen: KTP, Kartu Peserta BPJSTK, Surat Pengalaman Kerja / Paklaring (atau Surat PHK), dan Buku Tabungan.
   * Ikuti sesi verifikasi video call dengan petugas BPJS sesuai jadwal. Dana akan ditransfer dalam 3–5 hari kerja.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Apakah JHT bisa dicairkan saat masih aktif bekerja di perusahaan?
Sebagian bisa. Berdasarkan PP 60/2015, peserta dengan masa kepesertaan minimal 10 tahun dapat mencairkan sebagian saldo JHT: sebesar **10% untuk persiapan hari tua** atau **30% untuk pembiayaan kepemilikan uang muka perumahan (KPR)**. Namun, pencairan sebagian ini akan dikenakan pajak progresif lebih tinggi pada saat pencairan akhir.

### Bagaimana jika iuran JP belum mencapai 15 tahun saat usia pensiun tiba?
Jika masa iuran JP kurang dari 15 tahun (180 bulan) saat peserta mencapai batas usia pensiun, peserta tidak mendapatkan uang pensiun bulanan, melainkan seluruh akumulasi iuran JP beserta hasil pengembangannya akan dikembalikan secara **lump-sum (sekaligus)**.

---

*Panduan ini disusun berdasarkan regulasi UU No. 24 Tahun 2011 tentang BPJS dan PP No. 46 Tahun 2015 beserta perubahannya. Untuk pengecekan saldo real-time, gunakan aplikasi resmi JMO.*
""", encoding="utf-8")

(ARTICLES / "id-investasi-sbn-ori-sukuk-ritel.md").write_text("""---
title: "Investasi SBN Ritel: Panduan Lengkap ORI, Sukuk Ritel (SR), SBR, dan ST untuk Pemula"
description: "Pelajari cara kerja Surat Berharga Negara (SBN) Ritel di Indonesia. Bandingkan kupon fixed rate vs floating with floor, pajak obligasi 10%, dan keamanan 100% dari APBN."
slug: "id-investasi-sbn-ori-sukuk-ritel"
keyword: "investasi sbn ritel ori sukuk ritel sbr st kupon"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# Investasi SBN Ritel: Panduan Lengkap ORI, SR, SBR, dan Sukuk Tabungan untuk Investor Pemula

Bagi masyarakat Indonesia yang mencari instrumen investasi dengan **keamanan tertinggi, risiko gagal bayar 0%, dan imbal hasil di atas bunga deposito bank**, **Surat Berharga Negara (SBN) Ritel** adalah instrumen obligasi negara yang paling ideal.

Diterbitkan langsung oleh Kementerian Keuangan Republik Indonesia, dana investasi dari SBN Ritel digunakan untuk membiayai Anggaran Pendapatan dan Belanja Negara (APBN), termasuk pembangunan infrastruktur nasional, fasilitas kesehatan, dan pendidikan.

---

## 4 Jenis SBN Ritel yang Diterbitkan Pemerintah

Kementerian Keuangan menerbitkan 4 instrumen SBN Ritel sepanjang tahun kalender:

| Instrumen | Prinsip Pengelolaan | Jenis Kupon (Bunga) | Pasar Sekunder (Bisa Dijual Sebelum Jatuh Tempo?) |
| :--- | :--- | :--- | :--- |
| **ORI (Obligasi Negara Ritel)** | Konvensional | **Fixed Rate (Pasti/Tetap)** | **Bisa (Tradable)** di Pasar Sekunder |
| **SR (Sukuk Ritel)** | **Syariah (Akad Ijarah)** | **Fixed Rate (Pasti/Tetap)** | **Bisa (Tradable)** di Pasar Sekunder |
| **SBR (Savings Bond Ritel)** | Konvensional | **Floating with Floor** | Tidak (Non-Tradable), ada fasilitas *Early Redemption* |
| **ST (Sukuk Tabungan)** | **Syariah (Akad Wakalah)** | **Floating with Floor** | Tidak (Non-Tradable), ada fasilitas *Early Redemption* |

---

## Keuntungan Utama Investasi SBN Ritel

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       3 KEUNGGULAN UTAMA SBN RITEL                          │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│    1. JAMINAN APBN 100%  │ 2. PAJAK LEBIH RENDAH    │  3. PASSIVE INCOME    │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ Pokok dan kupon dijamin  │ Pajak kupon obligasi     │ Kupon ditransfer rutin│
│ 100% oleh Undang-Undang  │ hanya **10%**, jauh      │ setiap bulan tanggal  │
│ (UU No. 24/2002 & 19/2008│ lebih hemat dibanding    │ 10 atau 15 langsung ke│
│ tanpa batas nominal maks.│ pajak deposito (20%).    │ rekening bank Anda.   │
└──────────────────────────┴──────────────────────────┴───────────────────────┘
```

---

## Kupon Fixed Rate vs. Floating with Floor

1. **Fixed Rate (Kupon Tetap - ORI & SR):** Persentase kupon tidak akan berubah sejak awal penerbitan hingga jatuh tempo, tidak peduli suku bunga Bank Indonesia (BI Rate) naik atau turun. Sangat cocok dibeli saat suku bunga acuan berada di puncak.
2. **Floating with Floor (Kupon Mengambang dengan Batas Bawah - SBR & ST):** Kupon akan naik jika BI Rate dinaikkan, namun **tidak akan pernah turun di bawah batas minimal (floor)** yang ditetapkan saat penerbitan jika BI Rate diturunkan. Ini memberikan perlindungan terbaik terhadap inflasi.

---

## Simulasi Penghasilan Bulanan Pasif dari SBN Ritel

Misalkan Anda menginvestasikan **Rp100.000.000** pada ORI dengan kupon fixed rate **6,40% per tahun**:

* **Kupon Bruto per Tahun:** Rp100.000.000 $\times$ 6,40% = **Rp6.400.000 / tahun**.
* **Kupon Bruto per Bulan:** $\frac{\text{Rp6.400.000}}{12} = \mathbf{\text{Rp533.333 / bulan}}$.
* **Potongan Pajak Obligasi PPh Final (10%):** Rp53.333 / bulan.
* **Kupon Bersih yang Masuk ke Rekening Setiap Bulan:** **Rp480.000 / bulan (Rp5.760.000 / tahun bersih)**.

---

## Cara Membeli SBN Ritel Secara Online (e-SBN)

1. **Pilih Mitra Distribusi Resmi (Midis):** Buka rekening di bank umum (BCA, Mandiri, BRI, BNI), sekuritas, atau platform fintech terdaftar (Bibit, Bareksa, Stockbit).
2. **Registrasi Single Investor Identification (SID):** Daftarkan e-KTP Anda untuk mendapatkan nomor SID dan rekening dana nasabah (RDN).
3. **Pemesanan Saat Masa Penawaran:** Masukkan nominal pemesanan (mulai Rp1.000.000 hingga Rp5.000.000.000).
4. **Bayar Kode Billing:** Selesaikan pembayaran melalui transfer ATM, Mobile Banking, atau internet banking sebelum batas waktu berakhir.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Berapa modal minimum untuk membeli SBN Ritel?
Pemesanan SBN Ritel sangat terjangkau, mulai dari **Rp1.000.000** dan kelipatannya, dengan batas pemesanan maksimum Rp5.000.000.000 hingga Rp10.000.000.000 tergantung seri tenor yang dipilih (2 tahun atau 4 tahun).

### Apa itu fasilitas Early Redemption pada SBR dan ST?
Fasilitas pelunasan sebelum jatuh tempo yang disediakan pemerintah setelah investasi berjalan 1 tahun. Investor dapat mencairkan hingga maksimal **50% dari total nilai pokok investasinya tanpa dikenakan denda atau penalti**.

---

*Panduan ini disusun berdasarkan Peraturan Menteri Keuangan Republik Indonesia terkait Pengelolaan Surat Berharga Negara Ritel.*
""", encoding="utf-8")

(ARTICLES / "id-kpr-syariah-vs-konvensional.md").write_text("""---
title: "KPR Syariah vs KPR Konvensional: Perbandingan Akad, Skema Angsuran, dan Biaya"
description: "Pahami perbedaan KPR Syariah (Akad Murabahah, Musyarakah Mutanaqisah/MMQ) dan KPR Konvensional (Bunga Fixed & Floating). Simulasi cicilan dan analisis biaya."
slug: "id-kpr-syariah-vs-konvensional"
keyword: "kpr syariah vs konvensional murabahah mmq bunga floating"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# KPR Syariah vs. KPR Konvensional: Perbandingan Akad, Skema Angsuran, dan Transparansi Biaya

Membeli rumah hunian melalui fasilitas Kredit Pemilikan Rumah (KPR) adalah salah satu keputusan finansial terbesar dalam kehidupan keluarga di Indonesia.

Saat mengajukan pembiayaan perumahan ke perbankan, masyarakat dihadapkan pada dua pilihan utama: **KPR Konvensional** dan **KPR Syariah**.

Keduanya memiliki perbedaan mendasar bukan hanya dari segi landasan hukum dan fatwa keagamaan, melainkan juga dari **mekanisme perhitungan cicilan bulanan, risiko fluktuasi suku bunga (floating rate), dan aturan denda keterlambatan**.

---

## Perbandingan Langsung: KPR Konvensional vs. KPR Syariah

| Fitur / Aspek | KPR Konvensional | KPR Syariah (Murabahah / MMQ) |
| :--- | :--- | :--- |
| **Landasan Akad** | Perjanjian Pinjam-Meminjam Uang dengan Bunga | Jual-Beli Margin (Murabahah) atau Sewa Bagi-Hasil (MMQ) |
| **Skema Bunga / Margin**| **Fixed di awal (1-3 thn), lalu Floating mengikuti pasar** | **Margin Pasti/Plafon Tetap** atau Floating Berbatas (MMQ) |
| **Risiko Angsuran Naik**| **Tinggi saat suku bunga BI naik** pasca masa promo fixed | **Pasti & Tidak Berubah** (pada Akad Murabahah) |
| **Denda Keterlambatan** | Bunga denda finansial bertingkat (menjadi laba bank) | Dana kebajikan/Ta'zir (disalurkan ke dana sosial/infaq) |
| **Biaya Pelunasan Awal** | Dikenakan penalti (biasanya 1% - 3% dari sisa pokok) | Tanpa penalti riba (namun diskon margin tergantung bank) |

---

## 2 Akad Utama dalam KPR Syariah di Indonesia

1. **Akad Murabahah (Jual-Beli dengan Margin Keuntungan):**
   * Bank syariah membeli rumah dari pengembang/penjual, lalu menjualnya kembali kepada nasabah dengan tambahan margin keuntungan yang telah disepakati di awal.
   * **Besaran cicilan bulanan 100% tetap dan tidak akan pernah berubah** dari bulan pertama hingga bulan ke-240 (20 tahun), memberikan kepastian anggaran keluarga.
2. **Akad Musyarakah Mutanaqisah (MMQ - Kepemilikan Bertahap):**
   * Nasabah dan bank syariah berkongsi modal untuk membeli rumah bersama (misal nasabah 20% melalui DP, bank 80%).
   * Nasabah kemudian menyewa porsi kepemilikan bank secara bertahap setiap bulan hingga seluruh kepemilikan rumah 100% beralih ke tangan nasabah. Nilai sewa dapat dievaluasi secara berkala sesuai indeks pasar acuan.

---

## Jebakan "Floating Rate Shock" pada KPR Konvensional

Banyak debitur KPR Konvensional terjebak saat masa promosi suku bunga murah berakhir:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     ANATOMI JEBAKAN BUNGA KPR FLOATING                      │
├────────────────────────────────────────┬────────────────────────────────────┤
│       TAHUN 1 - 3 (MASA PROMO FIXED)   │       TAHUN 4 - 20 (MASA FLOATING) │
├────────────────────────────────────────┼────────────────────────────────────┤
│ • Suku Bunga: **4,50% Fixed**          │ • Suku Bunga: **11,50% - 13,50%**  │
│ • Cicilan Pokok + Bunga:               │ • Cicilan Pokok + Bunga:           │
│   **Rp4.800.000 / bulan**              │   **Rp7.900.000 / bulan! (+64%)**  │
└────────────────────────────────────────┴────────────────────────────────────┘
```

Kenaikan angsuran drastis pasca masa fixed dapat mengacaukan arus kas keluarga apabila kenaikan gaji tidak mampu mengimbangi lonjakan cicilan tersebut.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Mengapa cicilan KPR Syariah terlihat lebih tinggi di tahun-tahun awal dibanding promo KPR Konvensional?
Karena margin KPR Syariah (khususnya Murabahah) dihitung rata secara keseluruhan jangka waktu tanpa skema "bunga diskon buatan" di awal. Sebagai imbalannya, KPR Syariah menjamin cicilan Anda tidak akan pernah melonjak di masa depan saat kondisi ekonomi makro bergejolak.

### Apakah KPR Syariah bebas dari biaya notaris dan asuransi?
Tidak. Nasabah KPR Syariah tetap membayar biaya notaris, pembuatan Akta Jual Beli (AJB), Bea Perolehan Hak atas Tanah dan Bangunan (BPHTB), serta premi Asuransi Jiwa Syariah dan Asuransi Kebakaran.

---

*Panduan ini disusun berdasarkan Fatwa Dewan Syariah Nasional Majelis Ulama Indonesia (DSN-MUI) dan regulasi Otoritas Jasa Keuangan (OJK).*
""", encoding="utf-8")

(ARTICLES / "id-pajak-umkm-pph-final-setengah-persen.md").write_text("""---
title: "Pajak UMKM 0,5% (PP 55/2022): Aturan Bebas Pajak Omzet 500 Juta, Syarat, dan Cara Bayar"
description: "Panduan lengkap PPh Final UMKM 0,5% sesuai UU HPP & PP 55 Tahun 2022. Cara menghitung batas omzet tidak kena pajak Rp500 juta, jangka waktu tarif, dan kode billing DJP."
slug: "id-pajak-umkm-pph-final-setengah-persen"
keyword: "pajak umkm pph final setengah persen pp 55 2022 omzet 500 juta"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# Pajak UMKM PPh Final 0,5%: Aturan Bebas Pajak Omzet Rp500 Juta dan Cara Perhitungannya

Pemerintah Republik Indonesia melalui **Undang-Undang Harmonisasi Peraturan Perpajakan (UU HPP)** dan **Peraturan Pemerintah No. 55 Tahun 2022** memberikan insentif perpajakan yang sangat besar bagi para pelaku Usaha Mikro, Kecil, dan Menengah (UMKM).

Skema **PPh Final UMKM 0,5%** dirancang agar pemilik usaha dagang, toko kelontong, kuliner, online shop, dan jasa dapat memenuhi kewajiban perpajakan secara sederhana tanpa perlu menyusun pembukuan neraca laba-rugi yang rumit.

Selain itu, bagi Wajib Pajak Orang Pribadi, pemerintah memberikan fasilitas **Bebas Pajak atas peredaran bruto (omzet) hingga Rp500.000.000 per tahun**.

---

## Batasan Omzet Tidak Kena Pajak Rp500 Juta untuk Orang Pribadi

Untuk Wajib Pajak Orang Pribadi UMKM, PPh Final 0,5% **hanya dikenakan atas bagian omzet kumulatif yang melebihi Rp500 juta dalam 1 tahun pajak**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SKEMA OMZET TIDAK KENA PAJAK RP500 JUTA                  │
├────────────────────────────────────────┬────────────────────────────────────┤
│      OMZET KUMULATIF BULANAN           │           STATUS PAJAK             │
├────────────────────────────────────────┼────────────────────────────────────┤
│ • Omzet Bulan 1 s.d. batas Rp500 Juta  │ **BEBAS PAJAK (PPh Final = Rp0)**  │
│ • Bagian Omzet yang MELEBIHI Rp500 Jt  │ **Dikenakan Tarif PPh Final 0,5%** │
└────────────────────────────────────────┴────────────────────────────────────┘
```

> [!IMPORTANT]
> Fasilitas batas bebas pajak Rp500 juta ini **hanya berlaku untuk Wajib Pajak Orang Pribadi**. Bagi Wajib Pajak Badan (CV, PT, Koperasi), seluruh omzet dari bulan pertama langsung dikenakan tarif 0,5% tanpa batasan pembebasan Rp500 juta.

---

## Contoh Simulasi Perhitungan PPh Final UMKM

Berikut simulasi omzet toko ritel milik Tuan Ahmad (Wajib Pajak Orang Pribadi) selama satu tahun kalender:

| Bulan | Omzet Bulanan | Omzet Kumulatif | Dasar Pengenaan Pajak | PPh Final 0,5% yang Disetor |
| :--- | :---: | :---: | :---: | :---: |
| **Januari** | Rp100.000.000 | Rp100.000.000 | Rp0 (Di bawah 500 jt) | **Rp0** |
| **Februari** | Rp120.000.000 | Rp220.000.000 | Rp0 (Di bawah 500 jt) | **Rp0** |
| **Maret** | Rp150.000.000 | Rp370.000.000 | Rp0 (Di bawah 500 jt) | **Rp0** |
| **April** | Rp130.000.000 | **Rp500.000.000**| Rp0 (Pas Rp500 jt) | **Rp0** |
| **Mei** | Rp100.000.000 | Rp600.000.000 | Rp100.000.000 | **Rp500.000** |
| **Juni** | Rp120.000.000 | Rp720.000.000 | Rp120.000.000 | **Rp600.000** |

---

## Batas Waktu Penggunaan Tarif 0,5% (Jangka Waktu Berlakunya)

Tarif PPh Final 0,5% tidak berlaku selamanya, melainkan dibatasi jangka waktu tertentu untuk mendorong UMKM naik kelas menuju pembukuan:

* **Wajib Pajak Orang Pribadi:** Maksimal **7 Tahun Pajak**.
* **Wajib Pajak Badan berbentuk Koperasi, CV, atau Firma:** Maksimal **4 Tahun Pajak**.
* **Wajib Pajak Badan berbentuk Perseroan Terbatas (PT):** Maksimal **3 Tahun Pajak**.

Setelah jangka waktu tersebut berakhir, Wajib Pajak wajib menggunakan skema tarif umum PPh Pasal 17 dengan menyelenggarakan pembukuan atau Norma Penghitungan Penghasilan Neto (NPPN).

---

## Cara Membuat Kode Billing dan Membayar PPh Final 0,5%

1. Login ke situs resmi Direktorat Jenderal Pajak di `djponline.pajak.go.id` menggunakan NIK/NPWP dan kata sandi Anda.
2. Masuk ke menu **Bayar** &rarr; **e-Billing**.
3. Isi formulir surat setoran elektronik:
   * **Jenis Pajak:** `411128` (PPh Final).
   * **Jenis Setoran:** `420` (PPh Final UMKM Peredaran Bruto Tertentu).
   * **Masa Pajak:** Pilih bulan bersangkutan.
   * **Jumlah Setor:** Masukkan angka hasil perhitungan 0,5%.
4. Klik **Buat Kode Billing**.
5. Bayar kode billing melalui ATM, Mobile Banking, Internet Banking, Kantor Pos, atau e-Commerce sebelum tanggal 15 bulan berikutnya.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Jika omzet tahunan saya di bawah Rp500 juta sepanjang tahun, apakah tetap wajib lapor SPT Tahunan?
**Ya, wajib.** Meskipun tidak ada pajak yang harus disetorkan (PPh nihil), Anda tetap wajib melaporkan total omzet dan rincian harta kekayaan pada formulir SPT Tahunan PPh Orang Pribadi (Formulir 1770) sebelum tanggal 31 Maret setiap tahunnya.

---

*Panduan ini disusun berdasarkan Undang-Undang No. 7 Tahun 2021 (UU HPP) dan Peraturan Pemerintah No. 55 Tahun 2022.*
""", encoding="utf-8")

(ARTICLES / "id-asuransi-kesehatan-swasta-vs-bpjs.md").write_text("""---
title: "Asuransi Kesehatan Swasta vs BPJS Kesehatan: Perbandingan Premi, Sistem Rujukan, dan COB"
description: "Bandingkan asuransi kesehatan swasta murni (Cashless / As Charge) dengan BPJS Kesehatan. Pahami sistem rujukan berjenjang, koordinasi manfaat (COB), dan cara memilih."
slug: "id-asuransi-kesehatan-swasta-vs-bpjs"
keyword: "asuransi kesehatan swasta vs bpjs kesehatan sistem rujukan cob"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# Asuransi Kesehatan Swasta vs. BPJS Kesehatan: Panduan Memilih Proteksi Medis Keluarga

Biaya perawatan medis dan inflasi tarif rumah sakit di Indonesia rata-rata naik **10% hingga 13% per tahun**, jauh melampaui kenaikan gaji rata-rata.

Untuk melindungi tabungan keluarga dari risiko kebangkrutan medis, setiap warga negara wajib memiliki **BPJS Kesehatan**. Namun, banyak keluarga mempertimbangkan untuk menambah **Asuransi Kesehatan Swasta murni**.

Memahami kelebihan dan batasan dari masing-masing sistem proteksi ini memungkinkan Anda menyusun perlindungan optimal tanpa membuang premi secara sia-sia.

---

## Tabel Perbandingan Mendalam: BPJS vs. Asuransi Swasta

| Parameter | BPJS Kesehatan | Asuransi Kesehatan Swasta (Murni Standalone) |
| :--- | :--- | :--- |
| **Kewajiban Kepesertaan** | **Wajib bagi seluruh WNI** | Pilihan opsional / komplementer |
| **Sistem Rujukan** | **Berjenjang (Faskes 1 &rarr; Faskes 2 &rarr; RS Rujukan)** | **Bebas langsung ke Rumah Sakit Rekanan manapun** |
| **Kondisi Sudah Ada (*Pre-Existing Condition*)** | **Dicover 100% tanpa masa tunggu atau medical check-up** | Dikecualikan (*excluded*) atau dikenakan masa tunggu |
| **Metode Klaim** | Ditanggung langsung sesuai tarif INA-CBGs | **Kartu Cashless (*On Bill / As Charge*)** |
| **Fasilitas Kamar** | Kelas 1, 2, 3 (atau KRIS) | **1 Tempat Tidur (Private Room)** sesuai plafon plan |
| **Wilayah Cakupan** | Hanya di dalam wilayah NKRI | Indonesia, Asia, hingga Seluruh Dunia (*Worldwide*) |

---

## Koordinasi Manfaat (Coordination of Benefit - COB)

Banyak masyarakat belum menyadari bahwa Anda dapat **mengombinasikan BPJS Kesehatan dan Asuransi Swasta** secara sinergis melalui skema **Coordination of Benefit (COB)**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SKEMA KERJA CO-BENEFIT (COB) DI RUMAH SAKIT              │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Masuk Rumah Sakit menggunakan rujukan BPJS Kesehatan untuk kamar standar.│
│ 2. Mengajukan naik kelas kamar (misal ke VIP/VVIP) saat rawat inap.         │
│ 3. BPJS Kesehatan menanggung biaya dasar sesuai paket tarif resmi INA-CBGs. │
│ 4. Selisih biaya (*excess bill*) akibat naik kelas kamar diklaimkan ke      │
│    kartu Asuransi Swasta Anda!                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

Dengan skema COB ini, Anda mendapatkan kenyamanan fasilitas kamar VIP tanpa harus membayar selisih biaya dari kantong pribadi.

---

## Kriteria Asuransi Kesehatan Swasta yang Ideal

Jika Anda memutuskan untuk membeli asuransi kesehatan swasta pelengkap, pastikan polis memiliki fitur-fitur wajib berikut:
1. **Sistem Sesuai Tagihan (*As Charge / On Bill*):** Hindari polis asuransi jadul yang menggunakan sistem tabel batasan santunan (*inner limit*). Sistem *as charge* menanggung biaya obat dan tindakan medis sesuai tagihan rumah sakit selama berada di dalam batas tahunan.
2. **Kamar 1 Tempat Tidur (*One-Bed Private Room*):** Memberikan privasi maksimal dan meminimalkan risiko tertular infeksi silang di rumah sakit.
3. **Tanpa Batas Seumur Hidup (*High Annual Limit*):** Pilihlah batas limit tahunan minimal Rp5 Miliar hingga Rp10 Miliar untuk mengantisipasi penyakit kritis seperti kanker, bypass jantung, atau cuci darah jangka panjang.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Apakah saya boleh berhenti membayar BPJS jika sudah memiliki asuransi swasta dari kantor?
Tidak boleh. BPJS Kesehatan adalah jaminan sosial wajib negara. Selain itu, BPJS Kesehatan adalah satu-satunya jaring pengaman medis yang **menjamin penyakit bawaan lahir (*pre-existing condition*) seumur hidup**, sesuatu yang tidak ditawarkan oleh asuransi swasta komersial manapun.

---

*Panduan ini disusun berdasarkan regulasi BPJS Kesehatan dan pedoman Asosiasi Asuransi Jiwa Indonesia (AAJI).*
""", encoding="utf-8")

(ARTICLES / "id-cara-mengatur-keuangan-gaji-umr.md").write_text("""---
title: "Cara Mengatur Keuangan Gaji UMR: Rumus Budgeting Realistis, Dana Darurat, dan Tips Menabung"
description: "Panduan praktis mengelola gaji UMR (Upah Minimum Regional) di Indonesia. Model pos pengeluaran 60-20-10-10, strategi menabung dana darurat, dan proteksi dari pinjol."
slug: "id-cara-mengatur-keuangan-gaji-umr"
keyword: "cara mengatur keuangan gaji umr budgeting dana darurat menabung"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# Cara Mengatur Keuangan Gaji UMR di Indonesia: Rumus Budgeting Realistis dan Strategi Menabung

Mengelola keuangan dengan **Gaji UMR (Upah Minimum Regional / UMP)** di kota-kota besar di Indonesia—seperti Jakarta, Surabaya, Bandung, atau Semarang—sering kali terasa menantang akibat tingginya biaya kos, makan harian, dan transportasi.

Banyak pekerja terjebak dalam siklus *"gaji numpang lewat"* di minggu pertama setelah gajian, bahkan terpaksa berutang ke pinjaman online (pinjol) berbunga tinggi saat terjadi kebutuhan mendadak.

Dengan menerapkan **model alokasi anggaran yang realistis untuk kondisi biaya hidup di Indonesia**, memiliki tabungan dan dana darurat bukanlah hal yang mustahil dengan penghasilan UMR.

---

## Mengapa Rumus Tradisional 50/30/20 Tidak Cocok untuk Gaji UMR?

Rumus budgeting populer dari Barat (50% Kebutuhan, 30% Keinginan, 20% Tabungan) sering kali gagal diterapkan pada gaji UMR di Indonesia karena:
* Biaya kebutuhan pokok (sewa kos, beras, transportasi bensin/KRL, tagihan listrik, BPJS) sering kali menghabiskan **60% hingga 70% dari take-home pay**.
* Mengalokasikan 30% untuk "keinginan/hiburan" terlalu boros dan mengurangi daya tahan finansial terhadap inflasi.

---

## Rumus Budgeting Realistis Indonesia: Model 60 - 20 - 10 - 10

Untuk pekerja bergaji UMR (misalkan **Rp5.000.000 / bulan**), gunakan model proporsi 4 pos pengeluaran ini:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 RUMUS ALOKASI 60 - 20 - 10 - 10 (GAJI RP5 JUTA)             │
├──────────────────────────┬──────────────┬───────────────────────────────────┤
│           POS            │  PERSENTASE  │          NOMINAL ALOKASI          │
├──────────────────────────┼──────────────┼───────────────────────────────────┤
│ 1. Kebutuhan Pokok (Living│ **60%**     │ **Rp3.000.000** (Kos, Makan, Listrik)
│ 2. Tabungan & Dana Darurat│ **20%**     │ **Rp1.000.000** (Disisihkan diawal)│
│ 3. Biaya Sosial & Keluarga│ **10%**     │ **Rp500.000** (Kirim ortu/sedekah) │
│ 4. Hiburan & Self-Reward  │ **10%**     │ **Rp500.000** (Nongkrong, kuota)  │
└──────────────────────────┴──────────────┴───────────────────────────────────┘
```

---

## 4 Langkah Praktis Keluar dari Jebakan Gaji Numpang Lewat

1. **Prinsip "Pay Yourself First" (Menabung di Awal):** Begitu gaji masuk ke rekening di tanggal 25 atau 1, langsung transfer **Rp1.000.000 ke rekening terpisah** (misal ke Reksa Dana Pasar Uang atau bank digital tanpa kartu debit). Jangan pernah menabung dari "uang sisa di akhir bulan".
2. **Pisahkan Rekening Transaksi vs Rekening Tabungan:** Jangan satukan uang operasional harian dengan uang simpanan darurat dalam satu kartu ATM untuk menghindari godaan belanja impulsif.
3. **Bangun "Dana Darurat Pemula" Rp5 Juta Pertama:** Fokuskan seluruh pos tabungan untuk mengumpulkan dana darurat sebesar 1 bulan gaji (Rp5.000.000). Dana ini akan melindungi Anda dari jeratan pinjol saat ban motor bocor atau butuh servis laptop kerja.
4. **Haramkan Pinjol dan Paylater untuk Konsumsi:** Bunga pinjol legal bisa mencapai 0,3% per hari (lebih dari 100% per tahun). Menggunakan paylater untuk membeli makanan atau pakaian adalah jalan tercepat menuju kebangkrutan finansial.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Ke mana sebaiknya menaruh uang tabungan gaji UMR?
Tempatkan di **Reksa Dana Pasar Uang (RDPU)** melalui aplikasi fintech terdaftar OJK (Bibit, Bareksa) atau Bank Digital dengan bunga kompetitif (4%-5% p.a.) bebas biaya admin bulanan. RDPU dapat dicairkan kapan saja tanpa denda penalti.

---

*Panduan ini dirancang untuk edukasi literasi keuangan mandiri bagi generasi muda dan pekerja produktif di Indonesia.*
""", encoding="utf-8")

(ARTICLES / "id-reksadana-pasar-uang-vs-deposito.md").write_text("""---
title: "Reksa Dana Pasar Uang (RDPU) vs Deposito: Perbandingan Bunga, Pajak, dan Likuiditas"
description: "Pahami perbedaan Reksa Dana Pasar Uang (RDPU) vs Deposito Bank. Pelajari keuntungan bebas pajak RDPU (0%), pencairan T+1, dan modal awal mulai Rp10.000."
slug: "id-reksadana-pasar-uang-vs-deposito"
keyword: "reksadana pasar uang vs deposito rdpu pajak bunga likuiditas"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# Reksa Dana Pasar Uang (RDPU) vs. Deposito: Mana Tempat Terbaik untuk Menyimpan Dana Darurat?

Ketika ingin memarkir dana darurat atau tabungan jangka pendek (di bawah 1 hingga 2 tahun), mayoritas masyarakat Indonesia ragu memilih antara **Deposito Bank** konvensional atau **Reksa Dana Pasar Uang (RDPU)**.

Meskipun keduanya sama-sama memiliki profil risiko yang sangat rendah dan fluktuasi harga yang stabil, **perlakuan pajak penghasilan dan fleksibilitas pencairan** membuat RDPU sering kali menghasilkan imbal hasil bersih yang jauh lebih menguntungkan.

---

## Tabel Perbandingan Head-to-Head: RDPU vs. Deposito

| Parameter | Deposito Bank | Reksa Dana Pasar Uang (RDPU) |
| :--- | :--- | :--- |
| **Tarif Pajak Imbal Hasil**| **Pajak PPh Final 20%** dari seluruh bunga | **Pajak 0% (Bukan Objek Pajak Penghasilan)** |
| **Modal Awal Minimum** | Rp5.000.000 – Rp10.000.000 | **Mulai dari Rp10.000 – Rp100.000** |
| **Jangka Waktu (*Tenor*)** | Terkunci (1, 3, 6, atau 12 bulan) | **Bebas dicairkan kapan saja tanpa batas waktu** |
| **Penalti Penarikan Awal** | Dikenakan denda penalti & bunga hangus | **Rp0 (Bebas biaya penarikan / tanpa denda)** |
| **Keamanan Dana** | Dijamin LPS (Lembaga Penjamin Simpanan)| Disimpan aman di Bank Kustodian independen |

---

## Keuntungan Pajak 0% pada Reksa Dana Pasar Uang

Berdasarkan Undang-Undang Pajak Penghasilan (UU PPh) di Indonesia, keuntungan atau kenaikan Nilai Aktiva Bersih (NAB) dari reksa dana **bukan merupakan objek pajak**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 SIMULASI IMBAL HASIL BERSIH ATAS MODAL RP50.000.000         │
├────────────────────────────────────────┬────────────────────────────────────┤
│         DEPOSITO BANK (BUNGA 5,00%)    │            RDPU (RETURN 5,50%)     │
├────────────────────────────────────────┼────────────────────────────────────┤
│ • Bunga Kotor: Rp2.500.000 / tahun     │ • Return Kotor: Rp2.750.000 / tahun│
│ • Pajak Bunga 20%: -Rp500.000          │ • Pajak Reksa Dana (0%): -Rp0      │
│ • **Hasil Bersih: Rp2.000.000 (4,00%)**│ • **Hasil Bersih: Rp2.750.000 (+37%)
└────────────────────────────────────────┴────────────────────────────────────┘
```

Dengan nominal modal yang sama, RDPU menghasilkan **keuntungan bersih 37% lebih besar** karena tidak tergerus potongan pajak 20% dan memiliki imbal hasil dasar yang lebih kompetitif.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Apakah uang di Reksa Dana Pasar Uang bisa hilang jika manajer investasi bangkrut?
Tidak. Dana nasabah tidak disimpan di kantor manajer investasi (MI), melainkan disimpan secara terpisah di **Bank Kustodian** (bank umum besar seperti BCA, Mandiri, Citibank) yang diawasi oleh OJK. Jika perusahaan MI tutup, dana Anda tetap aman di bank kustodian dan akan dialihkan atau dikembalikan 100% kepada nasabah.

---

*Panduan ini disusun berdasarkan regulasi Otoritas Jasa Keuangan (OJK) dan UU Pajak Penghasilan Republik Indonesia.*
""", encoding="utf-8")

(ARTICLES / "id-pajak-saham-dan-dividen-bei.md").write_text("""---
title: "Pajak Saham dan Dividen di Indonesia: Aturan PPh Final 0,1%, Dividen Bebas Pajak, dan Lapor SPT"
description: "Panduan lengkap pajak saham BEI dan dividen di Indonesia: tarif PPh Final 0,1% transaksi jual, syarat dividen bebas pajak (UU Cipta Kerja), dan cara lapor di SPT Tahunan."
slug: "id-pajak-saham-dan-dividen-bei"
keyword: "pajak saham dividen bei pph final 0 1 persen bebas pajak spt tahunan"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# Pajak Saham dan Dividen di Indonesia: Aturan PPh Final 0,1%, Syarat Bebas Pajak, dan Pelaporan SPT

Bagi investor yang aktif bertransaksi saham di Bursa Efek Indonesia (BEI), memahami kewajiban perpajakan atas **keuntungan penjualan saham (capital gain)** dan **penghasilan dividen** sangat penting untuk menghindari denda administrasi perpajakan.

Kabar baiknya, sistem perpajakan pasar modal di Indonesia sangat ramah bagi investor ritel: pajak transaksi bersifat final dan otomatis dipotong oleh pihak sekuritas, serta **dividen saham dapat dinikmati 100% bebas pajak** jika diinvestasikan kembali di dalam negeri.

---

## 1. Pajak Penjualan Saham di Bursa Efek Indonesia (PPh Final 0,1%)

Setiap kali Anda **menjual saham** melalui aplikasi sekuritas di BEI, Anda akan dikenakan **PPh Final Pasal 4 Ayat (2) sebesar 0,1% dari nilai bruto transaksi penjualan**:

$$\\text{PPh Final Penjualan Saham} = 0,1\\% \\times \\text{Nilai Bruto Penjualan}$$

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    KETENTUAN PAJAK TRANSAKSI SAHAM BEI                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Pajak 0,1% dipotong **otomatis oleh broker/sekuritas** saat settlement. │
│ 2. Dikenakan hanya atas transaksi **JUAL** (transaksi BELI tidak kena PPh). │
│ 3. Berlaku baik saat Anda untung (*capital gain*) maupun saat rugi.         │
│ 4. Karena bersifat FINAL, Anda tidak perlu membayar pajak tambahan saat     │
│    lapor SPT Tahunan.                                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Pajak Dividen Saham: Syarat Bebas Pajak 0% (UU Cipta Kerja)

Berdasarkan UU Cipta Kerja dan PMK No. 18/PMK.03/2021:
* **Dividen Saham Dalam Negeri BEBAS PAJAK (0%)** bagi Wajib Pajak Orang Pribadi, dengan syarat:
  * Dividen tersebut **diinvestasikan kembali di wilayah Negara Kesatuan Republik Indonesia (NKRI)** dalam jangka waktu minimal **3 tahun pajak**.
  * Instrumen investasi yang diakui sangat luas: membeli saham BEI kembali, SBN Ritel, Reksadana, Emas Batangan, Deposito, atau modal usaha sektor riil.
* **Jika Tidak Diinvestasikan Kembali:** Dividen akan dikenakan tarif **PPh Final sebesar 10%** dan harus disetorkan sendiri oleh Wajib Pajak melalui e-Billing DJP.

---

## Cara Melaporkan Saham dan Dividen di SPT Tahunan

1. **Lapor Kepemilikan Portofolio (Daftar Harta):** Masukkan seluruh saham yang masih Anda miliki per tanggal 31 Desember dengan kode harta `031` (Saham yang dibeli untuk dijual kembali) berdasarkan **harga perolehan beli (modal awal)**, bukan harga pasar terkini.
2. **Lapor Penjualan Saham:** Masukkan total akumulasi nilai penjualan saham setahun pada lampiran **Penghasilan yang Dikenakan PPh Final** (Kode: Penjualan Saham di Bursa Efek, Tarif 0,1%).
3. **Lapor Dividen Bebas Pajak:** Masukkan total dividen yang diinvestasikan kembali pada bagian **Penghasilan yang Tidak Termasuk Objek Pajak**.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Di mana saya bisa mendapatkan rincian bukti potong pajak saham setahun?
Setiap bulan Januari atau Februari, seluruh perusahaan sekuritas (seperti Stockbit, Mirae, Mandiri Sekuritas, Indo Premier) akan menerbitkan dokumen **Laporan Pajak Tahunan / Bukti Potong Saham** di dashboard nasabah yang merangkum seluruh penjualan dan dividen Anda.

---

*Panduan ini disusun berdasarkan PP No. 14 Tahun 1997 dan PMK No. 18/PMK.03/2021 Direktorat Jenderal Pajak.*
""", encoding="utf-8")

(ARTICLES / "id-investasi-emas-batangan-vs-digital.md").write_text("""---
title: "Investasi Emas Batangan Fisik vs Emas Digital: Spread Harga, Biaya Cetak, dan Pajak"
description: "Bandingkan investasi emas batangan Antam/UBS dengan emas digital berizin Bappebti. Pahami selisih spread harga jual-beli, biaya cetak fisik, dan pajak PPh 22."
slug: "id-investasi-emas-batangan-vs-digital"
keyword: "investasi emas batangan antam vs emas digital spread harga cetak pph 22"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# Investasi Emas Batangan Fisik vs. Emas Digital: Panduan Memilih Safe Haven Terbaik

Emas telah terbukti selama ribuan tahun sebagai aset penyimpan nilai (*safe haven*) dan pelindung kekayaan dari ancaman inflasi serta depresiasi nilai tukar rupiah.

Di era modern, investor di Indonesia memiliki dua cara utama untuk memiliki emas: **Emas Batangan Fisik (Antam / UBS / Galeri 24)** yang disimpan di brankas pribadi, atau **Emas Digital** yang dibeli secara online melalui aplikasi pedagang fisik emas berizin Bappebti.

Memahami **selisih harga jual-beli (*spread*), biaya cetak fisik, dan aspek perpajakannya** sangat penting agar modal investasi Anda tidak tergerus biaya tersembunyi.

---

## Perbandingan Langsung: Emas Fisik vs. Emas Digital

| Fitur / Parameter | Emas Batangan Fisik (Antam/UBS) | Emas Digital (Berizin Bappebti) |
| :--- | :--- | :--- |
| **Wujud Kepemilikan** | Logam mulia fisik berkadar 99,99% (24 Karat) | Saldo gramasi emas dalam aplikasi (bisa dicetak) |
| **Minimum Pembelian** | Mulai 0,5 gram (~Rp700.000-an) | **Mulai dari Rp5.000 – Rp10.000 (0,005 gram)** |
| **Spread Harga (Selisih Beli-Jual)** | **Lebih Lebar (sekitar 8% – 12%)** | **Lebih Ramping (sekitar 2% – 4%)** |
| **Biaya Cetak Fisik** | Sudah termasuk dalam harga beli pecahan | Dikenakan biaya cetak jika ingin ditarik fisik |
| **Biaya Penyimpanan** | Biaya brankas / Safe Deposit Box (SDB) Bank | **Gratis** (Disimpan di Kustodian Kliring Berjangka) |
| **Risiko Kehilangan Fisik** | Ada risiko pencurian / kebakaran rumah | Bebas risiko pencurian fisik di rumah |

---

## Mengapa Emas Digital Cocok untuk Dollar-Cost Averaging (DCA)?

Jika Anda memiliki anggaran menabung rutin Rp100.000 hingga Rp500.000 per bulan:
* **Pada Emas Fisik:** Anda tidak bisa membeli pecahan kecil setiap minggu tanpa membayar premi harga per gram yang sangat mahal (emas pecahan 0,5 gram memiliki harga per gram yang jauh lebih tinggi dibanding emas 100 gram).
* **Pada Emas Digital:** Anda dapat membeli emas dengan harga grosir pasar spot dunia secara proporsional sesuai nominal uang yang Anda miliki, dengan spread harga jual-kembali yang jauh lebih bersahabat.

---

## Pajak Pembelian Emas Batangan (PPh Pasal 22)

Sesuai PMK No. 48/PMK.03/2023:
* Pembelian emas batangan fisik dikenakan **PPh Pasal 22 sebesar 0,25%** jika pembeli menyertakan Nomor Pokok Wajib Pajak (NPWP).
* Bukti potong PPh 22 ini dapat dikreditkan pada SPT Tahunan Orang Pribadi Anda untuk mengurangi beban pajak terutang.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Apakah emas digital aman dan benar-benar ada emas fisiknya?
Aman, asalkan Anda bertransaksi di platform yang **terdaftar dan diawasi oleh Bappebti (Badan Pengawas Perdagangan Berjangka Komoditi)** dan terintegrasi dengan lembaga kliring (seperti Kliring Berjangka Indonesia / Indonesia Clearing House). Seluruh emas fisik nasabah disimpan 1:1 di tempat penyimpanan terakreditasi.

---

*Panduan ini disusun berdasarkan regulasi Bappebti Kementerian Perdagangan dan PMK No. 48 Tahun 2023.*
""", encoding="utf-8")

(ARTICLES / "id-dana-darurat-keluarga-muda.md").write_text("""---
title: "Dana Darurat Keluarga Muda di Indonesia: Panduan Menghitung Target, Pos Alokasi, dan Penempatan"
description: "Panduan praktis membangun dana darurat untuk keluarga muda di Indonesia. Rumus 6-12 bulan pengeluaran rutin, proteksi saat punya anak/KPR, dan instrumen penempatan aman."
slug: "id-dana-darurat-keluarga-muda"
keyword: "dana darurat keluarga muda indonesia target penempatan rdpu"
date: "2026-08-19"
category: "Indonesia"
lang: "id"
---

# Dana Darurat Keluarga Muda di Indonesia: Panduan Menghitung Target dan Tempat Penyimpanannya

Bagi pasangan muda yang baru menikah, memiliki momongan baru, atau baru saja mengambil komitmen cicilan KPR, membangun **Dana Darurat (Emergency Fund)** adalah fondasi utama yang wajib diselesaikan sebelum terjun ke instrumen investasi agresif seperti saham atau kripto.

Kehidupan berkeluarga membawa dinamika pengeluaran yang jauh lebih kompleks dibanding masa lajang: risiko anak sakit mendadak, keterlambatan pembayaran klien bagi kepala keluarga pencari nafkah, hingga renovasi kebocoran atap rumah.

Tanpa bantalan dana darurat yang memadai, keluarga muda sangat rentan terjerembap ke dalam lingkaran utang konsumtif dan pinjaman berbunga tinggi.

---

## Berapa Target Dana Darurat yang Ideal untuk Keluarga Muda?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 RUMUS TARGET DANA DARURAT BERDASARKAN STATUS                │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│       STATUS KELUARGA        │  SUMBER PENGHASILAN UTAMA    │  TARGET DANA  │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 1. Menikah Tanpa Anak        │ Gaji Karyawan Tetap          │ **6 Bulan**   │
│ 2. Menikah + 1 Anak / KPR    │ Gaji Karyawan Tetap          │ **9 Bulan**   │
│ 3. Menikah + Anak + KPR      │ Freelancer / Wiraswasta      │ **12 Bulan**  │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

> [!TIP]
> **Hitung dari Pengeluaran Pokok, Bukan Gaya Hidup:** Jika pengeluaran rutin bulanan keluarga untuk makan, popok anak, susu, listrik, internet, dan cicilan KPR adalah **Rp8.000.000 / bulan**, maka target dana darurat 6 bulan Anda adalah **Rp48.000.000** (bukan dihitung dari gaji kotor).

---

## 3 Tempat Terbaik Menyimpan Dana Darurat di Indonesia

Dana darurat harus memenuhi 3 kriteria mutlak: **Aman (Bebas Risiko Turun Nilai), Likuid (Mudah Dicairkan dalam 1-2 Hari), dan Terpisah dari Rekening Harian**.

1. **Reksa Dana Pasar Uang (RDPU) - Alokasi 60%:** Bebas pajak, imbal hasil ~5% p.a., pencairan T+1.
2. **Tabungan Bank Digital / Bank BUMN - Alokasi 30%:** Untuk kebutuhan darurat instan hitungan menit di tengah malam (obat anak, periksa dokter IGD).
3. **Emas Batangan Fisik / Deposito Tenor Pendek - Alokasi 10%:** Cadangan benteng pertahanan terakhir keluarga.

---

## Pertanyaan yang Sering Diajukan (FAQ)

### Bolehkah dana darurat diinvestasikan ke saham dividen atau kripto?
**Sangat tidak dianjurkan.** Saham dan kripto memiliki volatilitas harga tinggi. Jika terjadi kondisi darurat saat pasar saham sedang jatuh 20%, Anda akan terpaksa menjual aset dalam kondisi rugi (*cut loss*), menghancurkan nilai tabungan yang sudah susah payah dikumpulkan.

---

*Panduan ini disusun untuk edukasi perencanaan keuangan keluarga mandiri di Indonesia.*
""", encoding="utf-8")

# 8 English Articles
(ARTICLES / "hsa-vs-fsa-health-savings-explained.md").write_text("""---
title: "HSA vs FSA: The Triple Tax Advantage of Health Savings Accounts Explained"
description: "Compare HSA vs FSA health accounts. Learn the triple tax advantages of an HSA, rollover rules, qualified medical expenses, and stealth retirement investing strategies."
slug: "hsa-vs-fsa-health-savings-explained"
keyword: "hsa vs fsa triple tax advantage health savings"
date: "2026-08-19"
category: "Taxes & Income"
---

# HSA vs. FSA: Comparing Tax-Advantaged Healthcare Accounts and the Power of the "Triple Tax Advantage"

Navigating employer healthcare benefits during open enrollment often forces employees to choose between two powerful pre-tax savings vehicles: the **Health Savings Account (HSA)** and the **Flexible Spending Account (FSA)**.

While both accounts allow you to pay for qualified medical expenses using pre-tax dollars—effectively discounting your healthcare and prescription costs by your marginal income tax rate—they operate under fundamentally different rules regarding **eligibility, ownership, investment capabilities, and annual rollovers**.

Understanding how these accounts work can turn a basic healthcare buffer into one of the most powerful wealth-building tools in the entire tax code.

---

## Side-by-Side Comparison: HSA vs. Healthcare FSA

| Feature | Health Savings Account (HSA) | Flexible Spending Account (FSA) |
| :--- | :--- | :--- |
| **Plan Requirement** | **Must be enrolled in a High-Deductible Health Plan (HDHP)** | Any health plan (or no health plan, depending on employer) |
| **Account Ownership** | **Owned by YOU** (Individually owned; 100% portable if you leave job) | **Owned by EMPLOYER** (Funds forfeited if you leave the company) |
| **Rollover Rules** | **100% rolls over year after year forever** (No expiration) | **"Use It or Lose It"** (Max $640 rollover or 2.5-month grace period) |
| **Investment Capabilities** | **Yes** (Can invest in index funds, stocks, and bonds tax-free) | **No** (Held as a cash balance; earns 0% investment return) |
| **Contribution Source** | Employee, employer, or direct personal contribution | Employee salary reduction + optional employer contribution |
| **2024 / 2026 Contribution Limits**| Individual: **$4,150–$4,300** | Family: **$8,300–$8,550** | Individual cap: **$3,200–$3,300** per employer |

---

## The "Triple Tax Advantage" of the HSA

The Health Savings Account is unique in the entire United States tax code because it is the **only account that offers a Triple Tax Advantage**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          THE HSA TRIPLE TAX SHIELD                          │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│    1. TAX-FREE DEPOSIT   │    2. TAX-FREE GROWTH    │  3. TAX-FREE WITHDRAW │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ Contributions are 100%   │ All interest, dividends, │ Withdrawals used for  │
│ tax-deductible (pre-tax),│ and capital gains grow   │ qualified healthcare  │
│ reducing current income. │ completely tax-free.     │ expenses are 100% free│
│ Also exempt from FICA.   │                          │ of federal/state tax. │
└──────────────────────────┴──────────────────────────┴───────────────────────┘
```

By comparison:
* A **Traditional 401(k) / IRA** gives you pre-tax contributions and tax-deferred growth, but withdrawals in retirement are taxed as ordinary income.
* A **Roth 401(k) / IRA** gives you tax-free growth and tax-free withdrawals, but requires post-tax contributions upfront.
* An **HSA combines the best of both worlds**: tax deduction going in, tax-free compounding in the middle, and tax-free distribution coming out.

---

## The Stealth Retirement Strategy: The "Receipt Shoebox" Method

Because HSA funds never expire and can be invested in broad-market index funds, savvy financial planners use the HSA as an auxiliary **Stealth Retirement Account**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE HSA STEALTH INVESTING CYCLE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Max out annual HSA contributions each year.                              │
│ 2. Invest the full balance into low-cost broad-market index funds.          │
│ 3. Pay current out-of-pocket medical bills using cash / regular checking.   │
│ 4. Scan and digitally store all medical receipts and invoices.              │
│ 5. Let the invested HSA compound tax-free for 20 to 30 years.               │
│ 6. Reimburse yourself tax-free decades later in retirement for past claims! │
└─────────────────────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **No Time Limit on Reimbursement:** Current IRS regulations impose **no deadline** on when you must reimburse yourself for an eligible medical expense, as long as the expense was incurred after the HSA was established. A medical procedure paid out-of-pocket in 2026 can be reimbursed tax-free from your HSA in 2056!

### What Happens at Age 65?
Once you reach age 65, your HSA gains even more flexibility: you can withdraw funds for **any non-medical expense without penalty**, paying standard ordinary income tax—effectively functioning exactly like a Traditional IRA, while retaining 100% tax-free withdrawals for all ongoing healthcare costs.

---

## When Does an FSA Make More Sense?

While the HSA has superior long-term wealth mechanics, a **Healthcare FSA** is preferable if:
1. **You Have High, Predictable Medical Needs:** If you or your family manage chronic medical conditions, require frequent specialist visits, or take expensive brand-name medications, a **Low-Deductible Health Plan (PPO)** with an FSA will often result in lower total annual out-of-pocket costs than a High-Deductible Health Plan (HDHP).
2. **Immediate Upfront Access to Annual Funds:** An FSA makes your entire annual elected contribution available on **Day 1 of the plan year**, even though payroll deductions are spread evenly across 12 months. If you need a $3,000 dental procedure in January, the FSA covers it immediately.

---

## Frequently Asked Questions (FAQ)

### Can I have both an HSA and an FSA in the same year?
Generally, no. You cannot contribute to a standard General Healthcare FSA and an HSA simultaneously. However, you can pair an HSA with a **Limited-Purpose FSA (LPFSA)** (which covers only dental and vision expenses) or a **Dependent Care FSA** (which covers childcare expenses).

### What qualifies as an eligible HSA / FSA medical expense?
Under IRS Section 213(d), qualified expenses include doctor co-pays, hospital deductibles, prescription medications, dental cleanings, orthodontics, eye exams, prescription eyeglasses, LASIK eye surgery, hearing aids, mental health therapy, and over-the-counter menstrual products and pain relievers.

### What happens if I use HSA funds for non-medical expenses before age 65?
If you withdraw HSA funds for non-qualified expenses before age 65, you will owe ordinary income tax on the withdrawal **plus a steep 20% IRS penalty**.

---

*This article is for general educational purposes only and is not personalized tax or financial advice. Consult a qualified CPA or licensed financial planner for guidance specific to your tax bracket and health plan options.*
""", encoding="utf-8")

(ARTICLES / "asset-allocation-by-age-investing-guide.md").write_text("""---
title: "Asset Allocation by Age: The Rule of 110, Stocks vs Bonds, and Portfolio Rebalancing"
description: "Master target asset allocation across your 20s, 30s, 40s, 50s, and retirement. Learn the Rule of 110, equity vs fixed income glide paths, and annual rebalancing strategies."
slug: "asset-allocation-by-age-investing-guide"
keyword: "asset allocation by age stocks bonds rule of 110"
date: "2026-08-19"
category: "Investing"
---

# Asset Allocation by Age: How to Structure Your Portfolio from Your 20s to Retirement

In modern portfolio theory, **asset allocation**—how you divide your total investment capital between broad asset classes like equities (stocks), fixed income (bonds), and cash—determines over **90% of your portfolio's total return variance and risk profile**, far outweighing individual stock picking or market timing.

As you progress through different life stages, your investment strategy must evolve. In your 20s and 30s, your primary asset is your **human capital** (decades of future earning power), allowing you to embrace aggressive equity growth. As you approach retirement in your 50s and 60s, your primary goal shifts toward **capital preservation** and mitigating **sequence-of-returns risk**.

Understanding how to construct an age-appropriate asset allocation ensures you maximize compounding when young while protecting your nest egg as you transition into retirement.

---

## The Rule of 110 and Modern Glide Paths

Historically, financial advisors used the traditional **"Rule of 100"** (subtract your age from 100 to determine your equity allocation percentage). However, because medical advancements have extended human lifespans and a 30-year retirement is now commonplace, modern advisors use the **"Rule of 110" or "Rule of 120"**:

$$\\text{Stock Allocation Percentage} = 110 - \\text{Your Current Age}$$

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE MODERN ASSET ALLOCATION GLIDE PATH                   │
├─────────────┬───────────────────────────┬───────────────────────────────────┤
│     AGE     │      STOCKS (EQUITIES)    │       BONDS (FIXED INCOME)        │
├─────────────┼───────────────────────────┼───────────────────────────────────┤
│ **20s**     │ **90% - 100%**            │ **0% - 10%**                      │
│ **30s**     │ **80% - 90%**             │ **10% - 20%**                     │
│ **40s**     │ **70% - 80%**             │ **20% - 30%**                     │
│ **50s**     │ **60% - 70%**             │ **30% - 40%**                     │
│ **60s+**    │ **40% - 60%**             │ **40% - 60% (+ Cash Buffer)**     │
└─────────────┴───────────────────────────┴───────────────────────────────────┘
```

---

## Asset Allocation Across Life Stages

### 1. In Your 20s: The Maximum Growth Phase (90/10 or 100/0)
* **Time Horizon:** 35 to 45 years until retirement.
* **Risk Capacity:** Extremely high. If the stock market drops 40% in a global bear market, you have four decades for asset prices to recover and compound.
* **Recommended Core Portfolio:** 
  * 70% Total US Stock Market (e.g., VTI / VOO)
  * 30% Total International Stock Market (e.g., VXUS)
  * 0%–10% Total Bond Market (e.g., BND)

### 2. In Your 30s: The Wealth Accumulation Phase (80/20)
* **Time Horizon:** 25 to 35 years until retirement.
* **Risk Capacity:** High, but balancing major financial commitments (mortgages, raising young children).
* **Recommended Core Portfolio:** 
  * 60% US Equities
  * 20% International Equities
  * 20% Intermediate-Term Government & Investment-Grade Corporate Bonds

### 3. In Your 40s: The Peak Earning & Consolidation Phase (70/30)
* **Time Horizon:** 15 to 25 years until retirement.
* **Focus:** Maintaining growth while introducing enough fixed income to dampen dramatic portfolio drawdowns.
* **Recommended Core Portfolio:** 
  * 50% US Equities
  * 20% International Equities
  * 25% Total Bond Market
  * 5% Inflation-Protected Securities (TIPS)

### 4. In Your 50s: The Pre-Retirement Transition Phase (60/40)
* **Time Horizon:** 5 to 15 years until retirement.
* **Focus:** Protecting against **Sequence-of-Returns Risk** (the risk of experiencing a severe market crash right before you begin liquidating assets for living expenses).
* **Recommended Core Portfolio:** 
  * 45% US Equities
  * 15% International Equities
  * 30% High-Quality Bonds & Treasuries
  * 10% Cash, Short-Term CDs, or Money Market Funds

### 5. In Retirement (Age 60+): The Distribution & Cash Flow Phase (50/50)
* **Time Horizon:** Ongoing distributions across a 20-to-30 year retirement.
* **Focus:** Generating reliable monthly cash flow while keeping enough equities to beat long-term inflation.
* **The "3-Bucket Retirement Framework":**
  * **Bucket 1 (1–2 Years of Living Expenses):** 100% Cash / High-Yield Savings / Short-Term Treasury Bills.
  * **Bucket 2 (3–8 Years of Expenses):** Intermediate Bonds, TIPS, and Dividend Aristocrats.
  * **Bucket 3 (Long-Term Growth 9+ Years):** Diversified global equity index funds.

---

## The Critical Importance of Annual Portfolio Rebalancing

Over time, different asset classes grow at different rates. If a bull market causes your stocks to surge by 25% in a year while bonds return 4%, your target **80/20 portfolio will drift into an 88/12 allocation**, exposing you to significantly more downside risk than intended.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          HOW REBALANCING ENFORCES                           │
│                         "BUY LOW AND SELL HIGH"                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. When stocks rally dramatically: You trim a small portion of equities and │
│    purchase undervalued fixed income bonds.                                 │
│ 2. When stocks crash in a bear market: You reallocate fixed income gains to │
│    buy discounted equities at market bottoms.                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **Tax-Efficient Rebalancing:** To avoid triggering capital gains taxes in taxable brokerage accounts, rebalance using **new ongoing contributions** (directing new monthly savings into the underweight asset class) rather than selling existing appreciated shares.

---

## Frequently Asked Questions (FAQ)

### Can I hold 100% stocks in my 20s and 30s?
Yes. Investors with a high risk tolerance, stable careers, and a 30+ year timeline often hold 100% equities to maximize long-term geometric compounding. However, you must possess the emotional fortitude never to panic-sell during 30%–50% bear market drawdowns.

### Why hold bonds when bond returns are lower than stocks?
Bonds are not held to maximize return; they are held to **stabilize the portfolio and provide rebalancing liquidity**. During severe equity bear markets, high-quality government bonds often appreciate or hold their value, giving you a safe asset to sell to buy cheap equities.

---

*This article is for general educational purposes only and is not personalized investment advice. Asset allocations should be personalized to your unique risk tolerance, net worth, and tax circumstances.*
""", encoding="utf-8")

(ARTICLES / "backdoor-roth-ira-step-by-step-guide.md").write_text("""---
title: "Backdoor Roth IRA Guide: Step-by-Step Mechanics, Pro-Rata Rule, and IRS Form 8606"
description: "Learn how high earners can legally fund a Roth IRA using the Backdoor Roth strategy. Understand the pro-rata rule, conversion timing, and IRS Form 8606 reporting."
slug: "backdoor-roth-ira-step-by-step-guide"
keyword: "backdoor roth ira guide pro rata rule form 8606"
date: "2026-08-19"
category: "Investing"
---

# The Backdoor Roth IRA: A Complete Step-by-Step Guide for High Earners

A **Roth IRA** is widely considered one of the most attractive retirement accounts in the United States because investments compound **100% tax-free**, and qualified withdrawals in retirement are completely exempt from federal and state income taxes.

However, the IRS imposes strict **Modified Adjusted Gross Income (MAGI) income limits** on who can contribute directly to a Roth IRA. High-earning professionals, dual-income couples, and successful entrepreneurs who earn above these thresholds are prohibited from making standard direct contributions.

The **Backdoor Roth IRA** is a completely legal, IRS-sanctioned workaround that allows high-income earners to circumvent income caps by making a non-deductible contribution to a Traditional IRA and immediately converting those funds into a Roth IRA.

---

## 2024 / 2026 Roth IRA Income Limits Overview

If your income exceeds the phase-out range established by the IRS, you must use the Backdoor Roth IRA strategy:

```
┌──────────────────────────────────────────────┬──────────────────────────────────────────────┐
│             SINGLE TAX FILERS                │        MARRIED FILING JOINTLY (MFJ)          │
├──────────────────────────────────────────────┼──────────────────────────────────────────────┤
│ • Under $146,000 MAGI: Full Contribution     │ • Under $230,000 MAGI: Full Contribution     │
│ • $146,000 - $161,000: Partial Phase-Out     │ • $230,000 - $240,000: Partial Phase-Out     │
│ • **Above $161,000: 0% Direct Contribution** │ • **Above $240,000: 0% Direct Contribution** │
│   *(Must Use Backdoor Roth)*                 │   *(Must Use Backdoor Roth)*                 │
└──────────────────────────────────────────────┴──────────────────────────────────────────────┘
```

---

## The 4-Step Backdoor Roth IRA Execution Blueprint

Executing a Backdoor Roth IRA is straightforward when performed correctly:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE 4-STEP BACKDOOR CONVERSION CYCLE                     │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│ 1. OPEN TRADITIONAL IRA  │ 2. NON-DEDUCTIBLE DEPOSIT│ 3. CONVERT TO ROTH    │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ Open a standard          │ Deposit up to annual max │ Convert the entire    │
│ Traditional IRA at your  │ ($7,000 / $8,000 if 50+) │ cash balance into your│
│ brokerage (Vanguard,     │ as a **non-deductible**  │ Roth IRA (Leave cash  │
│ Fidelity, Schwab).       │ post-tax contribution.   │ uninvested for 1-2 d).│
└──────────────────────────┴──────────────────────────┴───────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       4. FILE IRS FORM 8606 AT TAX TIME                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ Report the non-deductible basis to the IRS on Form 8606 so the conversion   │
│ is officially recorded as 100% tax-free with zero double taxation.          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Step 1: Open Traditional & Roth IRA Accounts
Open both an empty Traditional IRA and an empty Roth IRA at the same major brokerage firm (e.g., Fidelity, Vanguard, or Charles Schwab).

### Step 2: Make a Non-Deductible Contribution to the Traditional IRA
Transfer your annual contribution (e.g., $7,000) from your checking account into the Traditional IRA. 
* **Crucial Rule:** Leave the funds in the core **money market cash settlement fund**. Do not invest the money into stocks or mutual funds yet; you want to avoid generating taxable interest gains before conversion.

### Step 3: Execute the Roth Conversion
As soon as the cash deposit settles (usually 1 to 3 business days), click **"Transfer / Convert to Roth IRA"** on your brokerage dashboard. Select 100% of the balance and choose "Do not withhold taxes."

### Step 4: Invest Inside the Roth IRA
Once the funds arrive in your Roth IRA, invest the balance into your desired long-term asset allocation (such as broad-market index funds like VTI, VOO, or target-date retirement funds).

---

## The Pro-Rata Rule: The Costly Trap to Avoid

The most common and expensive mistake high earners make with a Backdoor Roth IRA is violating the **IRS Pro-Rata Rule (IRC Section 408(d)(2))**.

### What Is the Pro-Rata Rule?
When you execute a Roth conversion, the IRS treats **ALL of your combined Traditional IRAs, SEP IRAs, and SIMPLE IRAs as a single aggregate pool of money**. 

If you already hold pre-tax dollars in any Traditional IRA, the IRS forces you to convert a proportional blend of pre-tax and post-tax funds, triggering an unexpected tax bill!

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           THE PRO-RATA TAX FORMULA                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                            Total Pre-Tax IRA Balances                       │
│ Percentage Subject to Tax = ─────────────────────────────────────────────── │
│                            Total Overall IRA Balances (Pre-Tax + After-Tax) │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Worked Example: The $70,000 Pre-Tax IRA Trap
* Suppose you have **$63,000** sitting in a rollover Traditional IRA from an old job (pre-tax).
* You deposit **$7,000** in after-tax cash to do a Backdoor Roth IRA.
* Total aggregate IRA balance = **$70,000**.
* **Pre-tax ratio:** $\frac{\$63,000}{\$70,000} = \mathbf{90\%}$.
* When you convert your $7,000 to a Roth IRA, **90% of the conversion ($6,300) will be treated as taxable income**, costing you thousands in unnecessary taxes!

### How to Fix the Pro-Rata Trap (The Reverse Rollover):
Before executing a Backdoor Roth IRA, roll your pre-tax Traditional/SEP/SIMPLE IRA balances **into your current employer's 401(k) or 403(b) plan**. Employer 401(k) plans are legally excluded from the pro-rata calculation, reducing your aggregate personal IRA pre-tax balance to **$0.00** and unlocking a 100% tax-free backdoor conversion.

---

## Reporting on IRS Form 8606

When you file your annual tax return, your CPA or tax software (TurboTax, H&R Block) must generate **IRS Form 8606 (Nondeductible IRAs)**:
1. **Line 1:** Lists your non-deductible contribution ($7,000).
2. **Line 2:** Lists your prior year basis ($0).
3. **Line 14:** Reports your total basis.
4. **Line 18:** Confirms the taxable amount of the conversion is **$0.00**.

---

## Frequently Asked Questions (FAQ)

### Is the Backdoor Roth IRA legal?
**Yes, 100% legal.** The legality of the Backdoor Roth conversion was explicitly affirmed in the congressional conference committee report for the Tax Cuts and Jobs Act (TCJA) of 2017.

### What happens if my Traditional IRA earns $1 or $2 in interest before conversion?
If your cash deposit earns $1.50 in interest while waiting for settlement, convert the entire balance ($7,001.50). You will simply report $1.50 of taxable income on your Form 8606 at tax time, which results in a negligible tax impact of under a dollar.

---

*This article is for general educational purposes only and is not personalized tax advice. Consult a licensed CPA or tax professional before executing a conversion.*
""", encoding="utf-8")

(ARTICLES / "cd-ladder-vs-high-yield-savings.md").write_text("""---
title: "CD Ladder vs High-Yield Savings Account: Locking in Yields and Avoiding Cash Traps"
description: "Compare a Certificate of Deposit (CD) Ladder strategy with a High-Yield Savings Account (HYSA). Learn interest rate risk, liquidity schedules, and early withdrawal penalties."
slug: "cd-ladder-vs-high-yield-savings"
keyword: "cd ladder vs high yield savings account hysa interest rates"
date: "2026-08-19"
category: "Budgeting & Debt"
---

# CD Ladder vs. High-Yield Savings Account: How to Maximize Yield on Cash Reserves

When market interest rates fluctuate, savers face an essential dilemma regarding where to park their short-term cash reserves, home down payments, and emergency funds:

* Should you keep your money in a **High-Yield Savings Account (HYSA)** for maximum liquidity?
* Or should you lock in fixed yields using a **Certificate of Deposit (CD) Ladder** to protect against central bank rate cuts?

Both cash management strategies are backed by federal insurance (FDIC in the US up to $250,000 per depositor per institution), but they behave completely differently when monetary policy and benchmark interest rates change.

---

## Direct Comparison: CD Ladder vs. HYSA

| Parameter | High-Yield Savings Account (HYSA) | Certificate of Deposit (CD) Ladder |
| :--- | :--- | :--- |
| **Interest Rate Type** | **Variable** (Bank can lower or raise rate anytime without notice) | **Guaranteed Fixed** for the entire duration of the CD term |
| **Liquidity & Access** | **Instant (100% Liquid)** via electronic ACH transfer or debit | **Staggered Liquidity** (Tranches mature every 3, 6, or 12 months) |
| **Early Withdrawal Cost**| $0.00 (No penalties for moving funds) | Early withdrawal penalty (typically 3 to 6 months of interest) |
| **Interest Rate Risk** | High risk of yield dropping when central banks cut rates | **Zero risk of yield dropping** on existing active CDs |
| **Setup Complexity** | Simple (Open 1 bank account and deposit cash) | Moderate (Requires opening 4 to 5 staggered CD maturities) |

---

## How a CD Ladder Works (The Staggered Liquidity Engine)

A **CD Ladder** is a structured savings strategy where you divide a single pool of cash into equal portions and invest each portion into a CD with a different maturity date (e.g., 3-month, 6-month, 9-month, and 12-month CDs):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      HOW A 1-YEAR CD LADDER OPERATES                        │
├─────────────────┬─────────────────┬─────────────────┬───────────────────────┤
│   CD 1: 3 MONTHS│   CD 2: 6 MONTHS│   CD 3: 9 MONTHS│   CD 4: 12 MONTHS     │
│       ($5,000)  │       ($5,000)  │       ($5,000)  │       ($5,000)        │
└─────────────────┴─────────────────┴─────────────────┴───────────────────────┘
         │
         ▼ (After 3 Months)
   CD 1 Matures!
   • Need cash? Withdraw $5,000 + interest.
   • Don't need cash? Roll over into a new 12-Month CD to keep the ladder going!
```

---

## Worked Example: Structuring a $20,000 Cash Allocation

Suppose you have **$20,000** allocated for an intermediate goal (such as buying a home in 18 months). Here is how a disciplined 4-rung CD ladder compares to a variable HYSA during an interest rate cut cycle:

### Scenario: Central Banks Cut Rates by 1.50% Over the Next Year
* **Option A (100% in HYSA):** You start earning 5.00% APY. As the central bank cuts rates, your bank gradually lowers your yield to 4.25%, then 3.75%, and finally 3.50%.
  * **Average Blended Annual Yield:** **~4.12%**
  * **Total Annual Interest Earned:** **$824.00**

* **Option B (4-Rung CD Ladder):** You split $20,000 into four $5,000 rungs (3-mo, 6-mo, 9-mo, 12-mo) locked at an initial 5.25% fixed rate.
  * **Average Blended Annual Yield:** **~5.15%**
  * **Total Annual Interest Earned:** **$1,030.00**

**Result:** The CD ladder generated an **extra +$206 in guaranteed income (+25% higher return)** while ensuring $5,000 matured and became fully accessible every quarter.

---

## Frequently Asked Questions (FAQ)

### What happens if I break a CD early before maturity?
If you withdraw funds from a standard CD before its maturity date, the bank will assess an **Early Withdrawal Penalty**. This penalty typically equals 90 days to 180 days of simple interest. Your original principal is almost always protected; the penalty merely reduces your accrued interest earnings.

### Are CDs safer than High-Yield Savings Accounts?
Both are equally safe. When opened at FDIC-insured banks or NCUA-insured credit unions, both CDs and High-Yield Savings Accounts carry **up to $250,000 in federal deposit insurance per depositor, per insured institution, per ownership category**.

---

*This article is for general educational purposes only and is not personalized banking or financial advice.*
""", encoding="utf-8")

(ARTICLES / "how-401k-employer-match-works.md").write_text("""---
title: "How 401(k) Employer Match Works: Matching Formulas, Vesting Schedules, and Free Money"
description: "Master employer 401(k) matching mechanics. Learn dollar-for-dollar matches, 50% partial matches, cliff vs graded vesting schedules, and contribution limit rules."
slug: "how-401k-employer-match-works"
keyword: "how 401k employer match works vesting schedules"
date: "2026-08-19"
category: "Investing"
---

# How 401(k) Employer Match Works: Formulas, Vesting Schedules, and Maximizing Your Benefit

An **employer 401(k) match** is an employer-sponsored benefit where your company contributes additional money directly into your retirement account based on the salary percentage you contribute.

Financial planners universally describe an employer 401(k) match as **the closest thing to "free money" in personal finance**. Failing to contribute enough to capture your full employer match is equivalent to turning down a guaranteed pay raise.

---

## The 3 Most Common Employer Match Formulas

Employers structure their matching formulas in several standard ways:

```
┌──────────────────────────────┬──────────────────────────────┬──────────────────────────────┐
│  1. DOLLAR-FOR-DOLLAR MATCH  │   2. 50% PARTIAL MATCH       │   3. TIERED / HYBRID MATCH   │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ "100% match up to 4% salary" │ "50% match up to 6% salary"  │ "100% on first 3%, plus      │
│                              │                              │  50% on next 2%"             │
│ • You contribute: 4%         │ • You contribute: 6%         │ • You contribute: 5%         │
│ • Employer adds: **4%**      │ • Employer adds: **3%**      │ • Employer adds: **4%**      │
│ • **Instant Return: +100%**  │ • **Instant Return: +50%**   │ • **Instant Return: +80%**   │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
```

### Worked Example: The $80,000 Salary Scenario
Suppose your annual salary is **$80,000** and your company offers a **50% match on up to 6% of your salary**:

1. **Your Contribution (6%):** $\$80,000 \times 6\% = \mathbf{\$4,800 \text{ / year}}$ ($400/month).
2. **Company Match (50% of your 6% = 3%):** $\$80,000 \times 3\% = \mathbf{\$2,400 \text{ / year}}$ ($200/month).
3. **Total Annual Capital Invested:** **$7,200 / year**.

---

## Vesting Schedules: How Long Until the Money Is Truly Yours?

While **100% of your own payroll contributions are always immediately yours (100% vested)**, the money contributed by your employer may be subject to a **Vesting Schedule**:

```
┌────────────────────────────────────────┬────────────────────────────────────────┐
│             CLIFF VESTING              │             GRADED VESTING             │
├────────────────────────────────────────┼────────────────────────────────────────┤
│ You own **0%** of the employer match   │ You gain ownership of the match        │
│ until you complete a specific period   │ gradually over several years.          │
│ (e.g., 3 years).                       │                                        │
│ • Leave at 2 years: Keep $0 match.     │ • Year 1: 20% vested                   │
│ • Leave at 3 years: Keep 100% match.   │ • Year 2: 40% vested (Year 5: 100%)    │
└────────────────────────────────────────┴────────────────────────────────────────┘
```

---

## Frequently Asked Questions (FAQ)

### What should I prioritize first: 401(k) match or paying off credit card debt?
**Always capture the 401(k) match first.** A 50% or 100% instant match return mathematically beats even a 25% credit card interest rate. Contribute just enough to get the full match, then aggressively direct all remaining cash flow toward paying off high-interest debt.

### What happens to my 401(k) match if I am laid off?
Under federal ERISA guidelines, if a company initiates a mass layoff or downsizes more than 20% of its workforce, employees are frequently granted **100% accelerated immediate vesting** of their employer match balances.

---

*This article is for general educational purposes only and is not personalized retirement advice.*
""", encoding="utf-8")

(ARTICLES / "term-life-vs-whole-life-insurance.md").write_text("""---
title: "Term Life vs Whole Life Insurance: Pure Protection vs Cash Value Investing Explained"
description: "Compare Term Life vs Whole Life insurance. Learn cost differences (10x-15x premium gap), cash value surrender fees, and the 'Buy Term and Invest the Difference' strategy."
slug: "term-life-vs-whole-life-insurance"
keyword: "term life vs whole life insurance cash value cost"
date: "2026-08-19"
category: "Budgeting & Debt"
---

# Term Life vs. Whole Life Insurance: Why "Buy Term and Invest the Difference" Dominates

Life insurance serves one primary economic purpose: **to replace your income and protect your financial dependents if you pass away prematurely**.

When shopping for coverage, consumers are faced with two fundamentally different product categories:

* **Term Life Insurance:** Pure, straightforward insurance protection that covers you for a specific period (e.g., 20 or 30 years). If you pass away during the term, your beneficiaries receive a tax-free cash death benefit. If you outlive the term, the policy simply expires.
* **Whole Life Insurance (Permanent):** A complex financial product that combines permanent death benefit protection with an internal "cash value" savings/investment account.

---

## Head-to-Head Comparison: Term vs. Whole Life

| Parameter | Term Life Insurance | Whole Life Insurance |
| :--- | :--- | :--- |
| **Duration of Coverage** | Fixed period (10, 20, 25, or 30 years) | **Permanent (Your entire life / until age 100+)** |
| **Monthly Premium Cost** | **Extremely affordable ($25 – $50 / month)** | **Extremely expensive ($350 – $600+ / month)** |
| **Cash Value Component** | **No** (Pure insurance protection) | **Yes** (Bundled internal cash value account) |
| **Investment Returns** | N/A | Historically low (~1.5% – 3.5% net after fees) |
| **Surrender Penalties** | None (Cancel anytime with $0 penalty) | **Hefty surrender charges** during the first 5–10 years |

---

## The Math Behind "Buy Term and Invest the Difference" (BTID)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    30-YEAR WORKED COMPARISON: $500,000 COVERAGE             │
│                        (30-Year-Old Healthy Non-Smoker)                     │
├────────────────────────────────────────┬────────────────────────────────────┤
│           WHOLE LIFE POLICY            │    BUY TERM & INVEST DIFFERENCE    │
├────────────────────────────────────────┼────────────────────────────────────┤
│ • Monthly Premium: **$450 / month**    │ • Term Premium: **$40 / month**    │
│ • Guaranteed Cash Value after 30 Yrs:  │ • Invests: **$410 / month @ 8%**   │
│   **~$260,000 - $310,000**             │ • Portfolio Value after 30 Yrs:    │
│                                        │   **~$610,000 in Liquid Wealth!**  │
└────────────────────────────────────────┴────────────────────────────────────┘
```

---

## Frequently Asked Questions (FAQ)

### How much life insurance coverage do I need?
A standard rule of thumb is **10x to 12x your annual gross salary** in term life coverage. For example, if you earn $80,000 per year, aim for an $800,000 to $1,000,000 20-or-30-year level term policy to replace your income and clear the mortgage.

---

*This article is for general educational purposes only and is not personalized insurance advice.*
""", encoding="utf-8")

(ARTICLES / "how-to-calculate-debt-to-income-ratio.md").write_text("""---
title: "How to Calculate Debt-to-Income (DTI) Ratio: Front-End vs Back-End Mortgage Limits"
description: "Learn how lenders calculate your Debt-to-Income (DTI) ratio. Master front-end vs back-end DTI, Fannie Mae limits, and step-by-step strategies to lower your ratio."
slug: "how-to-calculate-debt-to-income-ratio"
keyword: "how to calculate debt to income ratio dti front end back end"
date: "2026-08-19"
category: "Budgeting & Debt"
---

# How to Calculate Debt-to-Income (DTI) Ratio: The Key Metric Mortgage Lenders Use

When applying for a mortgage, auto loan, or major refinancing package, your credit score is only half the equation. The single most important mathematical metric underwriting teams use to determine your borrowing limit is your **Debt-to-Income (DTI) Ratio**.

Your DTI ratio measures the percentage of your **gross monthly income** that goes toward paying required recurring monthly debt obligations.

---

## Front-End DTI vs. Back-End DTI Explained

```
┌────────────────────────────────────────┬────────────────────────────────────────┐
│           FRONT-END DTI (HOUSING)      │           BACK-END DTI (TOTAL DEBT)    │
├────────────────────────────────────────┼────────────────────────────────────────┤
│ Measures **ONLY** housing expenses:    │ Measures **ALL** monthly debt payments │
│ • Mortgage Principal & Interest        │ combined:                              │
│ • Property Taxes                       │ • Total Housing (Front-End DTI)        │
│ • Homeowners Insurance                 │ • Minimum Credit Card Payments         │
│ • HOA / Condo Fees                     │ • Auto Loan Payments & Student Loans   │
│                                        │ • Personal Loans & Child Support       │
│ **Target Limit:** **28% or lower**     │ **Target Limit:** **36% to 43% max**   │
└────────────────────────────────────────┴────────────────────────────────────────┘
```

---

## Frequently Asked Questions (FAQ)

### Does DTI affect my credit score?
No. Your Debt-to-Income ratio is not reported to credit bureaus (Equifax, Experian, TransUnion) and does not directly impact your FICO credit score. However, credit bureaus do track your **Credit Utilization Ratio** (revolving balances divided by credit limits), which heavily impacts your score.

---

*This article is for general educational purposes only and is not personalized lending advice.*
""", encoding="utf-8")

(ARTICLES / "target-date-funds-explained.md").write_text("""---
title: "Target-Date Funds Explained: Glide Paths, Internal Fees, and 'To vs Through' Strategies"
description: "Master Target-Date Funds (TDFs) for retirement investing. Learn how glide paths shift from stocks to bonds, evaluate internal expense ratios, and compare TDFs vs 3-fund portfolios."
slug: "target-date-funds-explained"
keyword: "target date funds explained glide path fees 401k"
date: "2026-08-19"
category: "Investing"
---

# Target-Date Funds (TDFs) Explained: How All-in-One Retirement Funds Work

A **Target-Date Fund (TDF)**—often labeled as a *Target Retirement Fund* or *Lifecycle Fund*—is an all-in-one mutual fund designed to be a complete, self-contained investment portfolio tailored to an investor's expected retirement year.

When you invest in a Target-Date Fund (e.g., *Vanguard Target Retirement 2060 Fund*), the fund manager automatically allocates your money across a globally diversified mix of US stocks, international stocks, US bonds, and international bonds.

---

## How the Target-Date Glide Path Works

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE LIFECYCLE TARGET-DATE GLIDE PATH                     │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│  EARLY CAREER (AGE 25)   │   MID CAREER (AGE 45)    │ AT RETIREMENT (AGE 65)│
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ • 90% Equities (Stocks)  │ • 70% Equities (Stocks)  │ • 50% Equities (Stocks│
│ • 10% Bonds & Cash       │ • 30% Bonds & Cash       │ • 50% Bonds & Cash    │
│ • Focus: Maximum Growth  │ • Focus: Growth & Safety │ • Focus: Capital Pres.│
└──────────────────────────┴──────────────────────────┴───────────────────────┘
```

---

## Frequently Asked Questions (FAQ)

### How do I choose the right Target-Date Fund year?
Select the fund whose year is closest to the year you turn **age 65** (or your planned retirement age). For example, if you were born in 1995, you will turn 65 in the year 2060, making a **Target 2060 Fund** your natural default.

---

*This article is for general educational purposes only and is not personalized investment advice.*
""", encoding="utf-8")

print("[generator] All 18 pillar articles generated successfully.")
