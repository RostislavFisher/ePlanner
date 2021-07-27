from django.db import models


class budgetItem(models.Model):
    title = models.TextField("")
    budget = models.IntegerField(default=0)


class budgetPlan(models.Model):
    totalBudget = models.IntegerField(default=0)
    budgetItem = models.ManyToManyField(budgetItem)
