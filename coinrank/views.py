from django.shortcuts import redirect, render
from .models import CoinRanking, Comments
from .forms.new_listing_form import CoinrankForm
from .forms.comment_form import AddCommentForm


def coinrankindex(request):
    coinrank_items = CoinRanking.objects.all().order_by('name')
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


def add_comment(request, id):
    comment_form = AddCommentForm
    comments = Comments.objects.filter(coin_name=id)
    if request.method == 'POST':
        coin = CoinRanking.objects.get(id=id)
        comment = Comments(coin_name=coin)
        comment_form = AddCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return render(request, 'coinrank/comments.html', {'coin_id': id, 'comments': comments})
    else:
        comment_form = AddCommentForm()
    return render(request, 'coinrank/add_comment.html', {'add_comment': comment_form})


def delete_coin(request):
    pass


# Coinrank like counter, dislike counter, hodler counter. Includes total point calc.
def like_counter(request, id):
    like_counter = CoinRanking.objects.get(id=id)
    like_counter.like += 1
    like_counter.total_points = like_counter.like - like_counter.dislike
    like_counter.save()
    return redirect('/coinrank')


def dislike_counter(request, id):
    dislike_counter = CoinRanking.objects.get(id=id)
    dislike_counter.dislike += 1
    dislike_counter.total_points = dislike_counter.like - dislike_counter.dislike
    dislike_counter.save()
    return redirect('/coinrank')


def hodler_counter(request, id):
    hodler_counter = CoinRanking.objects.get(id=id)
    hodler_counter.hodl += 1
    hodler_counter.save()
    return redirect('/coinrank')


# Comments, comments like counter and comment dislike counter
def comments(request, coin_id):
    comments = Comments.objects.filter(coin_name=coin_id).order_by('-like')
    return render(request, 'coinrank/comments.html', {'coin_id': coin_id, 'comments': comments})


def comment_like_counter(request, id):
    comment = Comments.objects.get(id=id)
    comment.like += 1
    comment.save()
    return redirect(request.META['HTTP_REFERER'])


def comment_dislike_counter(request, id):
    comment_dislike_counter = Comments.objects.get(id=id)
    comment_dislike_counter.dislike += 1
    comment_dislike_counter.save()
    return redirect(request.META['HTTP_REFERER'])



