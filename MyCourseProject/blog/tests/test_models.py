from django.test import TestCase
from blog.models import Author, Post, Genre
from django.contrib.auth.models import User
import datetime

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Christian11', password='11111111B', first_name='Christian',
             last_name = 'Surname')

    def test_full_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author.full_name()
        self.assertEquals(field_label, author.user.first_name + ' ' + author.user.last_name)


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Christian11', password='11111111B', first_name='Christian',
             last_name = 'Surname')
        
        Genre.objects.create(genre='Drama')

        Post.objects.create(title = 'Christian story',
                                    excerpt = 'Thats a Christian  story',
                                    image = 'uploads/posts/1.jpg',
                                    date = datetime.datetime.now(),
                                    slug = 'Christian-story',
                                    content = ' Thats a Christian  story' * 8,
                                    author = Author.objects.get(user=User.objects.get(username='Christian11')),
                                    genre = Genre.objects.get(genre='Drama'),
                                    tags = 'Fabulous, Great, fantastic')
    
    def test_get_absolute_url(self):
        post=Post.objects.get(slug='Christian-story')
        #This will also fail if the urlconf is not defined.
        self.assertEquals(post.get_absolute_url(),'/posts/Christian-story')
