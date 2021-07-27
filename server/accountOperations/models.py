from django.contrib.auth.models import User
from django.db import models
from budget.models import budgetPlan
from documents.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expire_date = models.DateField(null=True, blank=True)
    firstConnection_date = models.DateField(null=True, blank=True)
    icon = models.TextField(default="https://i.pinimg.com/736x/8b/16/7a/8b167af653c2399dd93b952a48740620.jpg")
    budget = models.OneToOneField(budgetPlan, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    @staticmethod
    def createCell(**kwargs):
        Profile(user=kwargs.get("user"), expire_date=kwargs.get("expire_date"),
                firstConnection_date=kwargs.get("firstConnection_date"), budget=kwargs.get("budget")).save()


