from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Autor (models.Model):
    autorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    autorRating = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.autorUser)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        postRating = 0
        postRating += postRat.get('postRating')

        commentRat = self.autorUser.comment_set.aggregate(commentRating=Sum('rating'))
        commentRating=0
        commentRating += commentRat.get('commentRating')

        self.autorRating = postRating * 3 + commentRating
        self.save()

class Category (models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Post (models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),

    )

    categoryTypes = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.title)



    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()



    def preview(self):
        return f'{self.text[0:123]}...'



class PostCategory (models.Model):
    postTrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryTrough = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentPost = models.ForeignKey(Category, on_delete=models.CASCADE)

    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()



