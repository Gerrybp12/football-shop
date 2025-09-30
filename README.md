https://gerry-bima-footballshop.pbp.cs.ui.ac.id/

# Tugas2

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

# Tugas3

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam sebuah platform data sangatlah penting untuk memastikan semua variable terisi dan bisa diperlihatkan. Untuk itu proses data delivery diperlukan agar data bisa sampai tujuan dengan aman, akurat, dan tidak terubah. Dalam projek django, ORM berperan besar karena mengubah objek python menjadi data yang dipahami database, dan sebaliknya.

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
menurutku JSON lebih baik, JSON adalah singkatan dari JavaScript Object Notation dan saya lebih terbiasa membaca object javascript daripada xml. Alasan mengapa JSON lebih populer dari XML adalah karena beberapa faktor, diantaranya: 
- Sintaks yang Ringkas dan Mudah Dibaca: Sintaks JSON menggunakan pasangan "key-value" yang sederhana dan mudah dibaca, mirip dengan objek JavaScript. Sebaliknya, XML menggunakan tag pembuka dan penutup yang membuatnya lebih bertele-tele (verbose) dan kurang ringkas. 
- Integrasi yang Lebih Baik dengan JavaScript: Karena JSON adalah singkatan dari "JavaScript Object Notation," ia secara alami cocok dengan JavaScript. Pengembang dapat langsung mengonversi string JSON menjadi objek JavaScript tanpa perlu parser yang rumit, yang membuat proses pengembangan jauh lebih cepat.
- Parsing yang Lebih Cepat: Karena sintaksnya yang lebih sederhana dan ukuran file yang lebih kecil, JSON dapat di-parsing lebih cepat. Dalam aplikasi yang sangat bergantung pada pertukaran data real-time, seperti API, kecepatan ini adalah keuntungan besar.
- Ideal untuk API: Sebagian besar API modern (RESTful API) menggunakan JSON sebagai format pertukaran data utama. Format ini sangat efisien untuk mengirimkan data terstruktur antara server dan klien (misalnya, browser web atau aplikasi seluler) dengan overhead minimal.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
method is_valid disini digunakan dalam views.py di kode 'if form.is_valid() and request.method == "POST":' form adalah object dari class ProductForm di forms.py. form.is_valid() diperlukan untuk mengecek apakah semua kolom data sudah diisi dengan benar oleh user (tidak dikosongkan dan sesuai tipe data), jika sudah benar akan mereturn true jika tidak false.

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token disini digunakan untuk memastikan bahwa submit form berasal dari request user di create_product.html dengan melakukan validasi apakah token sudah sama dengan token yang di generate otomatis oleh django. Jika tidak ada csrf_token django tidak bisa memverifikasi apakah submit form benar-benar dari user, yang bisa dimanfaatkan oleh penyerang untuk memasukkan sembarang data ke database kita.

Penjelasan checklist step by step:

- Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID: Menambahkan fungsi show_xml dengan parameter request yang berisi product_list yaitu data dari semua produk lalu diubah kedalam time xml. Menambahkan fungsi show_json dengan parameter request yang sama dengan show_xml tetapi product_list diganti ke json. Menambahkan show_xml_by_id dengan parameter request dan product_id yang berisi percobaan mengambil data produk berdasarkan product_id dengan .filter(), jika ada di ubah kedalam bentuk xml seperti sebelumnya. Menambahkan fungsi show_json_by_id yang mirip seperti show_xml_by_id namun data diubah ke bentuk json.

- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1: untuk membuat routing kira perlu menambahkan kode di urls.py. pertama-tama import keempat fungsi yang sudah dibuat, lalu gunakan path() yang diimport dari django.urls untuk menentukan path dari fungsi tersebut.

- Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek: disini saya menambahkan beberapa baris kode ke main.html dengan block code, diantaranya: logika 'if not product_list' yang isisnya ditampilkan jika product_list kosong, lalu 'for product in product_list' untuk interasi object product di product_list dan menampilkan variable dari objectnya satu persatu. untuk tombol "Add" saya menambahkan 'a' yang terhubung ke create_product dan terisi dengan 'button'.

- Membuat halaman form untuk menambahkan objek model pada app sebelumnya: agar halaman form nanti bisa mempunyai fungsi untuk mengisi object Product, perlu membuat fungsi baru di views yaitu create_product(request) fungsi ini menggunakan class ProductForm(modelForm) yang saya buat di forms.py, class ini digunakan untuk struktur data yang akan di sumbit. Dengan menggunakan validasi is_valid() data bisa tersubmit dengan benar. Yang penting juga menambahkan csrf_token agar django bisa memverifikasi bahwa request submit dari user.

