# Proyek Peramalan Beban Listrik Jangka Pendek

Proyek ini adalah implementasi model _deep learning_ untuk peramalan beban listrik jangka pendek di Jawa Timur. Model Hybrid LSTM-ANN yang telah dilatih dan dievaluasi dengan akurasi tinggi ini di-deploy sebagai sebuah REST API menggunakan FastAPI dan dikemas dengan Docker untuk kemudahan penggunaan dan portabilitas.

Tujuan utamanya adalah menyediakan alat bantu untuk menyeimbangkan pasokan dan permintaan listrik, mengurangi risiko pemadaman, dan mencegah pemborosan energi.

---

## Fitur Utama

- **Peramalan Akurat**: Memprediksi beban listrik untuk **24 jam ke depan** (48 data point setiap 30 menit).
- **Model Unggul**: Menggunakan arsitektur **Hybrid LSTM-ANN** yang terbukti konsisten mengungguli model tunggal dengan **MAPE di bawah 3%**.
- **API Siap Pakai**: Disediakan dalam bentuk REST API untuk kemudahan integrasi dengan sistem lain.
- **Portabel**: Dikemas menggunakan **Docker**, memastikan aplikasi berjalan konsisten di lingkungan mana pun.

---

## Teknologi yang Digunakan

- **Backend**: Python, FastAPI
- **Machine Learning**: TensorFlow (Keras), Scikit-learn, Pandas, NumPy
- **Deployment**: Docker
- **Kontrol Versi**: Git, GitHub

---

## Prasyarat

Sebelum memulai, pastikan perangkat Anda telah terinstal:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/products/docker-desktop/)

---

## Instalasi dan Setup

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di `localhost` Anda.

**1. Clone Repositori**
Buka terminal atau command prompt dan jalankan perintah berikut untuk mengunduh proyek:

```bash
git clone https://github.com/f2rra/stlf-plnjatim.git
```

**2. Masuk ke Direktori Proyek**

```bash
cd stlf-plnjatim
```

**3. Tarik (Pull) Image dari Docker Hub**
Perintah ini akan menarik image dari Docker Hub yang berisi semua dependensi dan kode aplikasi. Proses ini mungkin memakan waktu beberapa menit saat pertama kali dijalankan.

```bash
docker pull f2rra/stlf-plnjatim-api:latest
```

**4. Jalankan Kontainer Docker**
Setelah _image_ berhasil dipull, jalankan sebagai _container_. Aplikasi API akan berjalan di port `8000`.

```bash
docker run -p 8000:8000 stlf-plnjatim-api
```

**5. Verifikasi Instalasi**
Buka browser dan kunjungi `http://localhost:8000`. Jika Anda melihat pesan sambutan `{"message":"Selamat datang di API Peramalan Beban Listrik"}`, maka API Anda telah berhasil berjalan\! ✅

---

## Cara Penggunaan

Setelah API berjalan, Anda bisa mulai melakukan peramalan.

### 1\. Menggunakan Dokumentasi Interaktif (Swagger UI)

Cara termudah untuk mencoba API adalah melalui dokumentasi interaktif yang dibuat secara otomatis.

1.  **Buka Browser**: Kunjungi alamat `http://localhost:8000/docs`.

2.  **Pilih Endpoint**: Klik pada endpoint `POST /predict` untuk melihat detailnya.

3.  **Coba Langsung**: Klik tombol **"Try it out"**.

4.  **Masukkan Data**: Salin dan tempel data input dalam format JSON ke dalam _Request body_. Data harus berisi _key_ `"historical_load"` dengan _value_ berupa _list_ yang berisi **48 data point** (float).

    _Contoh Input:_

    ```json
    {
      "historical_load": [
        4541.68, 4483.65, 4427.15, 4411.21, 4344.98, 4315.7, 4307.25, 4323.4,
        4358.35, 4420.4, 4510.8, 4650.1, 4805.5, 4950.2, 5100.7, 5250.3, 5400.1,
        5550.9, 5700.6, 5850.2, 6000.0, 5950.5, 5800.8, 5650.4, 5500.0, 5350.7,
        5200.3, 5050.9, 4900.1, 4925.6, 4950.2, 4980.5, 5010.8, 5050.4, 5100.2,
        5150.7, 5200.9, 5250.1, 5300.6, 5350.3, 5400.7, 5450.2, 5500.8, 5480.1,
        5460.5, 5440.9, 5420.3, 5400.0
      ]
    }
    ```

5.  **Eksekusi**: Klik tombol **"Execute"**. Hasil peramalan untuk 24 jam ke depan akan muncul di bagian _Server response_.

### 2\. Menggunakan cURL

Untuk pengujian cepat melalui terminal, gunakan perintah `curl` berikut:

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "historical_load": [
    4541.68, 4483.65, 4427.15, 4411.21, 4344.98, 4315.7, 4307.25, 4323.4,
    4358.35, 4420.4, 4510.8, 4650.1, 4805.5, 4950.2, 5100.7, 5250.3,
    5400.1, 5550.9, 5700.6, 5850.2, 6000.0, 5950.5, 5800.8, 5650.4,
    5500.0, 5350.7, 5200.3, 5050.9, 4900.1, 4925.6, 4950.2, 4980.5,
    5010.8, 5050.4, 5100.2, 5150.7, 5200.9, 5250.1, 5300.6, 5350.3,
    5400.7, 5450.2, 5500.8, 5480.1, 5460.5, 5440.9, 5420.3, 5400.0
  ]
}'
```
