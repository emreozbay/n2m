from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):

    name = models.CharField(max_length=120, verbose_name='adınız')
    surname = models.CharField(max_length=120,verbose_name='Soyadınız')
    recorded_date = models.DateTimeField(verbose_name='Kayıt Tarihi', auto_now_add=True)
    department =models.ForeignKey("Department", verbose_name='departman')

    def __unicode__(self):
        return "{0} {1}".format(self.name,self.surname)

    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'id':self.id})

        #return "/post/{}".fomat(self.id)

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update',kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('post:delete',kwargs={'id':self.id})

    class Meta:
        ordering = ['-recorded_date','id']

class Department(models.Model):

    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name







