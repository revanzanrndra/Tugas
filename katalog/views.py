from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    catalog_item_data = CatalogItem.objects.all()
    context = {
        'list_item': catalog_item_data,
        'nama': 'TM Revanza Narendra Pradipta',
        'npm': '2206025003',
    }
    return render(request, "katalog.html", context)