from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.


class task(models.Model):
  priority_choices =[
  ('Low','Low'),
  ('Medium','Medium'),
  ('High','High'),
  
  

]
  status_choices=[
    ('Pause','Pause'),
    ('In progress','in Progress'),
    ('Complete','Complete'),
  ]
  
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  title=models.CharField(max_length=100)
  description=models.TextField()
  complete=models.BooleanField(default=False)
  create=models.DateTimeField(auto_now_add=True)
  task_priority=models.CharField(choices=priority_choices,max_length=30)
  due_date=models.DateTimeField()
  status=models.CharField(choices=status_choices,max_length=50)
  def due_remainder(self):
        now=timezone.now()
        time_difference=self.due_date-now
        return time_difference




    

