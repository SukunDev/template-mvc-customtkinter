# TEMPLATE MVC CUSTOMTKINTER

Proyek ini adalah template untuk aplikasi berbasis arsitektur MVC menggunakan `customtkinter`.

## Cara Menjalankan Proyek

1. Clone proyek ini
2. Buat dan aktifkan virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install paket yang diperlukan

```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi

```bash
python3 main.py
```

## Dependensi

Proyek ini menggunakan beberapa dependensi yang tercantum dalam [requirements.txt](requirements.txt):

- `customtkinter==5.2.2`
- `darkdetect==0.8.0`
- `greenlet==3.0.3`
- `packaging==24.0`
- `SQLAlchemy==2.0.30`
- `typing_extensions==4.11.0`

## Konfigurasi

Konfigurasi aplikasi dapat ditemukan di [config.py](config.py). Beberapa pengaturan penting termasuk:

- `SECRET_KEY`: Kunci rahasia untuk aplikasi
- `SQLALCHEMY_DATABASE_URI`: URI untuk koneksi database
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Mengaktifkan atau menonaktifkan sistem event SQLAlchemy
- `APP_NAME`: Nama aplikasi
- `APP_WIDTH`, `APP_HEIGHT`: Ukuran aplikasi
- `APP_MIN_WIDTH`, `APP_MIN_HEIGHT`: Ukuran minimal aplikasi

## Arsitektur MVC

Proyek ini menggunakan arsitektur Model-View-Controller (MVC):

- **Model**: Mengelola data dan logika bisnis. Lihat [models](models/).
- **View**: Mengelola antarmuka pengguna. Lihat [views](views/).
- **Controller**: Menghubungkan model dan view. Lihat [controllers](controllers/).

## Lisensi

Proyek ini dilisensikan di bawah MIT License.
