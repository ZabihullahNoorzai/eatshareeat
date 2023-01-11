from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('svg2font/', views.svg2font, name='svg2font'),
    path('delete/<user_id>', views.delete_user, name='delete_user'),
    path('activaty/<user_id>', views.user_activaty, name='user_activaty'),
    path('edit/<user_id>', views.user_edit, name='user_edit'),

    path('home/', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),


    
    # path('manage/', views.manage, name='manage')

]
