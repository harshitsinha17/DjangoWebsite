from django.db import models

# Create your models here.
class Members(models.Model):
    id = models.CharField(max_length = 100, primary_key=True)
    img = models.ImageField(upload_to = 'pics')
    name  = models.TextField(max_length = 100)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name
