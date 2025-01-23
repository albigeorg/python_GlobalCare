from django.urls import path
from User import views


app_name="webuser"


urlpatterns = [
    path('UserHome/',views.userhome,name='userhome'),

    path('Myprofile/',views.Myprofile,name='Myprofile'),

    path('Changepassword/',views.ChangePassword,name='ChangePassword'),

    path('Editprofile/',views.EditProfile,name='EditProfile'),

    path('viewdoctor/<int:hid>',views.searchdoctor,name="SearchDoctor"),

    path('SearchHospital/',views.searchHospital,name='SearchHospital'),

    path('ajaxplace/',views.ajaxplace,name="ajax_place"),

    path('ajaxHospital/',views.ajaxhospital,name="ajax_Hospital"),

    path('ajaxDepartment/',views.ajaxdepartment,name="ajax_Department"),
    
    path('viewAvailable/<int:docid>',views.viewavailable,name="ViewAvailable"),

    path('viewslot/<int:aid>',views.viewSlot,name='viewslot'),

    path('Appointment/<int:sid>',views.appointment,name='Appointment'),

    path('Viewmybooking/',views.viewmybooking,name='Viewmybooking'),


    path('Complaint/',views.complaint,name='Complaint'),
    path('del_com/<int:did>',views.delc,name="delc"),
    path('edi_com/<int:eid>',views.edtc,name="edtc"),

    path('feedback/',views.feedback,name='feedback'),
    path('del_feed/<int:did>',views.delf,name="delf"),
    path('edi_feed/<int:eid>',views.edtf,name="edtf"),
    
    path('Viewprescribtion/<int:pid>',views.viewprescribtion,name='Viewprescribtion'),

    path('Viewmedicalreport/<int:mid>',views.viewmedicalreport,name='Viewmedicalreport'),
]
