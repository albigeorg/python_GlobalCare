from django.urls import path
from Hospital import views


app_name="whospital"


urlpatterns = [
    path('home/',views.Home,name="Hoshome"),
    

    path('AddDoctor/',views.adddoctor,name="AddDoctor"),
    path('del_adddoctor/<int:did>',views.del_adddoctor,name="del_adddoctor"),
    


    path('AddConsultancy/',views.addconsultancy,name="AddConsultancy"),
    path('del_addconsultancy/<int:did>',views.del_addconsultancy,name="del_addconsultancy"),
    path('edi_addconsultancy/<int:eid>',views.edi_addconsultancy,name="edi_addconsultancy"),


    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('editprofile/',views.EditProfile,name='EditProfile'),
    

    path('Complaint/',views.complaint,name='Complaint'),
    path('del_com/<int:did>',views.delc,name="delc"),
    path('edi_com/<int:eid>',views.edtc,name="edtc"),

    path('feedback/',views.feedback,name='feedback'),
    path('del_feedback/<int:did>',views.delf,name="delf"),
    path('edi_feedback/<int:eid>',views.edtf,name="edtf"),

    path('AddGallery/',views.gallery,name="AddGallery"),


]