# DRAFT BRIEF — news-image-20261121

**Dibuat:** Sabtu 21 November 2026, ~12:00 WIB (05:00 UTC)
**Kompetisi:** `news-image-20261121` — satu gambar merangkum berita dunia
Sabtu 21 November 2026. Hadiah total $100 USDC ($20/$12/$6, 4–10 $2,
11–50 $1,20). **Deadline entri: 22 Nov 2026 07:00 WIB.**
**Status: DRAF — JANGAN submit hari ini.** Refresh + submit besok pagi
sebelum 07:00 WIB, sesudah hari 21 Nov berakhir di semua zona waktu.

**G0 (oleh induk):** HIJAU — rubrik dibaca verbatim; kuota TERBUKA
(entries made 0, can submit YES, 3 left today, hard limit 20/20).
Repo: https://github.com/jihoonbaee/news-image-20261121 (publik, kosong).

---

## ⚠️ PERINGATAN REFRESH — BACA DULU SEBELUM SUBMIT

**Gambar ini adalah DRAF / early edition.** Hari berita 21 November 2026
baru berjalan ~5 jam (05:00 UTC) saat draf dibuat. Gambar ini hanya
memuat berita yang sudah terverifikasi sampai pukul 05:00 UTC.

**SEBELUM SUBMIT, gambar WAJIB di-refresh** besok pagi (22 Nov, sesudah
21 Nov berakhir di semua zona waktu), agar memuat cerita-cerita besar
yang terjadi di sisa hari itu — kalau tidak, entri akan kalah dari entri
yang memakai hari penuh.

**Cara refresh (~15–30 menit):**
1. Riset lagi berita 21 Nov 2026 yang terjadi/dilaporkan sesudah 05:00 UTC
   (lihat daftar "Masih berkembang" di bawah — itu prioritas refresh).
2. Edit daftar `STORIES` (dan `ALSO_TODAY`) di `render.py` — jaga headline
   ≤ 2 baris di panel grid (cek otomatis di skrip), sub-teks ≤ 2 baris.
   Headline band (NATO) harus 1 baris.
3. Jalankan `python3 render.py`, lalu periksa `entry.png` secara visual.
4. Jalankan verifikasi determinisme (dua run `node main.ts`,
   bandingkan sha256).
5. Perbarui laporan draf dengan cerita + sumber yang baru, dan hapus
   peringatan ini bila gambar sudah memakai hari penuh.

