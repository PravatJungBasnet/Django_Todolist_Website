from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.


class task(models.Model):
    priority_choices =[
  (1,'1'),
  (2,'2'),
  (3,'3'),
  (4,'4'),
  (5,'5'),
  (6,'6'),
  (7,'7'),
  (8,'8'),
  (9,'9'),
  (10,'10'),

]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)
    task_priority=models.IntegerField(choices=priority_choices)
    due_date=models.DateTimeField()
    def due_remainder(self):
        now=timezone.now()
        time_difference=self.due_date-now
        return time_difference




    

