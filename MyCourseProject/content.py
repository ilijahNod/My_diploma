import MyCourseProject.settings
from django.contrib.auth.models import User
from blog.models import Author, Genre, Post
import datetime
from PIL import Image

number_of_entries = 13
'''
list1 = ('Detective', 'Drama', 'Action', 'Horror', 'Humor', 'Romance', 'Science Fiction', 'Thriller', 'Biography', 'Poetry')
for i in list1:
    Genre.objects.create(genre=i)



for author_num in range(number_of_entries):
    ab= User.objects.create(username='Christian%s' % author_num, password='11111111B', email='Christian%s@gmail.com' % author_num, first_name='Christian%s' % author_num, last_name='Surname%s' % author_num);
    ab.save()'''

for post_num in range(number_of_entries):
    ab= Post.objects.create(title='Christian %s story' % post_num, excerpt='Thats a Christian %s story' % post_num, date=datetime.datetime.now(), slug='Christian-%s-story' % post_num, content=(' Thats a Christian %s story' % post_num) * 8, author=Author.objects.get(user=User.objects.get(username='Christian%s' % post_num)), genre=Genre.objects.get(genre='Drama'), tags='Fabulous, great, fantastic')
    ab.save()
    ab.image.save('12%.jpg' % post_num, File() )
