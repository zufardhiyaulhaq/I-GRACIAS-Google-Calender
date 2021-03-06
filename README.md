# I-GRACIAS-Google-Calender
Tools yang dapat digunakan untuk mengambil jadwal mahasiswa di igracias dan memasukannya kedalam Google Calender. Google Calender dapat digunakan di smartphone dan dapat dikonfigurasi pengingat/reminder sehingga membantu mahasiswa.

### Requiremet
- Python 2.7
- Google API Library
```
pip install --upgrade google-api-python-client oauth2client
```
- Akses I-GRACIAS

## Petunjuk
### Aktifkan API Goole Calender
- https://developers.google.com/calendar/quickstart/python
- Move this file to your working directory and rename it client_id.json.

### Ambil Data Mata Kuliah dari I-GRACIAS
- Buka I-GRACIAS melalui web browser.
- Registrasi > Jadwal > Jadwal Mahasiswa.
- Buka Inspect Element > Network.
- Refresh Web Browser (F5).
- Akan muncul banyak data, Seleksi data tersebut, dan cari data yang memuat JSON Files.
<p align="center">
<img src="https://preview.ibb.co/dpKQ46/data1.png">
</p>
- Pada bagian response, salin Response Payload.
<p align="center">
<img src="https://image.ibb.co/eyQJrm/payload.png">
</p>
- Buat file data.json dan pastekan hasil dari Response Payload.

Catatan : Data pada tutorial ini diakses dengan Mozilla Firefox

### Send to Google Calender
- Unduh Program.py dari Repositori ini.
- File program.py, client_id.json dan data.json harus berada didalam satu folder.
- Jalankan program.py
- Masukan tanggal pertama jadwal anda ingin muncul di kalender.
- Masukan tanggal terakhir jadwal anda ingin muncul di kalender.
- Akan terbuka sebuah tab baru, pilih akun google sesuai akun di google calender.
- Data-data pelajaran akan otomatis masuk kedalam google calender.

#### Tips
- Tanggal pertama dan tanggal terakhir dikonfigurasi sesuai jadwal satu semester anda.

#### Catatan
Tools ini tidak mengambil API dari I-GRACIAS Telkom University, Hanya mahasiswa Telkom University yang dapat mengakses I-GRACIAS yang dapat menjalankan aplikasi ini. Karena aplikasi ini membutuhkan data jadwal mahasiswa yang diakses secara manual.
