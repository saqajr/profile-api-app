from django.urls import path
from profiles_Api import views


urlpatterns =[
        path('helloAPi/', views.HelloApi.as_view()),

]
