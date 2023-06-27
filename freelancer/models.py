from django.db import models
from django.utils import timezone

from users.models import User


# Create your models here.

class Skill(models.Model):
    name = models.CharField(null=False, max_length=255, db_index=True, unique=True)


class FreeLancer(User, models.Model):
    is_freelancer = True
    description = models.TextField(null=False, default="No Description Provided")
    skills = models.ManyToManyField(Skill, related_name="FreeLancer_Skills")


class Employer(User, models.Model):
    is_employer = True
    description = models.TextField(null=False, default="No Description Provided")


class Project(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False)
    freelancer = models.ForeignKey(FreeLancer, null=True, on_delete=models.SET_NULL, related_name="freelancer")
    employer = models.ForeignKey(Employer, null=True, on_delete=models.SET_NULL, related_name="employer")
    price = models.DecimalField(null=False, default=1000000, decimal_places=0, max_digits=9)
    tags = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(default=timezone.now)
