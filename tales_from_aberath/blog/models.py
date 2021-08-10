from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    permalink = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    content = models.TextField(max_length=20000)
    tags = models.JSONField()

    def __repr__(self):
        return f'<BlogPost {self.title}>'