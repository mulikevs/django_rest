from rest_framework import serializers
from BlogPost.models import Blog,Comments

class BlogSerializer(serializers.ModelSerializer):
    blogimage = serializers.CharField(allow_blank=True, required=False) 

    class Meta:
        model = Blog
        fields = ['id', 'slug', 'blogtext', 'blogtitle', 'blogtopic', 'blogauthor', 'blogdate', 'bloglikes', 'blogdislikes', 'blogimage'] 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment_id', 'blog', 'comment_text', 'comment_author', 'comment_date']



