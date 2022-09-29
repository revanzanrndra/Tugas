## Link Heroku
https://tugas2-revanza.herokuapp.com/todolist

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