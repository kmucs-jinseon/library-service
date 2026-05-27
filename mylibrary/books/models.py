from django.db import models
from django.db.models import QuerySet


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def get_all_books(cls) -> QuerySet['Book']:  # → 리턴 타입 힌트 (1점)
        """
        전체 책 목록 반환
        """
        return cls.objects.all()  # → 동작 코드 (2점)

    @classmethod
    def get_books_by_author(cls, author_name) -> QuerySet['Book']:  # → 파라미터 (1점)
        """
        특정 저자의 책만 반환
        """
        return cls.objects.filter(author__iexact=author_name)  # → 동작 코드 (2점)

    @classmethod
    def get_books_by_title_keyword(cls, keyword) -> QuerySet['Book']:  # → 파라미터 (1점)
        """
        제목에 키워드가 포함된 책 반환 (대소문자 구분 없이)
        """
        return cls.objects.filter(title__icontains=keyword)  # → 동작 코드 (2점)

    @classmethod
    def get_books_ordered_by_title(cls) -> QuerySet['Book']:  # → 리턴 타입 힌트 (1점)
        """
        제목 순으로 정렬된 책 목록 반환
        """
        return cls.objects.all().order_by('title')  # → 동작 코드 (2점)
