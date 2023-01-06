from books.models import Book
from books.serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class BookListView(APIView):
    
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data}) #TODO: add additional jsonfield for count
