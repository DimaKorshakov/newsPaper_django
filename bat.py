python manage.py makemigrations
python manage.py migrate

from news.models import *
user1 = User.objects.create(username='Mike', first_name='Frank')
Author.objects.create(authorUser=user1)
user2 = User.objects.create(username='Semon', first_name='Ber')
Author.objects.create(authorUser=user2)
Category.objects.create(name='IT')
Category.objects.create(name='Education')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Mike')),categoryType='NW', title='smth title', text='smth text')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Mike')),categoryType='AR', title='smth title222', text='2222smth text')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Semon')),categoryType='AR', title='smth title22', text='222smth text')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Mike')),categoryType='AR', title='smth title22', text='222smth text')
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Education')
p1.postCategory.add(c1)
p3.postCategory.add(c2)
Comment.objects.create(commentUser=User.objects.get(username='Mike'), commentPost= Post.objects.get(pk=1), text='comment text1')
Comment.objects.create(commentUser=User.objects.get(username='Mike'), commentPost= Post.objects.get(pk=2), text='comment text1')
Comment.objects.create(commentUser=User.objects.get(username='Semon'), commentPost= Post.objects.get(pk=3), text='comment32323232 text1')

Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=2).like()

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).dislike()

Author.objects.get(authorUser=User.objects.get(username='Mike')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Semon')).update_rating()

a = Author.objects.get(authorUser=User.objects.get(username='Semon'))

Author.objects.get(authorUser=User.objects.get(username='Mike')).ratingAuthor

best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]

allComment = Comment.objects.all().values('dateCreation', 'commentUser', 'rating', 'text')

best_posteUser = Post.objects.all().order_by('-rating').values('dateCreation', 'author', 'rating', 'title', 'text')[0]

print(best_posteUser)





