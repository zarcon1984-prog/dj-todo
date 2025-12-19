from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=150)
    done = models.BooleanField(default=False)


    class Meta:
        ordering = ('id',)
        verbose_name = 'ToDO Item'

    def __str__(self)->str:
        return self.title