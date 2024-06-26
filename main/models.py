from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to="books")
    
    def __str__(self):
        return str(self.title)

