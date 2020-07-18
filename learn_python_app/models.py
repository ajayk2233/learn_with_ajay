from django.db import models
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    title_detail = models.CharField(max_length=100,null=True,blank=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title