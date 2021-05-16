from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from store import views
urlpatterns = [ 
    path('home',views.home,name='home'),
    path('Login',views.Login,name='Login'),
    path('Logout',views.Logout_view),
    path('Register',views.Register,name='Register'),
    path('AboutUs',views.AboutUs,name='AboutUs'),
    path('product',views.product,name='product'),
    path('product1',views.product1,name='product1'),
    path('product2',views.product2,name='product2'),
    path('Profile1',views.profile1,name='profile1'),
    path('payment',views.payment,name='payment'),
    path('contact' ,views.Contact),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)