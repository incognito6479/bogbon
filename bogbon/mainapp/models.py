# DjangoImports
from django.db import models
# End DjangoImports


class Article(models.Model):
    name = models.CharField(verbose_name='Название на русском', max_length=200)
    name_en = models.CharField(verbose_name='Название на английском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    pub_date = models.DateField(verbose_name='Дата публикации')
    author = models.CharField(verbose_name='Автор на русском', max_length=200)
    author_en = models.CharField(verbose_name='Автор на английском', max_length=200)
    author_uz = models.CharField(verbose_name='Автор на узбекском', max_length=200)
    short_description = models.TextField(verbose_name='Краткое описание на русском')
    short_description_en = models.TextField(verbose_name='Краткое описание на английском')
    short_description_uz = models.TextField(verbose_name='Краткое описание на узбекском')
    img_preview = models.ImageField(verbose_name='Миниатюра (334х234)', upload_to='article_img/')
    img_background = models.ImageField(verbose_name='Фоновое изображение (1920х1080)', upload_to='article_img/')
    img_post = models.ImageField(verbose_name='Изображение в статье (780х500)', upload_to='article_img/')
    text = models.TextField(verbose_name='Текст на русском')
    text_en = models.TextField(verbose_name='Текст на английском')
    text_uz = models.TextField(verbose_name='Текст на узбекском')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'