- Membuat halaman yang menampilkan detail dari setiap data objek model: agar halaman bisa menampilkan produk yang diinginkan, saya memverifikasinya dengan id dengan fungsi show_product yang menerima parameter id, lalu menggunakan get_object_or404() yang diimport dari django.shortcuts dan mempassing dengan render() ke halaman untuk detail produk. Untuk halaman detail produk saya membuat product_detail.html karena sudah menerima object produk hanya tinggal membuat struktur html untuk menampilkan variable product.

Screenshot postman:

![alt text](image.png)
https://gerry-bima-footballshop.pbp.cs.ui.ac.id/json

![alt text](image-1.png)
https://gerry-bima-footballshop.pbp.cs.ui.ac.id/json/e9727c8b-b4f6-4f6a-9c77-6c66161bd3e8

![alt text](image-2.png)
https://gerry-bima-footballshop.pbp.cs.ui.ac.id/xml

![alt text](image-3.png)
https://gerry-bima-footballshop.pbp.cs.ui.ac.id/xml/e9727c8b-b4f6-4f6a-9c77-6c66161bd3e8

Untuk feedback tutorial 2 overall lancar dan aman.

# Tugas 4

Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya: Django AuthenticationForm adalah form bawaan Django yang digunakan untuk menangani proses login pengguna. Form ini secara otomatis memverifikasi username dan password terhadap data yang tersimpan di database, jadi kita tidak perlu membuat logika autentikasi dari nol. Kelebihan utamanya adalah kemudahan penggunaan karena form ini sudah terintegrasi dengan sistem autentikasi Django, mendukung pengecekan password hashing, serta mengurangi kemungkinan bug karena telah diuji dengan baik. Namun, ada kekurangannya juga: AuthenticationForm kurang fleksibel jika alur login yang dibutuhkan berbeda jauh dari standar bawaan Django. Misalnya, jika ingin menambahkan field tambahan atau memodifikasi perilaku validasi tertentu, kita mungkin harus membuat form kustom sendiri. Selain itu, tampilannya sangat sederhana sehingga sering kali memerlukan penyesuaian CSS atau penggantian template untuk menyesuaikan desain antarmuka.

Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut? Autentikasi adalah proses memastikan identitas pengguna, misalnya dengan memeriksa apakah kombinasi username dan password yang dimasukkan sesuai dengan data yang ada di sistem. Otorisasi adalah langkah setelah autentikasi berhasil, yaitu menentukan apa saja yang boleh dilakukan pengguna tersebut, seperti apakah ia bisa menambah produk, menghapus data, atau hanya melihat informasi. Django menangani autentikasi melalui modul django.contrib.auth yang menyediakan fungsi login, logout, serta form autentikasi. Untuk otorisasi, Django menyediakan sistem permission dan group—permission menentukan hak spesifik, sedangkan group memudahkan pengelompokan pengguna dengan hak akses yang sama. Dengan pendekatan ini, Django memisahkan proses mengenali pengguna dan mengatur izin mereka dengan jelas.

Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web? Session menyimpan data di server, sehingga lebih aman karena pengguna tidak bisa memanipulasinya langsung. Ini juga mendukung penyimpanan data yang lebih besar dan kompleks. Kekurangannya, session membutuhkan sumber daya server tambahan untuk menyimpan semua data dari banyak pengguna sekaligus, dan bisa meningkatkan beban server jika traffic besar. Sementara itu, cookies menyimpan data di sisi client, yang membuatnya ringan bagi server dan cocok untuk menyimpan informasi kecil seperti preferensi pengguna. Tapi, cookies lebih rentan terhadap pencurian dan manipulasi jika tidak diamankan dengan baik, dan kapasitas penyimpanannya terbatas sehingga tidak cocok untuk data yang besar.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut? Cookies tidak sepenuhnya aman secara default karena ada risiko seperti session hijacking, manipulasi isi cookies, atau serangan CSRF yang memanfaatkan cookies yang valid. Penyerang bisa saja mencuri cookies melalui serangan XSS dan menggunakannya untuk berpura-pura menjadi pengguna yang sah. Django membantu meminimalkan risiko ini dengan beberapa mekanisme bawaan. Cookies yang digunakan untuk session ditandatangani dan dienkripsi menggunakan SECRET_KEY, sehingga tidak bisa dimodifikasi tanpa terdeteksi. Django juga menyediakan middleware CSRF protection yang bekerja bersama csrf_token untuk memverifikasi request form. Selain itu, ada pengaturan seperti SESSION_COOKIE_SECURE dan CSRF_COOKIE_SECURE yang memaksa cookies hanya dikirim melalui koneksi HTTPS, serta opsi HttpOnly untuk mencegah akses cookies lewat JavaScript. Dengan konfigurasi bawaan ini dan praktik pengembangan yang aman, penggunaan cookies di Django dapat dibuat jauh lebih aman.

