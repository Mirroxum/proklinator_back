from rest_framework import serializers

from posts.models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'name',
            'curse',
            'comment',
            'duration',
            'likes',
            'link',
            'created_at',
            'updated_at',
        )
