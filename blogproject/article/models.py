from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
   
    date = models.DateTimeField(auto_now_add=True)
    slug= models.SlugField()
    thumbnail=models.ImageField(null=True,blank=True)
   
    def __str__(self):
        return self.title

    def getBodySlice(self):
        return self.body[:500] + "...."
