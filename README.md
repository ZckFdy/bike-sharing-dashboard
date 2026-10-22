# Proyek Analisis Data: Bike Sharing

## Deskripsi
Proyek ini menganalisis data penyewaan sepeda selama tahun 2011–2012 menggunakan Bike Sharing Dataset. Analisis dilakukan untuk memahami perbedaan jumlah penyewaan berdasarkan jenis hari dan kondisi cuaca.

## Pertanyaan Bisnis
1. Bagaimana perbedaan jumlah penyewaan sepeda antara hari kerja dan hari bukan kerja selama tahun 2011–2012?
2. Bagaimana perbedaan jumlah penyewaan sepeda berdasarkan kondisi cuaca selama tahun 2011–2012?

## Dataset
Dataset yang digunakan adalah Bike Sharing Dataset, khususnya file `day.csv`.

Dataset berisi informasi tanggal, kondisi cuaca, jenis hari, serta jumlah penyewaan sepeda.

## Proses Analisis
1. Mengumpulkan dan memuat dataset.
2. Memeriksa tipe data, nilai kosong, dan duplikasi.
3. Membersihkan data dan mengubah kolom tanggal ke format datetime.
4. Melakukan Exploratory Data Analysis (EDA).
5. Membuat visualisasi untuk menjawab pertanyaan bisnis.
6. Menyusun kesimpulan dan rekomendasi.

## Hasil Analisis
- Rata-rata penyewaan pada hari kerja lebih tinggi daripada hari bukan kerja.
- Rata-rata penyewaan tertinggi ditemukan pada kondisi cuaca cerah atau sedikit berawan.
- Rata-rata penyewaan lebih rendah pada kondisi hujan ringan atau cuaca buruk.

## Dashboard
Dashboard interaktif dibuat menggunakan Streamlit untuk menampilkan ringkasan data, filter tahun, grafik, dan hasil analisis.

## Cara Menjalankan Dashboard
1. Instal dependensi:

   `pip install -r requirements.txt`

2. Masuk ke folder dashboard:

   `cd dashboard`

3. Jalankan dashboard:

   `streamlit run dashboard.py`

## Struktur Folder
- `dashboard/`: kode dashboard dan dataset untuk dashboard.
- `data/`: dataset yang digunakan dalam proyek.
- `notebook.ipynb`: notebook analisis data.
- `requirements.txt`: daftar dependensi.
- `url.txt`: tautan yang diperlukan untuk submission.

## Sumber Dataset
Bike Sharing Dataset - UCI Machine Learning Repository:
https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view