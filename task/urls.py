from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('create/', views.Create.as_view(), name="create"),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name="delete"),
    path('finished/<int:pk>', views.Finished.as_view(), name="finished"),
]
