from news.models import *
u1 = User.objects.create_user(username='Stayer')
u2 = User.objects.create_user(username='Stanley')
u3 = User.objects.create_user(username='Bosch')
Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)
Author.objects.create(authorUser=u3)
Category.objects.create(name='IT')
Category.objects.create(name='Politics')
Category.objects.create(name='Sport')
Category.objects.create(name='Education')
author = Author.objects.get(id=1)
Post.objects.create(author=author, categoryType='AR', title='Finishing with IBM', text='Equipments for Multi-event tournament by IBM')
author = Author.objects.get(id=2)
Post.objects.create(author=author, categoryType='AR', title='Big Fishing with Hackers', text='Many many comps in far galaxy was damned by hackers')
Post.objects.create(author=author, categoryType='NW', title='To infinity and beyond!', text='A long time ago, in a galaxy far, far away…')
Comment.objects.create(commentPost=Post.objects.get(id=1),commentUser=Author.objects.get(id=1).authorUser, text='Some text by author')
Comment.objects.create(commentPost=Post.objects.get(id=2),commentUser=Author.objects.get(id=1).authorUser, text='Another text by Big author')
Comment.objects.create(commentPost=Post.objects.get(id=3),commentUser=Author.objects.get(id=2).authorUser, text='Not enough big text by great author')
Comment.objects.create(commentPost=Post.objects.get(id=4),commentUser=Author.objects.get(id=1).authorUser, text='A very small comment from another author')
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).rating
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).rating
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).rating
Comment.objects.get(id=4).dislike()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=3).rating
Post.objects.get(id=1).like()
Post.objects.get(id=1).rating
Post.objects.get(id=2).like()
Post.objects.get(id=2).rating


authfirst = Author.objects.order_by('-ratingAuthor')[:1]
authfirst[0].ratingAuthor
authfirst[0].authorUser.username

Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Author.objects.get(id=1).update_rating()
Author.objects.get(id=1).ratingAuthor
Author.objects.get(id=2).update_rating()
Author.objects.get(id=2).ratingAuthor

authfirst = Author.objects.order_by('-ratingAuthor')[:1]
authfirst[0].ratingAuthor
authfirst[0].authorUser.username
champion = authfirst[0].authorUser.id
Post.objects.get(id=champion).dateCreation
Post.objects.get(id=champion).author.authorUser.username
Post.objects.get(id=champion).rating
Post.objects.get(id=champion).title
Post.objects.get(id=champion).preview()



