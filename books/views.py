from books.models import Book, IssuedBook
from books.serializers import BookSerializer, IssuedBookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookListView(APIView):
    
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data}) #TODO: add additional jsonfield for count

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditBookView(APIView):
    def patch(self, request, format=None):
        try:
            resource =  Book.objects.get(id=request.data.get("id"))
        except Book.DoesNotExist:
            return Response({"error" : "Book id not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer =  BookSerializer(resource, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteBookView(APIView):
    def delete(self, request, pk=None):
        try:
            resource = Book.objects.get(pk=pk)
            resource.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)


class IssuedBookView(APIView):
    def get(self, request, format=None):
        issued_books = IssuedBook.objects.all()
        serializer = IssuedBookSerializer(issued_books, many=True)
        return Response({"books": serializer.data}) #TODO: add additional jsonfield for count

    def post(self, request, format=None):
        serializer = IssuedBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



