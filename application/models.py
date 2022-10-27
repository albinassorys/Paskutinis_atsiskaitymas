from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Category(models.Model):

    name = models.CharField('Name', max_length=20, blank=False, null=False, help_text='Choose category name',
                            default=f'Category')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Notes(models.Model):

    title = models.CharField('Title', max_length=20, null=False, blank=False,
                              help_text='Choose note title', default=f'Note')

    body = models.TextField('Text', max_length=500, help_text='Enter text', editable=True, null=False)

    image = models.ImageField('Image', upload_to='', null=True, blank=True, help_text='Upload an optional image')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Date', auto_now_add=True)

    ordering = ['date']

    def __str__(self):
        return f'{self.category} {self.title} {self.date} {self.user}'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def get_absolute_url(self):
        return reverse('note', args=[str(self.id)])
