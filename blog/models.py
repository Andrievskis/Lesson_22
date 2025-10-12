from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = models.CharField(max_length=1000, verbose_name='содержимое')
    image = models.ImageField(upload_to='images/blog/', null=True, blank=True, verbose_name='изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'заметка блога'
        verbose_name_plural = 'заметки блога'
        ordering = ['created_at']
