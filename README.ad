1. Create project

pip install django djangorestframework
django-admin startproject myproject
cd myproject

2. Create App

python manage.py startapp products


3. register
In myproject/settings.py,  add rest_framework and books

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # add Django REST Framework
    'products',  # add books 
]


4. create Model
In products/models.py

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    manufactured_date = models.DateField()

    def __str__(self):
        return self.title


5. Create database in mysql:
In workbench, create database product.
Back to vscode, in settings.py,

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product',  # database
        'USER': 'root',       # username
        'PASSWORD': 'root123',   # pwd
        'HOST': 'localhost',           # local
        'PORT': '3306',                # port
    }
}

(change pwd to yours)

then do migrate in command line:
python manage.py makemigrations
python manage.py migrate

6. Serializer:

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'manufacturer', 'manufactured_date']



7. create views.py:
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import get_object_or_404

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




8. create products/urls.py 

from django.urls import path
from .views import ProductList

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
]


then in myproject/urls.py, include products:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),  # 
]




9.
python manage.py runserver



