from django.urls import path
from Doctor import views



app_name="webDoctor"


urlpatterns = [
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Doctorhome/',views.DoctorHome,name='Doctorhome'),
    path('Changepassword/',views.ChangePassword,name='Changepassword'),
    path('Editprofile/',views.EditProfile,name='Editprofile'),
    path('Viewappointment/',views.viewappointment,name='Viewappointment'),
    path('Consuttedappointment/<int:aid>',views.consuttedappointment,name='Consuttedappointment'),


    path('feedback/',views.feedback,name='feedback'),
    path('del_fee/<int:did>',views.delt,name="delt"),
    path('edi_fee/<int:eid>',views.edt,name="edt"),
    

    path('UpdateMedicineReport/<int:mid>',views.updatemedicine,name='UpdateMedicineReport'),

    path('Addprescribtion/<int:pid>',views.prescribtion,name='Addprescribtion'),

    path('Complaint/',views.complaint,name='Complaint'),
    path('del_com/<int:did>',views.dele,name="dele"),
    path('edi_com/<int:eid>',views.edit,name="edit"),

    path('Consulted/',views.consulted,name='Consulted'),
    path('previousmedical/<int:pmid>',views.previousmedical,name='previousmedical'),
    

]
