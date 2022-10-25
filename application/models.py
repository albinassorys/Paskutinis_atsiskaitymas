from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField('Name', max_length=50, default=f'Category + {id}')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Notes(models.Model):

    title = models.CharField('Title', max_length=50, null=False, blank=False,
                              help_text='Choose note title', default= f'Note + {id}')

    body = models.TextField('Text', max_length=500, help_text='Enter text', editable=True, null=False)

    image = models.ImageField('Image', upload_to='', null=True, help_text='Upload an optional image')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Date', auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.date} {self.user}'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
