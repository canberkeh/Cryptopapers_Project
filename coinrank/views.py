from django.shortcuts import redirect, render
from .models import CoinRanking
# Create your views here.

def coinrankindex(request):
    coinrank_items = CoinRanking.objects.all()
    return render(request, 'coinrank/coinrank.html', {'coinrank_items': coinrank_items})

# def like_update(request):
#     likes = CoinRanking.objects.all()
#     # likes.like += 1
#     likes.save()
#     context = {'likes': likes}

#     return render(request, 'coinrank/coinrank.html', context)
