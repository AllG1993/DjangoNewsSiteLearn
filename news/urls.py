from django.urls import path

from .views import index, get_category, old

urlpatterns = [
    path('', index, name='home_url'),
    path('old/', old, name='old_url'),
    path('category/<int:category_id>/', get_category, name='category_url'),
]
