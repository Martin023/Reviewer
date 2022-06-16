from django import forms
from .models import WebReview
from cloudinary.forms import CloudinaryFileField


class WebReviewForm(forms.ModelForm):
    class Meta:
        model = WebReview
        fields = ('name','description','screenshot')
