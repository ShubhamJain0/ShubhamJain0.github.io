"""restaurantapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from mainapp.views import (homepage, orderpage, yourorders, repeatorder, deletepreviousorderview, deleteallordersview,deletecartpage, 
    confirmorder, placeorder, cancelitem, manageaddressview, finalcancelview, manageprofilepage, deleteaddressview, Searching, cartpage,
    cartforsearch, carthtml, LocationView,  finaltemplateview,  reduceitemview, navbarimage, contactpageform, booktableview, Bookingslist)
from accounts.views import (login_view, register_view, logout_view, change_password, activate)
from django.contrib.auth.views import ( PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view),
	path('accounts/register/', register_view),
	path('accounts/logout/', logout_view),
    path('password/', change_password),
   	path('home/', homepage),
   	path('order/', orderpage),
    path('yourorders/', yourorders),
    path('repeatorder/', repeatorder),
    path('deletepreviousorder/', deletepreviousorderview),
    path('deleteall/', deleteallordersview),
    path('cart/', cartpage),
    path('deletecart/', deletecartpage),
    path('confirm/', confirmorder),
    path('cancel/', cancelitem),
    path('address/', manageaddressview),
    path('finalcancel/', finalcancelview),
    path('manageprofile/', manageprofilepage),
    path('place/', placeorder),
    path('deleteaddress/', deleteaddressview),
    path('search/', Searching),
    path('cartforsearch/', cartforsearch),
    path('carthtml/', carthtml),
    path('location/',  LocationView),
    path('finaltemplate/',  finaltemplateview),
    path('reduceitem/', reduceitemview),
    path('navbarimage/', navbarimage),
    path('contactpage/', contactpageform),
    path('booktable/', booktableview),
    path('Bookingslist/', Bookingslist),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    path('accounts/password/reset/',PasswordResetView.as_view(),name="password_reset"),
    path('accounts/password/reset/done/',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('accounts/password/done',PasswordResetCompleteView.as_view(),name="password_reset_complete"),


    
] 


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    