Catatan kaki di gambar ("Draft edition — covers the day so far; refresh
after 21 November ends") harus dihapus/diubah saat refresh — ganti `note`
di `render.py`. Juga ubah `sub_line` ("as reported by 05:00 UTC") sesuai
jam refresh.

---

## Daftar cerita (draf, per 05:00 UTC 21 Nov 2026)

Semua klaim terverifikasi dari ≥2 sumber independen (lihat tabel sumber).
Tanggal peristiwa dicek eksplisit — tiga jebakan tanggal tertangkap dan
DIBUANG (lihat "Sengaja TIDAK dipakai").

| # | Panel | Cerita | Verifikasi |
|---|-------|--------|------------|
| 1 | LEAD — Middle East / Conflict | Koalisi pimpinan Saudi mencegat + menghancurkan 3 rudal balistik Houthi yang ditembakkan ke Riyadh; serangan ke-2 ke ibu kota dalam beberapa hari sesudah PIF Tower diserang Kamis 19 Nov | Reuters dateline 21 Nov; oneturn.news (Day 6 of 6); Middle East Eye / Straits Times / The National |
| 2 | South America / Disaster | Gempa M6,8 mengguncang Peru tengah (~30 km barat laut Junín), terasa di Lima; belum ada laporan korban/kerusakan besar | IGP/CENSIS RS 2026-0818 (M6,7, 00:09 UTC 21 Nov); USGS/GFZ/Reuters M6,8 |
| 3 | Global / Climate | COP31 di Belém berjalan melewati tenggat tanpa kesepakatan; sidang pleno penutup ditunda ke Sabtu pagi; draf revisi Kamis menghapus SEMUA sebutan bahan bakar fosil | Carbon Brief; draf Kamis 9 halaman, 144→80 paragraf; draf ke-3 dijanjikan Sabtu pagi |
| 4 | Sport / Asia-Pacific | KL Rahul century (100 dari 207 bola) di Wellington — opener India PERTAMA dengan century Test di keempat negara SENA | Laporan Sabtu 21 Nov, Day 3 Test 1 vs NZ, Basin Reserve; century Test ke-13; batter India ke-5 keseluruhan; century Test India pertama di NZ sesudah 12 tahun (Rahane 118, Feb 2014) |
| 5 | Markets / US | Wall Street masuk koreksi: S&P 500 −3,70% ke 6.910,39; Nasdaq −5,28% ke 22.617,73, menghapus seluruh gain 2026; Nvidia −13,8% sesudah laporan SEC memeriksa praktik akuntansi | Penutupan Jumat 20 Nov (dilaporkan Sabtu pagi di zona Asia); konsensus multi-sumber; S&P −8,6% seminggu; Nasdaq −10,0% seminggu |
| 6 | Europe / Security (band) | Sekjen NATO Mark Rutte berkunjung ke Warsawa hari ini sesudah rudal Rusia mendarat di Polandia Jumat; Warsawa menyebutnya provokasi disengaja, minta pasukan Eastern Sentry tambahan | SOFX / Irish Times / political.org / Helsinki Times: "due in Warsaw on Nov. 21"; Tusk: "intentional provocation"; Kosiniak-Kamysz akan minta pasukan tambahan |
| — | ALSO TODAY | Banjir Florida meluas ke utara · Kualifikasi GP Las Vegas · Senat AS memberi penghormatan kepada Fiona si kuda nil | ABC Detroit (flood watch diperpanjang ke Sabtu); F1 final practice Sat 01:30 GMT, kualifikasi berlangsung; Washington Examiner 21 Nov (resolusi Senat bulat; Fiona mati Kamis sesudah menelan topi pengunjung) |

### Catatan kejujuran tanggal

- **Panel 5 (Wall Street):** penutupan terjadi Jumat 20 Nov sore waktu New
  York, TETAPI pertama kali dilaporkan pada Sabtu 21 Nov di zona waktu
  Asia (tutup 16:00 EST = 21 Nov 04:00 WIB / 06:00 JST). RULES mendefinisikan
  berita hari itu sebagai peristiwa yang "terjadi, ATAU pertama kali
  dilaporkan, pada 21 November 2026 di zona waktu mana pun" — panel ini
  lolos definisi itu lewat pelaporan Asia. Sub-teks tidak mengklaim hari
  apa penutupan terjadi. Edisi Sabtu yang tidak memuat koreksi pasar
  terbesar minggu ini akan terlihat tidak lengkap bagi juri.
- **Panel 6 (Rutte):** kunjungan terjadwal hari ini dan terkonfirmasi oleh
  ≥4 outlet; hasil kunjungan BELUM diketahui saat draf dibuat — panel
  hanya menyatakan kunjungan + posisi yang sudah dinyatakan Jumat
  (provokasi disengaja; permintaan pasukan tambahan). Refresh besok pagi
  mengganti dengan HASIL kunjungan bila ada yang substantif.
- **Panel 3 (COP31):** draf ke-3 dijanjikan Sabtu pagi (waktu Belém) dan
  BELUM keluar saat draf dibuat; panel menyatakan fakta yang sudah pasti
  (melewati tenggat, tanpa kesepakatan, draf Kamis menghapus bahan bakar
  fosil). Refresh besok pagi memakai hasil akhir (kesepakatan Sabtu/Minggu
  atau gagal).

---

## Sengaja TIDAK dipakai (jebakan tanggal / klaim tak terverifikasi)

1. **Splashdown SpaceX Crew-12** — BUKAN November: mendarat **8 Oktober
   2026** (SpaceX.com + NASA). Item "splashdown today" di agregator adalah
   publikasi ulang basi. DIBUANG.
2. **Serangan siber superkomputer Fugaku (RIKEN)** — BUKAN 21 Nov:
   pelanggaran 10–13 Nov, shutdown 14 Nov, pernyataan RIKEN 16 Nov,
   The Register 17 Nov. Item bertanggal "Sat 21 Nov 02:05 UTC" di agregator
   adalah publikasi ulang. DIBUANG.
3. **Myanmar menyebut putusan ICJ "unfair"** — Jumat **20 Nov** (Reuters
   08:45 UTC; konferensi pers Naypyitaw). Milik edisi 20261120. DIBUANG.
4. **Rekor FPI India ₹1,22 lakh crore** — dilaporkan Jumat **20 Nov**
   (BusinessLine; data 2–20 Nov). Milik edisi 20261120. DIBUANG.
5. **Vonis Nikhil Gupta 235 bulan** — Jumat **20 Nov** (DOJ; AP/Reuters).
   Milik edisi 20261120. DIBUANG.
6. **"Poland invokes Article 4"** — headline europesays MENGKLAIM, tapi
   isinya tidak mengonfirmasi invokasi formal; political.org: keputusan
   meminta konsultasi MASIH terbuka. DIBUANG sebagai klaim.
7. **"41 tewas termasuk 11 anak" di Yaman** — klaim Houthi TAK
   TERVERIFIKASI (Instagram brief; oneturn mengatribusikan ke Houthi).
   DIBUANG sebagai fakta.
8. **Rudal Rusia ke Polandia sebagai panel sendiri** — Jumat 20 Nov
   (~06:30 lokal; 2 rudal Kh-101 + 1 drone jet; tanpa korban). Milik edisi
   20261120. Edisi ini hanya memakai KELANJUTAN Sabtunya (kunjungan Rutte).
9. **Pendaratan Siklon Akvan, kesepakatan UK–EU, vonis Palisades Fire,
   pil kanker pankreas ERAS-0015, ancaman pajak Trump atas data center**
   — semuanya Jumat 20 Nov; milik edisi 20261120. DIBUANG.

---

## Masih berkembang (prioritas refresh besok pagi)

1. **Hasil kunjungan Rutte ke Warsawa** — apakah Polandia meminta konsultasi
   NATO (Article 4) formal? Apakah ada pengumuman pasukan Eastern Sentry
   tambahan? Apakah AS memberi pernyataan?
2. **Hasil akhir COP31** — kesepakatan tercapai Sabtu/Minggu, atau gagal?
   Apakah draf final memulihkan sebutan bahan bakar fosil / angka adaptasi
   $120 miliar/tahun?
3. **Konvoi tanker Iran di Kharg** — 14+ tanker berkumpul, BELUM berlayar
   per laporan 20 Nov. Bila berlayar Sabtu = cerita besar 21 Nov.
4. **Eskalasi Houthi–Saudi** — serangan lanjutan? Korban di Hodeidah
   (klaim "41 tewas" terverifikasi atau tidak)? Respons PBB?
5. **Update gempa Peru** — korban/kerusakan setelah penilaian siang hari;
   gempa susulan besar?
6. **Hasil olahraga Sabtu** — hasil kualifikasi GP Las Vegas; hasil Test
   India–NZ Day 3 (Rahul century sudah masuk; bila India menang/kalah
   besar, update sub-teks); Premier League.
7. **Cerita baru Sabtu siang/malam** (Gaza, Ukraina, AS) — gantikan panel
   yang paling lemah (kandidat pertama: band NATO bila kunjungan Rutte
   tidak menghasilkan apa-apa; kedua: ALSO Florida/Fiona).

---

## Baseline yang dikunci (sebelum render)

- Format: koran 6 panel (lead full-width + grid 2×2 + band) + footer ALSO,
  mengikuti pola 20261119/20261120 yang sudah terbukti lolos gate.
- Masthead: "THE WORLD IN ONE DAY"; tanggal "SATURDAY • 21 NOVEMBER 2026"
  besar merah; sub-line "Six stories that defined the day — as reported
  by 05:00 UTC".
- Headline maks ~34 karakter/baris, maks 2 baris (band: 1 baris);
  sub maks ~110 karakter, maks 2 baris. Semua teks DejaVu (PIL),
  terbaca pada ~300px.
- Ikon: piktogram datar orisinal per panel (rudal+perisai, seismograf,
  globe+daun, bat kriket, grafik jatuh, perisai NATO). TIDAK ada foto
  orang nyata, TIDAK ada artwork orang lain.
- Program entri: main.ts (Node 22 stdlib) hanya menyalin entry.png ke
  /output; render.py (Pillow) adalah alat build lokal, bukan bagian
  program grader.

## Pra-registrasi (dicatat SEBELUM render; dinilai sesudah skor server)

- **P1 (dev rate):** draf ini, bila disubmit apa adanya, diprediksi
  provisional rate **45–55%** (pembanding: 20261117 draf pagi 48,8%;
  20261118 refresh 95,04%). Draf pagi BUKAN final.
- **P2 (refresh):** sesudah refresh hari penuh besok pagi, rate diprediksi
  naik ke **90–97%** (pembanding: 20261119 refresh, prediksi 95–97%).
- **P3 (top-50):** TIDAK diprediksi — kesenjangan breadth struktural
  (6 panel vs 44–52 cerita di entri teratas) tetap berlaku.
- **P4 (gate):** 4/4 cek gate lolos pada submit pertama (file valid,
  ≤1 MiB, ≤1024×1024, deterministik).
- **Falsifier:** F1 — bila refresh TIDAK menaikkan rate di atas draf pagi,
  hipotesis "hari penuh > draf pagi" ditolak untuk edisi ini. F2 — bila
  ada panel yang terbukti salah tanggal/fakta oleh juri atau sumber,
  seleksi draf dinyatakan gagal dan dicatat di advice-log.

## Review DeepSeek

Review atas seleksi berita diminta SEBELUM render (lihat laporan draf).
DeepSeek berhak BLOCK klaim yang meragukan; klaim yang di-BLOCK
dihapus/diganti sebelum render.
