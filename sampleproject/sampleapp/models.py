from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    def __str__(self):
        return self.name
class members(models.Model):
    name1=models.CharField(max_length=250)
    image1=models.ImageField(upload_to='picture')
    desc = models.CharField(max_length=300)

