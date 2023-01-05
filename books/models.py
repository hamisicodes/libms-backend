from django.db import models

# Create your models here.
class Book(models.Model):
    BOOK_CATEGORY = (
        ("Novel", "Novel"),
        ("Revision", "Revision Book"),
        ("Course", "Course Work")
    )

    title =  models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    amount = models.IntegerField()
    book_category = models.CharField(
        choices=BOOK_CATEGORY,
        max_length=100,
        verbose_name="book_category"
    )