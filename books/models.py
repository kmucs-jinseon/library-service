"""
=================================================================
[과제 5] books/models.py
클래스메서드와 함수 리턴타입을 이용한 간단한 책 대여 서비스
=================================================================

📌 작성 안내
- 이 파일은 빈칸을 채워 완성하는 스켈러튼 코드입니다.
- 각 메서드의 ▼ TODO 주석을 따라 코드를 작성하세요.
- TODO 옆 (n점) 은 배점입니다.

📊 [문제 1] 배점: 총 12점
   - 리턴 타입 힌트 4개 × 1점 = 4점
   - 동작 코드 4개 × 2점 = 8점

📌 힌트 — 이미 import 된 것
   - models.Model
   - QuerySet (from django.db.models import QuerySet)

⚠️ 빈칸 표시
   - "_____" 5개 짜리 밑줄 → 매개변수 이름 등 식별자가 들어갈 자리
   - "return None  # ← 이 줄을 교체" → 올바른 return 문으로 교체
   - "# ▼ TODO" 주석 → 그 자리에 코드 작성 또는 시그니처 수정
"""

from django.db import models
from django.db.models import QuerySet


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"

    # ──────────────────────────────────────────────────────────────
    # [1-1] 전체 책 목록 반환
    # ──────────────────────────────────────────────────────────────
    @classmethod
    def get_all_books(cls):
        # ▼ TODO 1-1-① (1점): 위 함수 시그니처에 리턴 타입 힌트를 추가하세요.
        #     형식:   def get_all_books(cls) -> ___타입힌트___:
        #     힌트:   파일 상단에서 import 한 QuerySet 을 사용. 'Book' 은 forward reference
        """
        전체 책 목록 반환
        """
        # ▼ TODO 1-1-② (2점): 모든 Book 객체를 반환하세요.
        #     힌트:   cls.objects.____()
        return None  # ← 이 줄을 올바른 return 문으로 교체

    # ──────────────────────────────────────────────────────────────
    # [1-2] 특정 저자의 책만 반환 (대소문자 구분 없는 정확 일치)
    # ──────────────────────────────────────────────────────────────
    @classmethod
    def get_books_by_author(cls, _____) -> QuerySet['Book']:
        # ▲ TODO 1-2-① (1점): 위 시그니처의 _____ 자리에 매개변수 이름을 작성하세요.
        #     힌트: 본문에서 사용하는 변수명과 일치해야 합니다 (= 우변 참조).
        """
        특정 저자의 책만 반환 (대소문자 구분 없이 정확 일치)
        """
        # ▼ TODO 1-2-② (2점): author 필드를 대소문자 구분 없이 정확 일치로 필터링하세요.
        #     힌트:   return cls.objects.filter(author______=author_name)
        #     참고:   __iexact 는 'i' + 'exact' = 대소문자 무시(insensitive) + 정확 일치
        return None  # ← 이 줄을 올바른 return 문으로 교체

    # ──────────────────────────────────────────────────────────────
    # [1-3] 제목에 키워드가 포함된 책 반환 (대소문자 구분 없는 부분 일치)
    # ──────────────────────────────────────────────────────────────
    @classmethod
    def get_books_by_title_keyword(cls, _____) -> QuerySet['Book']:
        # ▲ TODO 1-3-① (1점): 위 시그니처의 _____ 자리에 매개변수 이름을 작성하세요.
        """
        제목에 키워드가 포함된 책 반환 (대소문자 구분 없이)
        """
        # ▼ TODO 1-3-② (2점): title 필드에 키워드가 포함되는지 대소문자 구분 없이 필터링.
        #     힌트:   return cls.objects.filter(title__________=keyword)
        #     참고:   __icontains 는 'i' + 'contains' = 대소문자 무시 + 부분 일치
        return None  # ← 이 줄을 올바른 return 문으로 교체

    # ──────────────────────────────────────────────────────────────
    # [1-4] 제목 순으로 정렬된 책 목록 반환
    # ──────────────────────────────────────────────────────────────
    @classmethod
    def get_books_ordered_by_title(cls):
        # ▼ TODO 1-4-① (1점): 위 함수 시그니처에 리턴 타입 힌트를 추가하세요.
        """
        제목 순으로 정렬된 책 목록 반환
        """
        # ▼ TODO 1-4-② (2점): 모든 책을 가져온 뒤 'title' 기준으로 오름차순 정렬하세요.
        #     힌트:   return cls.objects.all().________('title')
        #     참고:   내림차순은 '-title' 처럼 - 부호를 붙임
        return None  # ← 이 줄을 올바른 return 문으로 교체
