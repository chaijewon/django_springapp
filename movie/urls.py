from django.urls import path,include
from movie import views
# @RequestMapping
urlpatterns=[
    path('',views.home),  # http://127.0.0.1:8000/movie
    path('list/',views.movie_list), #http://127.0.0.1:8000/movie/list
    path('news/',views.news),
    path('detail/',views.detail),
    path('recommand/',views.recommand)
]