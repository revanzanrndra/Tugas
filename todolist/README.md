## Link Heroku
https://tugas2-revanza.herokuapp.com/todolist

## README Tugas 4

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} berfungsi untuk melakukan proteksi terhadap Cross Site Request Forgeries atau Pemalsuan Permintaan Lintas Situs. Jika tidak ada potongan kode tersebut pada elemen <form>, maka response code yang dikembalikan oleh server adalah 403, artinya adalah server mengerti apa yang di-request oleh user, tetapi tidak mau mengautorisasinya. Jadi memang sepenting itu keberadaan token csrf. Kalaupun server tidak melarang hal tersebut, maka dapat terjadi tindak serangan terhadap situs web yang dibuat, serangan tersebut menggunakan kredensial dari pengguna yang sedang log in di website kita dan masuk ke situs web "jahat"

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, di file forms.py, buat class atribut-atribut yang di-assign dengan form fields, kemudian di views.py, buat sebuah dictionary dengan pasangan key:value, anggap key-nya adalah 'form' dan nama kelas yang dibuat di forms.py adalah InputForm() sehingga dictionary yang dibuat adalah context={'form':InputForm()}. Terakhir di file HTML, tinggal tulis saja {{ form }} sesuai dengan kebutuhan.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Data yang diinput oleh pengguna artinya adalah form disubmit dengan POST request, view akan membuat form dan mengisinya dengan data dari request, form akan dicek apakah valid atau tidak, jika valid, maka datanya akan dimasukkan ke database lalu di-redirect ke template html mana yang akan dituju. Terakhir, form dan atributnya akan dimasukkan ke template HTML, tepatnya di {{ form }}

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Membuat aplikasi todolist dengan perintah startapp, lalu membuat template todolist.html, mendaftarkan aplikasi di settings.py, dan membuat urls.py lalu menambahkan path todolist.

Membuat model Task yang berisi atribut user dengan parameter User, date, title, dan description.

Membuat views registrasi, login, dan logout, lalu membuat file template html logil.html dan registrasi.html, lalu menambahkan path ke urls.py di direktori todolist

membuat views create_task dan membuat file html-nya, lalu menambahkan path ke urls.py di direktori todolist

lalu saya deploy ke Heroku, di aplikasi heroku, saya membuat dua akun dengan masing-masing dimasukkan 3 data.


## README Tugas 5

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- Inline CSS adalah menambahkan style yang diinginkan di dalam tag HTML. Kelebihannya adalah mudah dan cepat untuk digunakan, apalagi jika ingin melakukan testing, dan juga tidak perlu membuat file terpisah. Kekurangannya adalah untuk file HTML yang besar, pastinya sangat memakan waktu untuk menambahkan style di setiap elemen HTML.
- Internal CSS adalah menambahkan tag style di section head dari template HTML yang ingin dihias. Kelebihannya adalah bisa dengan mudah menghias class dan id dari bagian yang ingin dihias. Kekurangannya adalah menambah waktu muat dan ukuran halaman.
- External CSS adalah melakukan link eksternal css file dengan template HTML yang ingin dibuat. Jadi kita menghias halaman web di luar template. Kelebihannya adalah file HTML kita jadi terlihat lebih rapi dan memiliki ukuran halaman yang lebih kecil karena file css-nya terpisah. Kekurangannya adalah halaman web mugnkin mengalami kesalahan render jika file external css gagal diload.

## Jelaskan tag HTML5 yang kamu ketahui.
- Paragraph : Membuat text sebagai paragraf.
- Heading : Untuk membuat text sebagai heading, ada 1-6 heading, makin kecil nomornya, makin besar ukuran headingnya.
- Bold : Menebalkan text.
- Italic : Memiringkan text.
- Underline : Membuat text memiliki garis di bawahnya.
- Anchor : Menghubungkan suatu elemen dengan link.
- Image : Memasukkan gambar.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Element Selector : Menggunakan tag HTML sebagai selector.
- ID Selector : menggunakan ID sebagai selector, perlu menambahkan # di depannya jika ingin mengubah properti di dalam ID tersebut.
- Class Selector : menggunakan class sebagai selector, perlu menambahkan . di depannya jika ingin mengubah properti di dalam class tersebut.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Saya menggunakan internal CSS dan Bootstrap untuk melakukan styling terhadap template HTML saya. Kustomisasi yang saya lakukan di login, register, dan create_task adalah dengan menengahkan setiap properti HTML, menambahkan border pada form, dan mengganti background warna yang gelap. Untuk di todolist, saya menambahkan navbar, membuat card untuk setiap task-nya, menambahkan animasi jika hover card, menambahkan animasi juga jika hover button, mengganti background color dengan warna yang gelap, mengganti warna card menjadi hijau jika tombol checklist diklik, dan menghapus card jika ditekan tombol delete.
Cara agar halaman menjadi responsive adalah dengan menambahkan tag meta yang berisi 'name="viewport" content="width=device-width, initial-scale=1"' di section head.