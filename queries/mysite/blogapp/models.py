from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    bio = models.TextField(null=False, blank=True, db_index=True)


class Category(models.Model):
    name = models.CharField(max_length=40, db_index=True)


class Tag(models.Model):
    name = models.CharField(max_length=20, db_index=True)


class Article(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(null=False, blank=True, db_index=True)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)