from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('reservation/<int:reservation_id>/', views.reservation, name='reservation'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
    path('delete/<int:reservation_id>/', views.delete_obj, name='delete_resv'),
    path('chek_in/<int:reservation_id>/', views.book_in, name='chek_in'),
    path('chek_out/<int:reservation_id>/', views.book_out, name='chek_out'),

]
