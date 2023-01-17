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

    def __str__(self) -> str:
        return str(self.title)


class IssuedBook(models.Model):
    student_name =  models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)
    title = models.CharField("book_title", max_length=100)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.title)
