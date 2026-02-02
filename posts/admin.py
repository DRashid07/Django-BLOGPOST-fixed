from django.contrib import admin

from .models import Author, Category, Post, Like, Favourite, Comment, Tag, About, Book

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Favourite)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Book)