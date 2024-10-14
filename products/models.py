from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    manufactured_date = models.DateField()

    def __str__(self):
        return self.title

