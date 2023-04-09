# Komiku Komik List
- Komiku Komik List adalah program yang berguna untuk mengatur daftar komik yang terdapat di website<a href='https://komiku.com'>KOMIKU<a>.<br>
- Untuk menggunakan program ini diperlukan sedikit penguasaan bahasa pemrograman PYTHON.<br>
- Program ini akan menghasilkan daftar komik beserta chapter terakhir dari komik yang anda telah baca.

<h2>Cara Penggunaan</h2>
- Menulis judul komik baru di file komik-favorit.txt (format penulisan lihat file komik-favorit.txt).<br>
- Menulis chapter komik baru di old-chap-komik.txt (format penulisan lihat file old-chap-komik.txt).<br>
- Data chapter terbaru akan otomatis ditambahkan ke new-chap-komik.txt setelah program dijalankan<br>
- file daftar-komik.txt akan berisi daftar lengkap komik beserta chapter.<br>
- Jika ada data "komik baru" yang tidak ditemukan, maka komik tersebut akan ditambahkan ke file tidak-ada-judul.txt.<br>
- Urutan antara judul komik dan chapter harus sama!!!!

<h2>Cara Memperbaiki Judul Komik Pada File tidak-ada-judul.txt</h2>
- Judul yang memiliki tanda "-" akan selalu ditambahkan ke tidak-ada-judul.txt<br>
- Penulisan judul harus sesuai format<br>
- Manhua akan masuk ke dalam list tidak-ada-judul.txt<br>

<h2>Installation</h2>
pip install requests<br>
pip install bs4
