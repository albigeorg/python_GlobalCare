from django.urls import path
from Guest import views


app_name="webguest"


urlpatterns = [
    path('NewHospital/',views.newHospital,name="NewHospital"),
    path('ajaxplace/',views.ajaxplace,name="ajax_place"),
    path('UserRegistration/',views.userregistration,name="UserRegistration"),
    path('Login/',views.Login,name="Login"),

    path('',views.mainpage,name="MainPage")

]