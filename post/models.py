from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=120, verbose_name='adınız')
    surname = models.CharField(max_length=120,verbose_name='Soyadınız')
    recorded_date  = models.DateTimeField(verbose_name='Kayıt Tarihi', auto_now_add=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'id':self.id})

        #return "/post/{}".fomat(self.id)

    def get_create_url(self):
        return reverse('post:detail')

    def get_update_url(self):
        return reverse('post:detail',kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('post:detail',kwargs={'id':self.id})

    class Meta:
        ordering = ['-recorded_date','id']
