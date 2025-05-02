from rest_framework import serializers
from books.models import Book, Category


class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all(),
        allow_null=True,
    )

    class Meta:
        model = Book
        fields = ['book_id', 'title', 'subtitle', 'category', 'expense',
                  'authors', 'publisher', 'published_date']

    def validate_category(self, value):
        if not value or value == 'default':
            return None
        try:
            value = Category.objects.get(name=value)
        except Category.DoesNotExist:
            value = Category.objects.create(name=value)

        return value

    def validate_id(self, value):
        return int(value)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class BookBulkCreate(serializers.ListSerializer):
    child = BookSerializer()

    def validate(self, data):
        if not isinstance(data, list):
            raise serializers.ValidationError("Data must be a list of books.")
        return super().validate(data)

    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)
