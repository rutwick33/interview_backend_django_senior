from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserProfiles(models.Model):
        
    username = models.OneToOneField(User, on_delete=models.CASCADE),
    email = models.EmailField(max_length=50), 
    password = models.CharField(max_length=50, null=True), 
    first_name = models.CharField(max_length=50, null=True),
    last_name = models.CharField(max_length=50, null=True), 
    date_joined = models.DateField(null=True), 
    last_login = models.DateField(null=True), 
    is_staff = models.BooleanField(default=True), 
    is_superuser = models.BooleanField(default=False), 
    is_admin = models.BooleanField(default=False)
    
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.email}"
        
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserProfiles, self).save(*args, **kwargs)
        
    def get_full_name(self):
        return self.first_name + self.last_name
    
    def get_username(self):
        return self.username
        
    def is_authenticated(self):
        return self.is_active