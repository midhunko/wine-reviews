from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('signup/', views.sign_up, name='sign_up'),
    path('reviewlist/', views.review_list, name='review_list'),
    path('addreview/<int:w_id>', views.add_review, name='add_review'),
]