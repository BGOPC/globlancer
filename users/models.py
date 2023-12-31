from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

default_profile_picture = "https://www.seekpng.com/png/detail/413-4139803_unknown-profile-profile-picture-unknown.png"


# Create your models here.
class User(AbstractUser):
    username = models.CharField(default="", null=False, db_index=True,
                                unique=True)
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    phoneNum = PhoneNumberField(null=False, unique=True, default='')
    profile_picture = models.ImageField(upload_to="profile/", null=True, blank=True,
                                        default=default_profile_picture)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "password"]
    is_freelancer = False
    is_employer = False

    def __str__(self):
        return f"{self.username}:{self.first_name} {self.last_name}"
