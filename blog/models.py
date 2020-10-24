from django.db import models

# Create your models here.

class Category(models.Model):
    name        = models.CharField(max_length=50,verbose_name='Kategori Kısaltması')
    show_name   = models.CharField(max_length=100,verbose_name='Kategori İsmi')

    def __str__(self):
        return self.name

    class Meta:
        db_table                = 'categories'
        verbose_name            = 'Kategori'
        verbose_name_plural     = 'Kategoriler'


class Post(models.Model):
    slug                = models.SlugField(max_length=250, unique=True,null=True,blank=True)
    title               = models.CharField(max_length=200,verbose_name='Başlık',null=False,blank=False)
    description         = models.CharField(max_length=600)


class Subscribe(models.Model):
    email = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table       = 'subscribe'
        verbose_name = 'Abonelik'
        verbose_name_plural = 'Abonelikler'