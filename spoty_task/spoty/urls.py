from django.urls import path

from spoty import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
    path('add_review/<int:pk>/', views.review, name='review'),
    path('<int:pk>/', views.post, name='song_page')
]