Penjelasan cheklist step by step:

- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya: Ada tiga fungsi yang perlu dibuat yaitu login, registrasi, dan logout. Pertama-tama saya membuat logika fungsinya di views.py: Untuk fungsi register saya menggunakan UserCreationForm dari django.contrib.auth.forms, jadi variable-variable form sudah terbuat otomatis oleh django, selanjutnya saya hanya perlu membuat logika yang menghandle submit form dengan menggunakan form.is_valid() fungsi bawaan formnya juga yang mereturn true jika input user sudah benar, saya juga menambahkan login required. Kedua saya membuat fungsi login, saya menggunakan AuthenticationForm dari django.contrib.auth.forms dan login dari django.contrib.auth, seperti register, variable sudah dibuatkan oleh AuthenticationForm, jadi saya lanjut membuat logika saat user submit formnya dengan menggunakan form.is_valid() seperti register. Ketiga saya membuat fungsi logout, fungsi ini cukup simpel karena hanya perlu menggunakan fungsi logout dari django.contrib.auth. Setelah tiga fungsi dibuat saya membuat struktur html untuk login dan register, untuk logout saya menambahkannya di main.html. Setelah algoritma login, register, logout berfungsi dengan benar saya membuat login required dari django.contrib.auth.decorators untuk fungsi show_main(), create_product(), show_product().

- Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal: untuk membuat dua akun di lokal, saya menjalankan server secara lokal lalu menambahkan akun secara manual menggunakan fungsi register yang sudah dibuat. Untuk membuat tiga dummy data di setiap akun, saya login untuk setiap akun lalu mengakses create product dan buat tiga produk.

- Menghubungkan model Product dengan User: untuk membuat model terhubung dengan user, saya menambahkan variable baru di class Product di models.py dengan mengimport user dari django.contrib.auth.models, lalu menggunakan models.ForeignKey() yang mereturn ke variable yang sudah dibuat "user"

- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi: Untuk menampilkan username user yang sedang login, saya mengubah user didalam context show_main menjadi request.user.username, Karena ingin menyimpan cookies untuk login, kita perlu melakukan perubahan untuk fungsi login di views.py, dengan menambahkan response.set_cookie(), untuk variable yang dimasukkan ke fungsi ini adalah last_login yang akan saya ambil di context show_main dengan request.COOKIES.get() dan last_login ini akan ditampilkan di main.html.

# Tugas 5

Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut: Saya akan menggambarkan urutan ini dalam bentuk list, yang paling awal yang paling di prioritaskan:
1. !important, jika style terdapat tag ini maka ia akan mengalahkan semua CSS selector yang lain.
2. Inline Style, karena langsung dimasukkan kedalam elemen HTML (bukan tailwind) kesannya Inline Style ini seperti "perintah langsung" ke satu elemen unik, ini akan berguna dalam proses pembuatan jika tidak ingin memusingkan elemen lain.
3. Menggunakan ID, seperti Inline Style id juga bersifat unik tetapi penulisan terpisah jadi level dibawah Inline Style.
4. Class dan Pseudo-class, ini bisa diterapkan ke banyak elemen sekaligus jadi agak rendah prioritasnya.
5. Elemen/tag, karena langsung mengspesifika elemen yang ingin di kasih style logis jika selector ini menjadi yang paling rendah.
Jika diperhatikan urutan ini sudah sangat masuk akal dan akan sangat memudahkan kita dalam proses styling.

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa: Resposive desain adalah konsep yang sangat penting dalam pengembang aplikasi web dan menjadi salah satu hal yang paling diperhatikan dalam proses pengembangan, sudah banyak web-app terkenal yang sudah menerapkan ini, contoh youtube. Mengapa sangat penting? Karena ada berbagai macam device di dunia ini dengan bermacam-macam ukuran, bahkan satu device yang sama pun bisa berbeda-beda ration contoh laptop 16:9 dengan 21:9, jadi agar user experience bisa maksimal dan target user bisa luas, responsive desain yang bisa menyesuaikan kesegalan ratio sangat diperlukan.

Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut: Margin, border, dan padding adalah tiga elemen css yang sangat penting dan selalu dipakai. Kegunaan utamanya adalah mengatur layout dan desain dari suatu elemen agar bisa sesuai dengan keinginan kita. Perbedaan antara ketiganya dan cara implementasi:
1. Margin: Cara implemetasi, margin: 20px (CSS) dan bisa menambahkan spesifik arah (top, bottom, left, right), margin ini menambah jarak atau seperti kotak kosong di luar elemen (diluar border).
2. Padding: Cara implementasi, padding: 20px (CSS) dan juga bisa menambahkan spesifik arah, mirip seperti margin tetapi jarak atau kotak kosong tersebut berada di dalam elemen (didalam border).
3. Border: cara implementasi border: 20px warna (CSS) dan juga bisa menambahkan spesifik arah, kegunaan border ini seperti menambahkan garis tepi atau pada sebuah elemen, jadi berbeda dengan padding dan margin yang tidak terlihat yang letaknya diantara margin dan padding.

