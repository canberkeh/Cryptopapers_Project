from django.shortcuts import redirect, render
from .models import CoinRanking
from .forms.new_listing_form import CoinrankForm


def coinrankindex(request):
    coinrank_items = CoinRanking.objects.all()
    return render(request, 'coinrank/coinrank.html', {'coinrank_items': coinrank_items})


def create_new_coin(request):
    form = CoinrankForm
    if request.method == 'POST':
        form = CoinrankForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
            return redirect('/coinrank')
    else:
        form = CoinrankForm()
    return render(request, 'coinrank/create_new_coin.html', {'create_new_coin': form })

def delete_coin(request):
    pass

# def get(self, request, *args, **kwargs):
#     photo = Photos.objects.get(pk=value)
#     photo.likes_count += 1
#     photo.save()
#     return JsonResponse({'action': 'success'}, safe=False)
# #  list = ToDoList(user=request.user)
#         form = ToDoListForm(request.POST, instance=list)

###############################################################333
# def like_update(request):
#     likes = CoinRanking.objects.all()
#     # likes.like += 1
#     likes.save()
#     context = {'likes': likes}

#     return render(request, 'coinrank/coinrank.html', context)

