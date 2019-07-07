from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Author(models.Model):
    alias = models.CharField(max_length=12, unique=True, verbose_name="Alias")
    name = models.CharField(max_length=30, verbose_name="Nombre")
    photo = models.ImageField(blank=True, null=True, upload_to="authors", verbose_name= 'Foto')

    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Fecha de Creación")
    modified = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Última Modificación")

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    slug = models.SlugField(unique=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Fecha de Creación")
    modified = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Última Modificación")

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    slug = models.SlugField(unique=True)

    STATUS_CHOICES = (
        ('D', 'draft'),
        ('P', 'published')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='B', verbose_name="Estado")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField(blank=True, verbose_name="Contenido")

    image = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name="Imagen Destacada")
    image_450 = ImageSpecField(source='image',
                                processors=[ResizeToFill(450,450)],
                                format='JPEG',
                                options={'quality':60},
                                )

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Fecha de Creación")
    modified = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Última Modificación")

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.title

    def categoryName(self):
        try:
            return self.category.name
        except:
            return 'undefined'

    def authorName(self):
        try:
            return self.author.name
        except:
            return 'undefined'
