from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(WebReview),
admin.site.register(Rating),
admin.site.register(Category)