from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length= 30)


    def __str__(self):
        return self.name

    
    def save_category(self):
        self.save()

class Rating(models.Model):
    number = models.CharField(max_length= 30)


    def __str__(self):
        return self.number

    
    def save_rating(self):
        self.save()


class WebReview(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    screenshot = CloudinaryField()
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.Choices('web',on_delete=models.DO_NOTHING )
    rating = models.ForeignKey(Rating,on_delete=models.DO_NOTHING)
    slug = models.SlugField()

    def __str__(self):
        return self.name

     
    def save_site(self):
        self.save()

    def delete_site(self):
        self.delete()

    def update_site(self,name,description,category,screenshot):
        self.name=name,
        self.description=description,
        self.category=category,
        self.screenshot=screenshot
        
        self.save()

    @classmethod
    def display_site(cls):
        site=cls.objects.all()
        return site

    @classmethod
    def search_by_cat(cls,search_term):
        site = cls.objects.filter(category__name__icontains=search_term)
        return site


    @classmethod
    def search_by_slug(cls,slug):
        site = cls.objects.get(slug=slug)
        return site
