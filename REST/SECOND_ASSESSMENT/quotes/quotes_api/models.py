from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Quote(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='quotes')
    quote = models.CharField(max_length=100)
    context = models.CharField(max_length=50, null=True, blank=True)
    source = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.context}'
