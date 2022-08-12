from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class Author(models.Model):
    first_name = models.CharField(max_length=128, blank=True)
    middle_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self) -> str:
        last_name = self.last_name
        first_name = self.first_name
        if self.first_name == "":
            return f"{last_name}"
        else:
            return f"{last_name}, {first_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    num_pages = models.PositiveIntegerField(blank=True)
    publish_date = models.DateField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=25, blank=True)
    color = models.CharField(max_length=32,  blank=True)
    isbn13 = models.CharField(max_length=13, blank=True)
    author = models.ManyToManyField(Author)

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self) -> str:
        return self.title