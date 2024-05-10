from django.contrib.auth import get_user_model
from django.db import models
from .constans import MAX_LIMIT_SLUG, MAX_LIMIT_CHAR


User = get_user_model()


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follows'
    )

    def __str__(self):
        return self.following


class Group(models.Model):
    title = models.CharField(blank=True, max_length=MAX_LIMIT_CHAR)
    slug = models.SlugField(max_length=MAX_LIMIT_SLUG)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.CharField(max_length=MAX_LIMIT_CHAR)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
