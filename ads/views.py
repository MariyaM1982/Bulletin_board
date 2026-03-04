from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Ad, Review
from .permissions import IsOwnerOrReadOnly, IsReviewAuthorOrReadOnly
from .serializers import AdListSerializer, AdSerializer, ReviewSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.select_related("author").all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["^title"]
    filterset_fields = ["author"]

    def get_serializer_class(self):
        if self.action == "list":
            return AdListSerializer
        return AdSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["get"], permission_classes=[permissions.AllowAny])
    def reviews(self, request, pk=None):
        ad = self.get_object()
        reviews = ad.reviews.select_related("author").all()
        page = self.paginate_queryset(reviews)
        if page is not None:
            serializer = ReviewSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)
        serializer = ReviewSerializer(reviews, many=True, context={"request": request})
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsReviewAuthorOrReadOnly()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
