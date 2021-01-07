from django.contrib import admin
from .models import Story, Poem, Article, Favourite

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    ordering = ['id']


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    ordering = ['id']


@admin.register(Article)
class ArticeAdmin(admin.ModelAdmin):
    ordering = ['id']


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    ordering = ['id']

