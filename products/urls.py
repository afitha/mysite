from products import views
from django.urls import path


urlpatterns = [
    path('',views.prohome),
    path('user',views.userinfosave),
    

]
