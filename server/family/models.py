from django.contrib.auth.models import User
from django.db import models
from budget.models import budgetPlan


class Family(models.Model):
    users = models.ManyToManyField(User)
    title = models.TextField()
    budget = models.OneToOneField(budgetPlan, on_delete=models.CASCADE)