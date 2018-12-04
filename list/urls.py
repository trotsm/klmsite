from . import views
from django.urls import path, include
from django.views.generic import ListView, DetailView
from list.models import Articles

urlpatterns = [
    # path('', views.index, name='index'),
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("title")[:20], template_name="html/list.html")),
    path('<int:pk>/', DetailView.as_view(model=Articles, template_name="html/detail.html")),
]