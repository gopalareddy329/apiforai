from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.testapi),
    path('api/post/',views.testapipost,name="apicalls"),
    path('',views.sendresponce)
]
