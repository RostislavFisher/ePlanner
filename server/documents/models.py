from django.db import models

class File(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")

    @classmethod
    def init(cls, **kwargs):
        File.objects.create(file=kwargs.get("files")).save()

