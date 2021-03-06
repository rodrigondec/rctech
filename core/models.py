import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    objects = models.Manager()

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ('title',)
