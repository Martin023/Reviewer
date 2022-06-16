from django import forms
from .models import WebReview


class WebReviewForm(forms.ModelForm):
    class Meta:
        model = WebReview
        fields = ('name','description','screenshot')
