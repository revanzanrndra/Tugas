from django.shortcuts import render
from mywatchlist.models import MovieWatchlist
from mywatchlist.message import return_message
from django.http import HttpResponse
from django.core import serializers

def returnData():
    return MovieWatchlist.objects

# Create your views here.
def show_watchlist(request):
    data_movie_watchlist = returnData().all()
    context = {
        'list_movie': data_movie_watchlist,
        'nama': 'Tm Revanza Narendra Pradipta',
        'npm': '2206025003',
        'message': return_message, # Mengembalikan pesan sesuai dengan jumlah film yang sudah ditonton
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = returnData().all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = returnData().filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = returnData().all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = returnData().filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
