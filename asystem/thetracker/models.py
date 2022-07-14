from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Job(models.Model):
    order_num = models.CharField(max_length=275)
    SKU = models.CharField(max_length=275)
    num_items = models.IntegerField()
    num_stones = models.IntegerField()
    description_text = models.TextField()
    creator_name = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.order_num + ' | ' + str(self.creator_name) + ' | ' + str(self.created)
    
    def get_absolute_url(self):
        return reverse('add-job')

    @property
    def calculate_total_amt(self):
        amt = 0.50
        num_stones = self.num_stones * amt
        return num_stones
   

class Memo(models.Model):
    name = models.CharField(max_length=275)
    email = models.EmailField(max_length=275)
    date_set = models.DateField(auto_now_add=True)
    job = models.ForeignKey(Job, blank=True, null=True, related_name='memos',on_delete=models.CASCADE)

    def get_absolute_url(self):
       
        return reverse('home')
        # return reverse('job-detail', args=(str(self.id)))
    
   


   
# https://www.youtube.com/watch?v=FzV_Py68Y_I&t=969s&ab_channel=Codemy.com