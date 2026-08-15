---
title: "Screener Saham IDX: Cara Menyaring Saham Indonesia Berdasarkan Angka"
description: "Screener saham IDX gratis yang memberi peringkat saham-saham Bursa Efek Indonesia berdasarkan ROE, valuasi, pertumbuhan, utang, dan dividen â€â€— beserta penjelasan metodologi dan keterbatasannya."
slug: "screener-saham-idx"
keyword: "screener saham idx"
lang: "id"
translation_of: "idx-stock-screener"
calculator: "screener"
date: "2026-08-14"
path: "id/screener-saham-idx"
---

# Screener Saham IDX: Cara Menyaring Saham Indonesia Berdasarkan Angka

Screener di atas memindai pasar saham Indonesia (IDX) dan memberi peringkat sekitar 55 saham likuid berkapitalisasi besar dan menengah berdasarkan fundamental yang paling penting bagi investor jangka panjang: profitabilitas, valuasi, pertumbuhan, leverage, dan dividen. Angka dari laporan tahunan dan harga penutupan terbaru diubah menjadi satu daftar yang bisa dibandingkan, sehingga waktu Anda dipakai untuk membaca laporan tahunan, bukan membuat spreadsheet.

Panduan ini menjelaskan arti setiap metrik, bagaimana skor disusun, dan â€â€— sama pentingnya â€â€— apa yang tidak bisa dikatakan oleh screener.

## Apa yang diukur oleh screener

Setiap saham mendapat skor 0 sampai 100 dari enam komponen:

| Metrik | Bobot | Apa yang diukur |
|---|---|---|
| Return on equity (ROE) | 20% | Seberapa menguntungkan manajemen memakai uang pemegang saham |
| Valuasi (P/BV) | 20% | Berapa yang Anda bayar per rupiah nilai buku |
| Leverage (D/E) | 15% | Seberapa besar utang perusahaan dibandingkan ekuitas |
| Pertumbuhan laba | 15% | Apakah laba tumbuh atau menyusut |
| Imbal hasil dividen | 15% | Berapa yang dibayarkan perusahaan kembali ke pemegang saham |
| Kapitalisasi pasar | 15% | Ukuran perusahaan dan likuiditasnya |

Bobot tersebut adalah pilihan editorial kami, bukan kebenaran objektif. Bobot ini menyukai bisnis yang menguntungkan, bernilai wajar, berutang rendah, dan membayar dividen â€â€— titik awal yang masuk akal untuk investasi jangka panjang di saham unggulan Indonesia, tetapi Anda boleh menimbangnya dengan cara berbeda.

### Return on equity (ROE)

ROE adalah laba bersih dibagi ekuitas pemegang saham: berapa rupiah laba yang dihasilkan setiap rupiah modal pemilik per tahun. ROE konsisten di atas 15% adalah batas yang wajar untuk bisnis berkualitas. Bank secara alami melaporkan ROE tinggi dengan ekuitas tipis â€â€— sebab itulah filter leverage pada screener cenderung mengeluarkan bank (lihat keterbatasan di bawah).

### Price-to-book value (P/BV)

P/BV membandingkan harga pasar dengan nilai aset bersih perusahaan per saham. P/BV di bawah 1 berarti Anda bisa membeli bisnis lebih murah dari nilai bukunya; di atas 2â€â€œ3, pasar sudah memperhitungkan ekspektasi pertumbuhan. Metrik ini paling bermakna untuk bisnis padat aset (bank, properti, tambang) dan kurang berguna untuk bisnis yang asetnya ringan.

### Debt-to-equity (D/E)

D/E membandingkan total kewajiban dengan ekuitas pemegang saham â€â€— seberapa besar bisnis dibiayai utang dibandingkan modal pemilik. Semakin rendah umumnya semakin aman, tetapi beberapa sektor (bank, utilitas, pengembang properti) memang terstruktur dengan leverage tinggi. D/E di bawah 1 adalah saringan konservatif yang dengan sengaja mengeluarkan sebagian besar perusahaan keuangan.

### Pertumbuhan laba

Pertumbuhan membandingkan laba bersih tahunan terakhir dengan tahun sebelumnya. Disajikan dalam persen dan bisa negatif. Pertumbuhan satu tahun saja berisik â€â€— tahun yang bagus atau keuntungan sekali waktu bisa menyanjung angka tersebut, jadi perlakukan sebagai satu masukan, bukan vonis.

### Imbal hasil dividen

Imbal hasil adalah dividen per saham tahunan dibagi harga saham. Bank dan konglomerat Indonesia sering membayar dividen yang tinggi dan konsisten, karena itu mereka mendominasi kolom dividen di screener. Imbal hasil tinggi juga bisa menandakan harga saham yang turun, jadi dibaca bersama ROE dan D/E.

