from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:pk>/', views.view_question, name='view_question'),
    path('question/<int:pk>/answer/', views.answer_question, name='answer_question'),
    path('answer/<int:pk>/like/', views.like_answer, name='like_answer'),
    path('logout/', views.logout_view, name='logout'),
]
