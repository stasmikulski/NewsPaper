from news.models import *

# 1) Создать двух пользователей
u1 = User.objects.create_user(username='Stanley')
u2 = User.objects.create_user(username='Stayer')
# Создадим еще двух пользователей
u3 = User.objects.create_user(username='Bosch')
u4 = User.objects.create_user(username='Pegeout')
# -- Выведем всех пользователей)
User.objects.all().values('username')
# -- Или любого из них по id
User.objects.get(id=4)

# 2) Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)
# Author.objects.create(authorUser=u3)
# Author.objects.create(authorUser=u4)
# -- Выведем всех авторов
Author.objects.all().values('authorUser')

# 3) Добавить 4 категории в модель Category.
Category.objects.create(name='IT')
Category.objects.create(name='Politics')
Category.objects.create(name='Sport')
Category.objects.create(name='Education')
# -- Выведем все категории
Category.objects.all().values('name')

# 4) Добавить 2 статьи и 1 новость.
author = Author.objects.get(id=1)
Post.objects.create(author=author, categoryType='AR', title='Finishing with IBM', text='Equipments for Multi-event tournament by IBM')
author = Author.objects.get(id=2)
Post.objects.create(author=author, categoryType='AR', title='Big Fishing with Hackers', text='Many many comps in far galaxy was damned by hackers')
Post.objects.create(author=author, categoryType='NW', title='To infinity and beyond!', text='A long time ago, in a galaxy far, far away…')

# 5) Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=4))
# -- Выведем категории
catpost1 = Post.objects.get(id=1).postCategory.all()
catpost1.values('name')
catpost2 = Post.objects.get(id=2).postCategory.all()
catpost2.values('name')

# 6) Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(commentPost=Post.objects.get(id=1),commentUser=Author.objects.get(id=1).authorUser, text='Some text by author')
Comment.objects.create(commentPost=Post.objects.get(id=2),commentUser=Author.objects.get(id=1).authorUser, text='Another text by Big author')
Comment.objects.create(commentPost=Post.objects.get(id=3),commentUser=Author.objects.get(id=2).authorUser, text='Not enough big text by great author')
Comment.objects.create(commentPost=Post.objects.get(id=4),commentUser=Author.objects.get(id=1).authorUser, text='A very small comment from another author')

# 7) Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
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
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).rating

# 8) Обновить рейтинги пользователей.
Author.objects.get(id=1).update_rating()
Author.objects.get(id=1).ratingAuthor
Author.objects.get(id=2).update_rating()
Author.objects.get(id=2).ratingAuthor

# 9) Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
authfirst = Author.objects.order_by('-ratingAuthor')[:1]
authfirst[0].ratingAuthor
# Author.objects.get(id=authfirst).ratingAuthor
#? Узнать почему id=authfirst работает как обычный id=3
# authfirstid = authfirst[0].id
# 3
# Author.objects.get(id=authfirstid).ratingAuthor
authfirst[0].authorUser.username
# Author.objects.get(id=authfirst).authorUser.username
# championid = authfirst[0].authorUser.id
# 3
# Author.objects.get(id=championid).authorUser.username

# 10) Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# -- Если внимательно прочитать, то ищем сначала лучшую статью
postfirst = Post.objects.order_by('-rating')[:1]
# -- Выводим
# Post.objects.get(id=postfirst).dateCreation
Post.objects.get(id=postfirst).dateCreation.strftime("%Y-%m-%d %X")
Post.objects.get(id=postfirst).author.authorUser.username
Post.objects.get(id=postfirst).rating
Post.objects.get(id=postfirst).title
Post.objects.get(id=postfirst).preview()

# 11) Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
# --- Добавим комментарии к посту-чемпиону postfirst
Comment.objects.create(commentPost=Post.objects.get(id=postfirst),commentUser=Author.objects.get(id=2).authorUser, text='Blah-blah-blah - five 555 text by author')
Comment.objects.create(commentPost=Post.objects.get(id=postfirst),commentUser=Author.objects.get(id=3).authorUser, text='Oh, God! 333 letters by 333 writers')
# --- Соберем все комменты к посту-чемпиону postfirst
champ_post_comments = Comment.objects.filter(commentPost=Post.objects.get(id=postfirst))
champ_post_comments_values = champ_post_comments.values('dateCreation', 'commentUser', 'rating', 'text')
# --- Напечатаем их
for i in champ_post_comments_values:
    print(i['dateCreation'].strftime("%Y-%m-%d"),Author.objects.get(id=i['commentUser']).authorUser.username,' Rating:', i['rating'], i['text'])


