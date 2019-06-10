from django.urls import path
from . import views

# Any route matching the first argument will be handled
# by the second argument

urlpatterns = [
    path('', views.index, name="work_history"),
]