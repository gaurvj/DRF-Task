from django.db import models


#Create your models here.
class UserInfo(models.Model):
     id = models.CharField(max_length=20, primary_key=True)
     real_name = models.CharField(max_length=30)
     tz = models.CharField(max_length=60)


#Time field has to be datetimefield but just to insert dummy data have created like this.
class ActivityPeriod(models.Model):
     user = models.ForeignKey(UserInfo, related_name='users', on_delete=models.CASCADE)
     start_time = models.CharField(max_length=60)
     end_time = models.CharField(max_length=60)
