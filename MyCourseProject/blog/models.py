
from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from taggit.managers import TaggableManager


class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, default='', on_delete=CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Author.objects.create(user=instance)
        instance.author.save()

    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.full_name()

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Genre(models.Model):
    genre = models.CharField(max_length=150, unique=True, default='Fiction')

    def __str__(self):
        return self.genre


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail-page', kwargs={'slug': self.slug})


class Comment(models.Model):
    user_name = ForeignKey(User, on_delete=models.SET_NULL,
                           null=True, related_name="posts")
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True, null=True)
