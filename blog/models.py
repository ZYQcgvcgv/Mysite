from django.db import models
from django.db.models.fields import exceptions
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from read_statistics.models import ReadNum
from read_statistics.models import ReadNumExpandMethod,ReadDetail
from django.urls import reverse




class BlogType(models.Model):
    type_name=models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    title=models.CharField(max_length=50)
    blog_type=models.ForeignKey(BlogType,on_delete=models.CASCADE,related_name='blog_blog')
    content=RichTextUploadingField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    read_details=GenericRelation(ReadDetail)
    create_time=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)




    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk' : self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog:%s>"%self.title

    class Meta:
        ordering=['-create_time']

'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog=models.OneToOneField(Blog,on_delete=models.DO_NOTHING)'''
