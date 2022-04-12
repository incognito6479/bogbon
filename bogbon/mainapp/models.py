from django.db import models


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


class Category(models.Model):
    name_ru = models.CharField(verbose_name='Название категории на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название категории на узбекском', max_length=200)
    name_en = models.CharField(verbose_name='Название категории на английском', max_length=200)
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('mainapp.Category', on_delete=models.PROTECT, verbose_name='Категория продукта',
                                blank=True, null=True, related_name='product')
    title_ru = models.CharField(verbose_name="Название продукта на русском", max_length=255)
    title_uz = models.CharField(verbose_name="Название продукта на узбекском", max_length=255)
    title_en = models.CharField(verbose_name="Название продукта на английском", max_length=255)
    subtitle_en = models.CharField(verbose_name="Подзаголовок на английском", max_length=500)
    subtitle_ru = models.CharField(verbose_name="Подзаголовок на русском", max_length=500)
    subtitle_uz = models.CharField(verbose_name="Подзаголовок на узбекском", max_length=500)
    price = models.FloatField(verbose_name='Цена продукта')
    show_price = models.FloatField(verbose_name='Показательная цена', blank=True, null=True)
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')
    img_hover = models.ImageField(verbose_name='Основное фото', upload_to='products/', blank=True, null=True)
    img_preview = models.ImageField(verbose_name='Фото при наведении', upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductPhoto(models.Model):
    product = models.ForeignKey('mainapp.Product', on_delete=models.PROTECT, verbose_name='Товар')
    photo = models.ImageField(verbose_name='Фото продукта', upload_to='products/')

    def __str__(self):
        return f"{self.product} | {self.photo}"

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продукта'
