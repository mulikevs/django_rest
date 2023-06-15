from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=255,unique=True)
    blogtext = models.TextField()
    blogtitle = models.CharField(max_length=255)
    blogtopic = models.CharField(max_length=255)
    blogauthor = models.CharField(max_length=255)
    blogdate = models.DateTimeField()
    bloglikes = models.IntegerField(default=0)
    blogdislikes = models.IntegerField(default=0)
    blogimage = models.TextField(blank=True, null=True)  # Add the blogimage field

    class Meta:
        ordering = ['-blogdate']

    def __str__(self):
        return self.blogtitle
    

class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_author = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_author} on {self.blog.blogtitle}"