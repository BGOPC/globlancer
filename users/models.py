from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    username = models.CharField(default="", null=False, db_index=True,
                                unique=True)
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    phoneNum = PhoneNumberField(null=False, unique=True, default='')
    profile = models.ImageField(upload_to="profile/", null=True, blank=True,
                                default="https://www.seekpng.com/png/detail/413-4139803_unknown-profile-profile-picture-unknown.png")
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username", "email", "first_name", "last_name", "password"]

    def __str__(self):
        return f"{self.username}:{self.first_name} {self.last_name}"
