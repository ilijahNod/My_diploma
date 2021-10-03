from django.test import TestCase
import datetime
from django.db import models
from django.contrib.auth.models import User
from blog.models import Author, Genre, Post
from django.urls import reverse


class AllPostsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 posts for tests
        number_of_entries = 13
        Genre.objects.create(genre='Detective')
        Genre.objects.create(genre='Drama')

        for author_num in range(number_of_entries):
            User.objects.create(username='Christian%s' % author_num,
                                password='11111111B',
                                email='Christian%s@gmail.com' % author_num,
                                first_name='Christian%s' % author_num,
                                last_name='Surname%s' % author_num,)

        for post_num in range(number_of_entries):
            Post.objects.create(title='Christian %s story' % post_num,
                                excerpt='Thats a Christian %s story' % post_num,
                                image='uploads/posts/1.jpg',
                                date=datetime.datetime.now(),
                                slug='Christian-%s-story' % post_num,
                                content=(' Thats a Christian %s story' %
                                         post_num) * 8,
                                author=Author.objects.get(user=User.objects.get(
                                    username='Christian%s' % post_num)),
                                genre=Genre.objects.get(genre='Drama'),
                                tags='Fabulous, Great, fantastic')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/posts')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('posts-page'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('posts-page'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, "blog/all-posts.html")

    def test_pagination_is_ten(self):
        resp = self.client.get('/posts')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['all_posts']) == 10)

    def test_lists_all_posts(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get('/posts'+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['all_posts']) == 3)


class AllPostsFilterTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 posts for tests
        number_of_entries = 13
        Genre.objects.create(genre='Detective')
        Genre.objects.create(genre='Drama')

        for author_num in range(number_of_entries):
            User.objects.create(username='Christian%s' % author_num,
                                password='11111111B',
                                email='Christian%s@gmail.com' % author_num,
                                first_name='Christian%s' % author_num,
                                last_name='Surname%s' % author_num,)

        for post_num in range(number_of_entries):
            Post.objects.create(title='Christian %s story' % post_num,
                                excerpt='Thats a Christian %s story' % post_num,
                                image='uploads/posts/1.jpg',
                                date=datetime.datetime.now(),
                                slug='Christian-%s-story' % post_num,
                                content=(' Thats a Christian %s story' %
                                         post_num) * 8,
                                author=Author.objects.get(user=User.objects.get(
                                    username='Christian%s' % post_num)),
                                genre=Genre.objects.get(genre='Drama'),
                                tags='Fabulous, Great, fantastic')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/posts/filter/Drama')
        self.assertEqual(resp.status_code, 200)

    def test_lists_of_posts(self):
        resp = self.client.get('/posts/filter/Drama'+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['all_posts']) == 3)
