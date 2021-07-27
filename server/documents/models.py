from django.contrib.auth.models import User
from django.db import models
from budget.models import budgetPlan
from family.models import Family


class File(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")

    @classmethod
    def init(cls, **kwargs):
        File.objects.create(file=kwargs.get("files")).save()


class Tag(models.Model):
    tag = models.TextField("")

    @classmethod
    def init(cls, **kwargs):
        Tag.objects.create(tag=kwargs.get("tag")).save()

    @classmethod
    def remove(cls, **kwargs):
        Tag.objects.get(id=kwargs.get("id")).delete()


class Product(models.Model):
    dateAdded = models.DateField(null=True, blank=True)
    textTitle = models.TextField()
    price = models.IntegerField()
    text = models.TextField(default="")
    files = models.ManyToManyField(File)
    tags = models.ManyToManyField(Tag)
    family = models.ManyToManyField(Family)

    @classmethod
    def init(cls, **kwargs):
        documentObject = Product.objects.create(textTitle=kwargs.get("textTitle"), text=kwargs.get("text"),
                                                dateAdded=kwargs.get("dateAdded"), price=kwargs.get("price"))
        if bool(kwargs.get("family")):
            documentObject.family.add(Family.objects.get(id=kwargs.get("family")))

        for x in kwargs.get("files"): documentObject.files.add(x)
        for x in kwargs.get("tags"): documentObject.tags.add(x[0].id)
        documentObject.save()
        return documentObject

    @classmethod
    def remove(cls, **kwargs):
        Product.objects.get(id=kwargs.get("id")).delete()
