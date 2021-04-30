from django import forms
from coinrank.models import CoinRanking

class CoinrankForm(forms.ModelForm):
    class Meta:
        model = CoinRanking
        exclude = ['is_approved', 'like', 'dislike', 'hodl', 'total_points', 'comment']