from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CommentSerializer,
    BlogSerializer,
)
from .models import (
    Blog,
    Comment,
    PostViewRecords,
    Like,
)
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrStaffOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response


class BlogViewset(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(status='p')
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



    def get_object(self):
        obj = super().get_object() 
        # if self.request.user.is_authenticated():
        PostViewRecords.objects.create(viewer=self.request.user, blog=obj)
        return obj

class CommentView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(commentor=self.request.user)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
     obj = Blog.objects.get(slug = slug)
     like_qs = Like.objects.filter(liker = self.request.user, blog=obj)
     if like_qs.exists():
         like_qs[0].delete()
     else:
         Like.objects.create(liker = self.request.user, blog=obj)

         data= {
             "message": "Like process done"
         }
         return Response(data)
