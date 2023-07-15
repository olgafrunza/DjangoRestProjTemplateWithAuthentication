from rest_framework import serializers
from .models import (
    Blog,
    Comment,
    Like,
)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "commentor",
            "created",
            "content",
            "blog",

        )

class BlogSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()

    comments = CommentSerializer(many=True, read_only=True) 
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "created",
            "updated",
            "content",
            "image",
            "slug",
            "status",
            "category",
            "author",
            "view_count",
            "like_count",
            "comment_count",
            "comments",
            "is_owner",
            "has_liked",
        )

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
        return False   

    def get_has_liked(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            if Like.objects.filter(liker = request.user, blog=obj).exists(): 
                return True
        return False   
    
