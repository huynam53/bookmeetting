from typing import List

from django.db import models


class BaseManager(models.Manager):

    def get_batch_ids(self, ids: List[int]):
        return self.filter(id__in=ids)


class BaseUuidManager(models.Manager):

    def get_batch_ids(self, ids: List[str]):
        return self.filter(id__in=ids)
