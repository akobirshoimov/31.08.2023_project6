from django.shortcuts import render,get_object_or_404
from .models import ErkaklarKiyimi,AyollarKiyimi
from django.http import JsonResponse

# Create your views here.
def all(request):
    all = AyollarKiyimi.objects.all()
    result = []
    for i in all:
        result.append({
            'name':i.name,
            'rangi':i.colour,
            'narhi':i.price
        })
    return JsonResponse(result,safe = False)

def detail(request,detail_id):
    each = ErkaklarKiyimi.objects.get(id=detail_id)
    each = get_object_or_404(ErkaklarKiyimi,id =detail_id)
    info = f'kiym nomi:{ErkaklarKiyimi.name},rangi:{ErkaklarKiyimi.colour}'
    return JsonResponse(info)

