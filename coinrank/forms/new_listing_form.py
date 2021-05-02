from django import forms
from coinrank.models import CoinRanking

class CoinrankForm(forms.ModelForm):
    class Meta:
        model = CoinRanking
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name Here' }),
        }
        exclude = ['is_approved', 'like', 'dislike', 'hodl', 'total_points', 'comment']