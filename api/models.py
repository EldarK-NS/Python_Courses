from tastypie.resources import ModelResource

from shop.models import Category, Course
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
# python manage.py  makemigrations после создания/изменения моделей вызываем команду создания миграций
# python manage.py migrate применяет миграции к базе данных
