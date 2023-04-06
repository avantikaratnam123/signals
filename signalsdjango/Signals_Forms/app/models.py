from django.db import models
from django.db.models.signals import  post_save,pre_delete
from django.dispatch import receiver

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
         return self.name

@receiver(post_save,sender = MyModel)
def mymodel_post_save(sender,instance, **kwargs):
        print('AMyModel instance was saved.')

    
@receiver(pre_delete,sender = MyModel)
def mymodel_pre_delete(sender,instance, **kwargs):
        print('A MyModel instance is about to be deleted.')
  
  

    