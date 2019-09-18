import uuid

from factory import DjangoModelFactory, lazy_attribute
from factory.faker import Faker

from core.models import BaseModel, Article


class BaseModelFactory(DjangoModelFactory):

    class Meta:
        model = BaseModel
        abstract = True

    id = lazy_attribute(lambda x: uuid.uuid4())


class ArticleFactory(BaseModelFactory):

    class Meta:
        model = Article

    title = Faker('text', max_nb_chars=50)
