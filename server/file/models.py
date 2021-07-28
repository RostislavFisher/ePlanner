from django.contrib.auth.models import User
from django.db import models
from budget.models import budgetPlan
from family.models import Family


class File(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")

    @classmethod
    def init(cls, **kwargs):
        File.objects.create(file=kwargs.get("files")).save()


