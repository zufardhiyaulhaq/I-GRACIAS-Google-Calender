# I-GRACIAS-Google-Calender
Tools yang dapat digunakan untuk mengambil jadwal mahasiswa di igracias dan memasukannya kedalam Google Calender. Google Calender dapat digunakan di smartphone dan dapat dikonfigurasi pengingat/reminder sehingga membantu mahasiswa.

### Requiremet
- Python 2.7
- Akses I-GRACIAS

## PETUNJUK
### Aktifkan API Goole Calender
- Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
- On the Add credentials to your project page, click the Cancel button.
- At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
- Select the Credentials tab, click the Create credentials button and select OAuth client ID.
- Select the application type Other, enter the name "Google Calendar API Quickstart", and click the Create button.
- Click OK to dismiss the resulting dialog.
- Click the file_download (Download JSON) button to the right of the client ID.
- Move this file to your working directory and rename it client_id.json.

### Ambil Data Mata Kuliah dari I-GRACIAS
- Buka I-GRACIAS melalui web browser.
- Registrasi > Jadwal > Jadwal Mahasiswa.
- Buka Inspect Element > Network.
- Refresh Web Browser (F5).
- Akan muncul banyak data, Seleksi data tersebut, dan cari data yang memuat JSON Files.
![Image1](https://preview.ibb.co/dpKQ46/data1.png)
- Pada bagian response, salin Response Payload.
- Buat file data.json dan pastekan hasil dari Response Payload.

Catatan : Data pada tutorial ini diakses dengan Mozilla Firefox

### Send to Google Calender


#### Catatan
Tools ini tidak mengambil API dari I-GRACIAS Telkom University, Hanya mahasiswa Telkom University yang dapat mengakses I-GRACIAS yang dapat menjalankan aplikasi ini. Karena aplikasi ini membutuhkan data jadwal mahasiswa yang diakses secara manual.
