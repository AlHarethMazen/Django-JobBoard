from django.db import models


# Create your models here.
JOB_TYPES= (('Full Time','Full Time'),
            ('Part Time','Part Time'))
class job(models.Model):
   title = models.CharField(max_length=100)
   type = models.CharField(max_length=15,choices=JOB_TYPES)
   description = models.TextField(max_length=1000)
   published_at = models.DateTimeField(auto_now=True)
   Vacancy = models.IntegerField(default=1)
   Salary = models.IntegerField(default=0)
   experience = models.IntegerField(default=0)

   def __str__(self):
      return self.title