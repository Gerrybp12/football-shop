- Membuat sebuah proyek Django baru: untuk membuat project django baru pertama saya membuat environment untuk mengisolasi depedencies yang akan saya install. Lalu saya membuat requirement.txt yang berisi depedencies yang diperlukan project django saya. Setelah itu menjalankan "pip install -r requirements.txt", dilanjut dengan konfigurasi .env dan env.prod untuk mengakses database. Dan diakhiri dengan menghubungkan ke repository github.

- Membuat aplikasi dengan nama main pada proyek tersebut: untuk membuat directory baru bernama "main" dapat dengan command "python manage.py startapp main" dan didaftarkan ke INSTALLED_APPS di settings.py, directory ini digunakan untuk struktur project.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main: Untuk menghubungkan 'main' ke directory utama perlu mengedit urls.py di directory utama dengan mengimport include dari django.urls. Didalam urlpattern isi dengan fungsi path('route', include('directory_urls.py (main.urls)')).

- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib: mengisi model.py didalam directory main dengan class yang kita inginkan (Product) dengan class dasar models.Model yang diimportt dari django.db. Lalu didalam class-nya, menambahkan atribut yang diinginkan sesuai dengan tipe data yang diinginkan.

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu: untuk langkah ini dimulai dengan import render dari django.shortcuts di views.py directory main. Lalu membuat fungsi dengan parameter request, buat fungsi ini mereturn render(request, "nama_file_html", object data yang ingin di kirim). Setelah itu buat folder baru bernama templates di 'main' untuk tempat file html-nya. Lalu buat struktur html yang diinginkan dengan menggunakan variable object yang sudah dikirim viws.py.

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py: untuk langkah ini, pertama-tama buat urls.py di directory main dengan mengimport path dari django.urls dan fungsi dari views.py yang ingin di perlihatkan. Dilanjut dengan membuat list berisi object URLPattern yang dihasilkan dari fungsi path('route', fungsi_views.py).

- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet: Sesuai ketentuan dari Pacil Web Service untuk melakukan deploy perlu membuat project baru pws lalu mengisi variable di environs sesuai dengan .env.prod lalu melakukan command sesuai ketentuan dari pws: 'git remote add pws ....', 'git branch -M master', lalu 'git push pws master'. sebelum push di settings.py pada ALLOWED_HOST tambahkan url deployment PWS.

Bagan request client web aplikasi berbasis Django:
HTTP Request -> URLS(urls.py) -> View(views.py) <-> Model(models.py)  
Template(.html) -> Vieww(views.py) -> HTTP Response (HTML)
Model: berisi struktur data dan tabel database. Berhubungan dengan View dengan read/write data.
View: berisi class dan fungsi yang untuk membuat algoritma dari project. Berhubungan dengan Model dengan read/write data.
URLS: menentukan URL route yaitu view mana yang dipanggil ketika user mengakses suatu url. Berhubungan dengan view untuk mengirim request.
Template: Digunakan untuk menampilkan data dari view ke user dengan struktur HTML. Berhubungan dengan view untuk mengakses data object.

Jelaskan peran settings.py dalam proyek Django? Peran settings.py adalah untuk konfigurasi project seperti app yang akan digunakan di INSTALLED_APPS, MIDDLEWARE untuk menangani request sebelum/sesudah sampai ke view, DATABASES untuk konfigurasi koneksi ke database, ALLOWED_HOSTS untuk menentukan yang bisa mengakses project.

Bagaimana cara kerja migrasi database di Django? proses migrasi terjadi saat melakukan perubahan di models.py. dengan menjalankan perintah 'python manage.py makemigrations' django akan membaca perubahan di models.py lalu membuat file migrasi di folder migrations/ yang berisi instruksi python mendeskripsikan perubahan model.py. jika sudah yakin dengan perubahannya, dengan menjalankan 'python manage.py migrate' perubahan pada models.py sudah tersimpan dan terbaca di project.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

1. Framework django sudah mempunyai fitur-fitur yang cukup untuk mengembangkan website seperti autentikasi user, admin panel, ORM (Object-Relational Mapping), routing, middleware, template engine, dsb. Jadi programmer permula cukup fokus ke konsep utama pengembangan aplikasi.
2. Django menggunakan aturan MVT (model view template) yang mudah dipahami dan membantu programmer pemula memahami arsitektur perangkat lunak.
3. Menggunakan Python yang termasuk high level languange yang mudah dipahami programmer pemula
4. ORM, dengan ORM untuk menghubungkan database, proses penggunaan database menjadi mudah.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya? Tutorial sudah sangat lengkap dan diisi dengan bahasa yang mudah dipahami, jadi overall sudah bagus.