## Cara kerja filter

Keenam kotak filter memetakan ke angka yang sama di atas. Mulailah dari nilai bawaan, lalu persempit:

- **Kapitalisasi pasar minimum** â€â€— pertahankan di atas Rp 10 triliun demi likuiditas; kapitalisasi lebih kecil lebih berisiko dan lebih sulit dijual.
- **ROE minimum** â€â€— naikkan ke 20 untuk mengisolasi nama paling menguntungkan.
- **P/BV maksimum** â€â€— turunkan ke 1,5 untuk berburu nilai; sebagian besar saham berkualitas akan gugur.
- **Pertumbuhan minimum** â€â€— 5â€â€œ10% menjaga daftar berisi saham bertumbuh; atur ke 0 atau di bawahnya untuk menyertakan saham pemulihan.
- **Imbal hasil minimum** â€â€— 3%+ memilih pembayar dividen; 0 mempertahankan semua.
- **D/E maksimum** â€â€— 1 menjaga daftar konservatif; bank hanya muncul pada nilai yang lebih tinggi.

Kombinasi paling ketat (kapitalisasi pasar â‰¥ Rp 10 T, ROE â‰¥ 15%, P/BV â‰¤ 2, pertumbuhan â‰¥ 5%, imbal hasil â‰¥ 3%, D/E â‰¤ 1) memang sengaja dibuat menuntut â€â€— biasanya hanya segelintir saham Indonesia yang lolos keenam filter sekaligus. Itulah gunanya: saringan yang mengembalikan 50 saham adalah katalog, bukan penyaring.

## Apa yang tidak bisa dikatakan oleh screener

Menyaring dengan angka punya batas yang tegas:

- **Itu potret, bukan cerita.** Skor mengurutkan laporan tahunan *terbaru* terhadap harga *terbaru*. Screener tidak bisa melihat parit kompetitif perusahaan, kualitas manajemen, atau perubahan regulasi tahun depan.
- **Bank sebagian besar tidak terlihat.** Karena filter leverage, perusahaan keuangan jarang muncul â€â€— padahal bank adalah sektor paling menguntungkan di Indonesia. Jika ingin menyaring bank, naikkan D/E maksimum; metrik lain tetap mengurutkannya.
- **Data punya tanggal.** Fundamental berasal dari laporan tahunan teraudit (2022â€â€œ2025) dan harga dari penutupan pasar terbaru â€â€— baris "data per" di screener menunjukkan kapan persisnya. Di antara musim pelaporan, angka menjadi usang.
- **Tidak ada informasi ke depan.** Tidak ada perkiraan laba, target harga, atau rekomendasi di sini. Ini peringkat masa lalu dan masa kini.

## Cara menggunakannya dengan bijak

1. **Jalankan screener, lalu buka laporan tahunan** beberapa nama teratas. Angka di balik layar ini berasal dari laporan tersebut â€â€— verifikasi, dan baca diskusi manajemennya.
2. **Bandingkan sektor, bukan hanya skor.** Skor teratas di properti bukan risiko yang sama dengan skor teratas di tambang. Kolom sektor menjaga Anda tetap jujur.
3. **Periksa baris rezim pasar.** Bilah pasar menunjukkan apakah IHSG diperdagangkan di atas atau di bawah rata-rata 60 harinya dan berapa banyak saham yang naik versus turun dalam 5 hari. Arti saringan berubah di pasar yang jatuh â€â€— nama ber-leverage berlebihan yang tampak murah bisa tetap murah.
4. **Jangan pernah membeli hanya karena saringan.** Gunakan ini sebagai filter pertama, lalu terapkan analisis valuasi, kualitas, dan risiko yang spesifik untuk bisnis tersebut.

## Penelusuran terkait

- [Apa Itu THR dan Bagaimana Cara Menghitungnya](id/apa-itu-thr-dan-cara-menghitungnya.html) â€â€— uang masuk yang teratur
- [Kalkulator dana darurat](../calculators/emergency-fund.html) â€â€— bangun cadangan yang membuat Anda mampu bertahan saat pasar turun
- [Cara kerja bunga majemuk](../calculators/compound-interest.html) â€â€— mengapa berpegang jangka panjang lebih penting daripada satu pilihan apa pun
- [Disclaimer](disclaimer.html) â€â€— apa yang dijamin dan tidak dijamin oleh alat situs ini

---

*Screener ini hanya untuk tujuan edukasi umum dan bukan nasihat investasi yang dipersonalisasi. Skor adalah peringkat transparan dari fundamental yang dipublikasikan, bukan rekomendasi untuk membeli, menjual, atau menahan sekuritas apa pun. Verifikasi data terhadap laporan resmi perusahaan sebelum bertindak.*
