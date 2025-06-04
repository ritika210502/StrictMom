from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICE=[('M','Male'),('F','Female'),('O','Other')]

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no=models.CharField(max_length=15)
    dob=models.DateField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICE)
    profile_img=models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username
