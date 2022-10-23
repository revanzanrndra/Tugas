## Link Heroku
https://tugas2-revanza.herokuapp.com/todolist

## README Tugas 6

## Perbedaan antara asynchronous programming dengan synchronous programming:
Dalam asynchronous programming, lebih dari satu operasi bisa dieksekusi secara bersamaan tanpa perlu menunggu satu operasi selesai. Sementara synchronous programming hanya bisa mengeksekusi satu operasi dalam satu waktu, artinya saat satu operasi sedang dieksekusi, maka operasi lain akan diblok untuk sementara waktu sampai operasi yang sedang dieksekusi saat ini selesai.

## Maksud dari paradigma Event-Driven Programming dan contohnya:
Paradigma Event-Driven Programming adalah sebuah paradigma pemrograman di mana alur berjalannya program ditentukan oleh sebuah event yang dipicu oleh aksi pengguna, dalam penerapannya pada tugas 6 ini, terdapat onclick yang akan berfungsi saat user mengklik suatu tombol yang pada tugas ini adalah tombol checklist untuk merubah warna card menjadi hijau, tombol delete untuk menghapus card, dan tombol submit pada modal untuk men-submit task.

## Penerapan asynchronous programming pada AJAX:
Seperti yang sudah diketahui, asynchronous programming merupakan model pemrograman di mana lebih dari satu operasi bisa berjalan di waktu yang bersamaan. Dalam konteks komunikasi web, model yang digunakan juga berupa synchronous dan asynchronous, asynchronous web communication menunjukkan bahwa pengguna bisa terus berinteraksi dengan halaman web selama data di-load tanpa perlu me-reload halaman, hal ini bisa dilakukan dengan implementai AJAX.

Cara implementasi AJAX adalah dengan menambahkan ```html 
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>``` pada header HTML, lalu tulis sintaks ajax pada tag script sesuai dengan kebutuhan.

## Cara saya mengimplementasikan checklist deskripsi tugas 6:
# AJAX GET
- Membuat view yang mengembalikan seluruh data task dalam bentuk JSON

    ```python   
    def get_todolist_json(request):
        data = Task.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
- Membuat path /todolist/json yang mengarah ke view yang baru dibuat

    Pada file urls.py, di fungsi urlpatterns, saya menambahkan potongan kode berikut:
    ```python 
    path('json/', get_todolist_json, name='get_todolist_json'),
    ```

- Mengambil task dengan AJAX GET

    Dalam tag script, saya membuat fungsi getTodolist yang mengambil data dari database dalam bentuk JSON, lalu membuat fungsi refreshTodolist, pada fungsi ini, saya mengiterasi objek data yang dikembalikan oleh getTodolist, lalu dari data tersebut saya meng-construct card dengan membuat script html di tiap iterasinya, script tersebut akan di-concat ke string variabel htmlString, setelah iterasi selesai, innerHTML dari div untuk meletakkan card akan diisi dengan htmlString.

# AJAX POST
- Membuat tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task

    Untuk membuat tombol Add Task yang membuka sebuah modal, saya menambahkan potongan kode berikut:
    ```html 
    <div class="container">
        <div class="title" style="padding-top: 7px; padding-left: 7px; padding-right: 7px;">
            <h6><font>Welcome, {{username}}</font></h6>
            <h3><font>List of Tasks</font></h3>
            <button id="create-btn" data-bs-toggle="modal" data-bs-target="#createTaskModal"><font>Add Task</font></button>
        </div>
        </div>
    ```
    Bisa dilihat pada potongan kode di atas saya menambahkan atribut data-bs-target untuk membuka modal dengan id createTaskModal.

    Selanjutnya saya membuat modal, dengan potongan kode berikut:
    ```html 
    <div class="modal fade" id="createTaskModal" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header border-0">
                <h5 class="modal-title"><font>CREATE NEW TASK</font></h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <form id="createTaskForm" onsubmit="return false;">
                {% csrf_token %}
                <div class="modal-body">
                <fieldset>
                    <input type="text" name="title" placeholder="Title" class="form-control mb-2">
                    <textarea name="description" class="form-control" placeholder="Description" style="height:200px; width:100%"></textarea>
                </fieldset>
                </div>
                <div class="modal-footer border-0">
                <button id="btn-submit" class="btn btn-primary" value="Submit" type="submit" data-bs-dismiss="modal">Submit</button>
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </form>
            </div>
        </div>
        </div>
    ```

- Membuat view baru untuk menambahkan task baru ke dalam database

    Saya menambahkan fungsi berikut:
    ```python
    def add_task_ajax(request):
        if request.method == "POST":
            title = request.POST.get('title')
            description = request.POST.get('description')
            new_task = Task(title=title, description=description, user=request.user)
            new_task.save()

            return HttpResponse(b"CREATED", status=201)
        return HttpResponseNotFound()
    ```

- Membuat path /todolist/add yang mengarah ke view yang baru dibuat

    Pada file urls.py, di fungsi urlpatterns, saya menambahkan potongan kode berikut:
    ```python 
    path('add/', add_task_ajax, name='add_task_ajax')
    ```

- Menutup modal setelah penambahan task berhasil dilakukan

    Bisa dilihat pada potongan kode html untuk membuat modal yang saya tampilkan di poin pertama bagian AJAX POST, untuk button dengan id btn-submit, saya menambahkan atribut data-bs-dismiss dengan value modal, yang artinya setiap submit dilakukan, maka modal akan tertutup.

- Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page

    Saat tombol submit diklik, program akan memanggil fungsi addTask
    ```javascript
    function addTask() {
        fetch("{% url 'todolist:add_task_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#createTaskForm'))
        }).then(refreshTodolist)
        return false
        }
    ```
    Pada fungsi di atas, program akan mengambil mengambil data yang telah diinput melalui form dan memanggil fungsi refreshTodolist, pada fungsi refreshTodolist inilah halaman utaman akan menampilkan list terbaru tanpa me-reload seluruh page.
