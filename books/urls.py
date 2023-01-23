from django.urls import path
from .views import BookListView, IssuedBookView, EditBookView

urlpatterns = [
    path('book-list/', BookListView.as_view()),
    path('issue-book/', IssuedBookView.as_view()),
    path('edit-book/', EditBookView.as_view() )
]


