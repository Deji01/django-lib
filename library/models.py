from django.db import models

# Create your models here.
class User:
    pass


class Book(models.Model):
    title = models.CharField(max_length=255)
    num_pages = models.IntegerField(default=0)
    publish_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    color = models.CharField(max_length=32,  blank=True, null=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self) -> str:
        return self.title