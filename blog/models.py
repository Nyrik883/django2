from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    descriptions = models.TextField()
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='img')
    public = models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super().save(*args,**kwargs)
    

    def __str__(self):
        return self.title