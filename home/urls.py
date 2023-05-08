
from home import views
from django.urls import path


# urlpatterns = [

#     path('',views.homepage),
#     path('calc',views.calcvalues),
# ]
####################################################

urlpatterns = [
    path('dbitems',views.dbitemdisp),
    path('homeone',views.homeone),
    path('pro/<str:pi>',views.prod),
    path('addcart',views.addtocart),
    path('viewcarts',views.viewcart),
    path('jsondata',views.getjsondata),
    path('proser',views.search),
    path('getpro/<str:keyw>',views.getproduct),


    
]
