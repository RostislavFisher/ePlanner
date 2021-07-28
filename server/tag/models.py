from django.db import models


class Tag(models.Model):
    tag = models.TextField("")

    @classmethod
    def init(cls, **kwargs):
        Tag.objects.create(tag=kwargs.get("tag")).save()

    @classmethod
    def remove(cls, **kwargs):
        Tag.objects.get(id=kwargs.get("id")).delete()


