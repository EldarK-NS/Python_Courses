from tastypie.resources import ModelResource

from shop.models import Category, Course

from tastypie.authorization import Authorization
from .authentication import CustomAuthentication
# Create your models here.


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

# hydrate - преобразование входящих данных из запроса API в объект модели, метод позволяет настраивать, как данные из запроса будут сохранены в модели (как данные идут от клиента на сервер)
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

# dehydrate - преобразование данных из объекта модели в формат, подходящий для API, метод позволяет регулировать вывод данных для клиента(как данные идут от сервера к клиенту)
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category
        return bundle
# пример

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
