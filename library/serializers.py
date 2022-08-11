from rest_framework import serializers
from library.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "title",
            "num_pages",
            "publish_date",
            "price",
            "color",
            "isbn13",
        ]