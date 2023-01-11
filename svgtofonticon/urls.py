
from django.contrib import admin
from django.urls import path , include
from svg2font import views as svg2fonr_views
from user_app import views as user_app_views
urlpatterns = [
    # path('',include('svg2font.urls')),
    path('',svg2fonr_views.index,name='index'),
    path('admin/', admin.site.urls),
    path('svg2font/',include('svg2font.urls')),

    path('home/',include('svg2font.urls')),
    path('about_us/',include('svg2font.urls')),
    path('contact_us/',include('svg2font.urls')),
    
    # --------------This is user App---------------
    path('account/',include('user_app.urls'))



    # path('manage/',include('svg2font.urls'))

]
