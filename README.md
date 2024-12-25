# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data peminjaman sepeda dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset). Data ini mencakup informasi tentang cuaca, musim, hari libur, dan sebagainya. Analisis ini dilakukan untuk menjawab beberapa pertanyaan bisnis terkait dengan faktor-faktor yang mempengaruhi jumlah peminjaman sepeda.

## Pertanyaan Bisnis
1. Bagaimana pengaruh hari kerja dan hari libur terhadap jumlah peminjaman sepeda?
2. Bagaimana pengaruh pengguna sepeda berlangganan dan tidak berlangganan terhadap jumlah peminjaman sepeda?
3. Bagaimana pengaruh cuaca terhadap jumlah peminjaman sepeda?
4. Bagaimana pengaruh musim terhadap jumlah peminjaman sepeda?
5. Bagaimana distribusi jumlah peminjaman sepeda pada tahun 2011 dan 2012?

## Library yang Digunakan
- Pandas
- Seaborn
- Datetime
- Matplotlib

## Insight Utama
- Jumlah peminjaman sepeda lebih tinggi pada hari kerja dibandingkan dengan hari libur.
- Pengguna sepeda yang berlangganan memiliki jumlah peminjaman sepeda yang lebih tinggi dibandingkan dengan pengguna sepeda yang tidak berlangganan.
- Kondisi cuaca cerah memiliki jumlah peminjaman sepeda yang lebih tinggi dibandingkan dengan kondisi cuaca berawan, salju, dan hujan.
- Musim panas memiliki jumlah peminjaman sepeda yang lebih tinggi dibandingkan dengan musim semi, musim gugur, dan musim dingin.
- Jumlah peminjaman sepeda pada tahun 2012 lebih tinggi dibandingkan dengan tahun 2011.

## RFM Analysis
RFM Analysis digunakan untuk mengelompokkan pelanggan berdasarkan tiga faktor:
- **Recency (R):** Seberapa baru pelanggan melakukan pembelian.
- **Frequency (F):** Seberapa sering pelanggan melakukan pembelian.
- **Monetary (M):** Seberapa besar total pembelian yang dilakukan oleh pelanggan.

Segmentasi pelanggan berdasarkan RFM Score:
- **Hibernating:** Pelanggan yang tidak aktif dalam melakukan pembelian.
- **At Risk:** Pelanggan yang memiliki potensi untuk meninggalkan bisnis.
- **Can't Lose:** Pelanggan yang memiliki nilai pembelian tinggi dan sering melakukan pembelian.
- **About to Sleep:** Pelanggan yang memiliki nilai pembelian tinggi tetapi jarang melakukan pembelian.
- **Need Attention:** Pelanggan yang sering melakukan pembelian tetapi memiliki nilai pembelian rendah.
- **Loyal Customers:** Pelanggan yang memiliki nilai pembelian tinggi dan sering melakukan pembelian.
- **Promising:** Pelanggan yang memiliki potensi untuk menjadi pelanggan loyal.
- **New Customers:** Pelanggan baru yang perlu mendapatkan perhatian lebih.
- **Potential Loyalists:** Pelanggan yang memiliki potensi untuk menjadi pelanggan loyal.
- **Champions:** Pelanggan yang memiliki nilai pembelian tinggi dan sering melakukan pembelian.

## Cara Menjalankan Proyek

### Instalasi Dependencies
Untuk menginstal dependencies yang diperlukan, jalankan perintah berikut:
```bash
pip install -r requirements.txt
```

### Menjalankan Dashboard
Untuk menjalankan dashboard menggunakan Streamlit, jalankan perintah berikut:
```bash
streamlit run dashboard.py
```

## Struktur Direktori
```
┌── dashboard
│   ├── dashboard.py
│   └── hour.csv
├── data
│   ├── day.csv
│   ├── hour.csv
│   └── Readme.txt
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Kontak
- **Nama:** Bima Rakajati
- **Email:** bimandugal@gmail.com
- **ID Dicoding:** [bimarakajati](https://www.dicoding.com/users/bimarakajati/academies)