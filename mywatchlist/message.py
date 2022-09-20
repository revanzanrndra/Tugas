import json
from mywatchlist.models import MovieWatchlist

# Fungsi untuk mengembalikan pesan "Selamat, kamu sudah banyak menonton!" jika banyak sudah nonton >= belum nonton
# dan mengembalikan pesan "Wah, kamu masih sedikit menonton!" jika banyak sudah nonton < belum nonton
def return_message():
    numbers_of_yes = 0
    numbers_of_no = 0

    data = MovieWatchlist.objects.all()

    for i in data:
        ditonton = i.watched
        if ditonton == 'Yes':
            numbers_of_yes += 1
        else:
            numbers_of_no += 1
    
    if numbers_of_yes >= numbers_of_no:
        return "Selamat, kamu sudah banyak menonton!"
    
    return "Wah, kamu masih sedikit menonton!"