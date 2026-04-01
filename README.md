# 🚦 PRAKTIKUM 5

## Big Data Analytics & Use Case (Decision-Oriented System)

### 📍 Smart Transportation (Multi-Domain Pipeline)

---

## 📖 Deskripsi Project

Project ini merupakan implementasi sistem **Big Data Streaming** pada domain **Smart Transportation**, yang mensimulasikan aliran data kendaraan secara real-time untuk menghasilkan insight dan alert berbasis data.

---

## 🎯 Tujuan

* Memahami pipeline Big Data end-to-end
* Mengolah data streaming menggunakan Spark
* Menampilkan insight real-time melalui dashboard
* Menghasilkan alert berbasis kondisi tertentu

---

## ⚙️ Arsitektur Sistem

1. **Data Generator** → menghasilkan data kendaraan
2. **Streaming Layer (Spark)** → memproses data
3. **Serving Layer** → menyimpan hasil olahan
4. **Dashboard (Streamlit)** → visualisasi & alert

---

## 📂 Struktur Project

```bash
BIGDATA-PROJECT/
│
├── dashboard/
│   └── dashboard_streamlit.py
│
├── scripts/
│   ├── transaction_generator.py
│   └── streaming_layer.py
│
├── data/
├── logs/
├── stream_data/
└── README.md
```

---

## ▶️ Cara Menjalankan

### 1. Jalankan Generator

```bash
python scripts/transaction_generator.py
```

---

### 2. Jalankan Spark Streaming

```bash
python scripts/streaming_layer.py
```

---

### 3. Jalankan Dashboard

```bash
streamlit run dashboard/dashboard_streamlit.py
```

---

## 🛠️ Teknologi

* Python
* PySpark
* Streamlit
* JSON

---

## 👨‍💻 Identitas

* Nama: (M. Agil Tauhit Ismail)
* NIM: (230104040223)
* Kelas: (TI23A)

---

## ⏰ Deadline

📅 Rabu, 01 April 2026
🕚 23.00 WITA

---