Jelaskan konsep flex box dan grid layout beserta kegunaannya: Flexbox dan Grid Layout adalah dua sistem tata letak utama dalam CSS yang digunakan untuk mengatur posisi elemen pada halaman web secara responsif dan efisien, namun keduanya memiliki konsep dan tujuan yang berbeda. Flexbox atau Flexible Box Layout merupakan sistem layout satu dimensi yang digunakan untuk menyusun elemen secara horizontal (baris) atau vertikal (kolom) dalam satu arah saja. Flexbox sangat cocok untuk mengatur posisi elemen seperti navbar, tombol, atau daftar kartu karena mampu menyesuaikan ukuran elemen secara fleksibel, mendistribusikan ruang secara otomatis, serta mempermudah penyusunan dan perataan elemen, baik di tengah, kiri, kanan, atas, maupun bawah. Sementara itu, Grid Layout adalah sistem layout dua dimensi yang memungkinkan pengembang mengatur elemen secara horizontal dan vertikal secara bersamaan. Grid sangat ideal untuk membuat struktur tata letak yang kompleks seperti halaman utama, dashboard, atau galeri, karena memungkinkan pembagian kolom dan baris secara presisi serta penempatan elemen pada posisi grid tertentu. Secara umum, Flexbox lebih cocok digunakan untuk tata letak sederhana yang berfokus pada distribusi dan penyusunan elemen dalam satu arah, sedangkan Grid lebih tepat untuk membuat struktur layout yang kompleks dengan pengaturan dua dimensi. Keduanya dapat dikombinasikan dalam satu proyek, misalnya menggunakan Grid untuk membentuk kerangka besar halaman, lalu Flexbox di dalamnya untuk menyusun elemen-elemen kecil agar tampilan web menjadi lebih fleksibel, responsif, dan terstruktur.

Cheklist step by step:

Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin: Disini saya memilih untuk memakai tailwind CSS dengan menghubungkannya ke project di base.html, dan satu persatu elemen di setiap HTML saya desain semenarik mungkin agar enak dipandang.

Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
 Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
 Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!): Untuk menghandle tidak adanya product saya menambahkan block if untuk kondisi list produk kosong, dan jika ada akan menampilkan card_product.html yang sudah saya buat dengan iterasi for loop sesuai jumlah product agar responsive saya balut dengan grid yang juga menyesuaikan ukuran device.

Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut: sebelumnya saya membuat fungsi untuk menghandle fungsi button ini di views.py dan menaruhnya di urls.py ke url yang akan saya masukan di button nya. Untuk penghapusan produk cukup dengan product.delete. Untuk pengeditan produk saya menggunakan ProductForm seperti pembuatan produk dan membuat halama khusus untuk pengeditan. Setelah kedua fungsi disiapkan tinggal menambah button ke card_product.html.

Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop: Karena saya memutuskan untuk membuat navbar hamburger untuk mobile dan navbar biasa untuk dekstop maka saya menggunakan device:style dari tailwind CSS untuk menambahkan hidden di device yang bersesuaian. Untuk menhandle kemunculan tulisan saat button navbar di klik saya menggunakan script untuk mentoogle hidden di class mobile-menu-button yang dihubungkan ke buttonnya.

