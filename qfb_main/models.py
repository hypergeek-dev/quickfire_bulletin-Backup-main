from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class NewsArticle(models.Model):
    article_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_articles")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    source_id = models.CharField(max_length=255)
    source_priority = models.IntegerField()
    country = models.CharField(max_length=2)
    category = models.CharField(max_length=50)
    language = models.CharField(max_length=2)
    pubDate = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    NewsArticle = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
