# Simple AI Inference Analyzer

Simple Python application for analysing AI inference data.

## Penerangan Projek

Aplikasi ini membaca data inferens AI daripada fail CSV, menapis rekod berdasarkan nilai confidence, mengira statistik asas dan menghasilkan carta bar jumlah pengesanan mengikut kelas objek.

## Fungsi Utama

- Membaca fail CSV menggunakan pandas.
- Memaparkan lima rekod pertama.
- Menerima nilai confidence threshold daripada pengguna.
- Menapis rekod berdasarkan nilai confidence.
- Mengira statistik data inferens.
- Menyimpan data yang telah ditapis.
- Menghasilkan carta bar menggunakan Matplotlib.
- Mengendalikan ralat fail dan input pengguna.

## Struktur Projek

```text
simple-ai-inference-analyzer/
├── data/
│   └── inference_data.csv
├── output/
│   ├── filtered_data.csv
│   └── object_count.png
├── main.py
├── analysis.py
├── README.md
├── AI_USAGE.md
├── requirements.txt
└── .gitignore