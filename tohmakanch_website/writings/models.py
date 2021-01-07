from django.db import models

class Writing(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    
    class Meta:
        db_table='writing'

    def __str__(self):
        return self.title

class Story(Writing):

    class Meta:
        db_table='story'


class Poem(Writing):

    class Meta:
        db_table='poem'


class Article(Writing):

    class Meta:
        db_table='article'


class Favourite(models.Model):
    writing = models.ForeignKey(Writing, on_delete=models.CASCADE)

    class Meta:
        db_table='favourite'

    def __str__(self):
        return self.writing.title