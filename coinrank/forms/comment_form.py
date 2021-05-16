from django import forms
from django.forms import widgets
from coinrank.models import Comments

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Add Comment Here'}),
        }
        exclude = ['like', 'dislike', 'create_date', 'coin_name']