from django.db import models

from documents.models import File, Tag
from family.models import Family


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

