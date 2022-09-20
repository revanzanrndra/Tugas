import json

# Fungsi untuk mengembalikan pesan "Selamat, kamu sudah banyak menonton!" jika banyak sudah nonton >= belum nonton
# dan mengembalikan pesan "Wah, kamu masih sedikit menonton!" jika banyak sudah nonton < belum nonton
def return_message():
    numbers_of_yes = 0
    numbers_of_no = 0

    dir  = "mywatchlist\\fixtures\\initial_mywatchlist_data.json"
    open_data = open(dir)

    data = json.load(open_data)

    open_data.close()

    for i in data:
        watched = i.get('fields').get('watched')
        if watched == 'Yes':
            numbers_of_yes += 1
        else:
            numbers_of_no += 1
    
    if numbers_of_yes >= numbers_of_no:
        return "Selamat, kamu sudah banyak menonton!"
    
    return "Wah, kamu masih sedikit menonton!"
