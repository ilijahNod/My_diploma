from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Author, Post, Genre, Comment
from django.contrib.auth.models import User
import datetime


class CommentFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Christian11', password='11111111B', first_name='Christian',
                            last_name='Surname')

        Genre.objects.create(genre='Drama')

        Post.objects.create(title='Christian story',
                            excerpt='Thats a Christian  story',
                            image='uploads/posts/1.jpg',
                            date=datetime.datetime.now(),
                            slug='Christian-story',
                            content=' Thats a Christian  story' * 8,
                            author=Author.objects.get(
                                user=User.objects.get(username='Christian11')),
                            genre=Genre.objects.get(genre='Drama'),
                            tags='Fabulous, Great, fantastic')

    
    def test_comment_form(self):

        data = {'user_name' : User.objects.get(username='Christian11'),
                'text' : 'Its Fabolous and u know it.' ,
                'post' : Post.objects.get(slug='Christian-story'), }
        form = CommentForm(data)
        self.assertTrue(form.is_valid())

