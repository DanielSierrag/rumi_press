from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .serializers import BookBulkCreate, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework import status


class BulkBookCreateView(CreateAPIView):
    """
    View to create multiple books at once.
    """
    serializer_class = BookBulkCreate
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     if isinstance(self.request.data, list):
    #         serializer = self.get_serializer(data=request.data, many=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryCreateAPIView(CreateAPIView):
    """
    View to create a category.
    """
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return redirect(reverse_lazy('books:book_create'))
