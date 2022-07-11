from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title = "API")

urlpatterns = [
    path("products/categories/", views.categories),
    path("products/fetch/", views.categories),
    path("products/create/", views.products_create),
    path("products/delete/", views.products_delete),
    path("products/docs", schema_view)
]