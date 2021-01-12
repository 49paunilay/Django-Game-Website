from django.db import models

# Create your models here.
class Catagory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Images(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    url = models.URLField(max_length=200,default="http://www.google.com")
    added_date = models.DateTimeField()
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
