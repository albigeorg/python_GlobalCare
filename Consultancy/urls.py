from django.urls import path
from Consultancy import views


app_name="webConsultancy"


urlpatterns = [
    path('home/',views.Home,name="Consultancyhome"),
    path('availabledoctor/',views.availabledoctor,name="availabledoctor"),
    path('del_availabledoctor/<int:did>',views.del_availabledoctor,name="del_availabledoctor"),


    path('Slots/<int:sid>',views.slots,name="Slots"),
    path('del_slots/<int:did>',views.del_slots,name="del_slots"),
    path('edi_slots/<int:eid>',views.edi_slots,name="edi_slots"),


    path('Complaint/',views.complaint,name='Complaint'),
    path('del_com/<int:did>',views.delc,name="delc"),
    path('edi_com/<int:eid>',views.edtc,name="edtc"),


    path('feedback/',views.feedback,name='feedback'),
    path('del_feed/<int:did>',views.delf,name="delf"),
    path('edi_feed/<int:eid>',views.edtf,name="edtf"),


    path('Viewappointment/',views.viewappointment,name='Viewappointment'),
    path('acc_Viewappointment/<int:aid>',views.acc_viewappointment,name="acc_Viewappointment"),
    path('rej_Viewappointment/<int:rid>',views.rej_viewappointment,name="rej_Viewappointment"),

    path('Acceptedappointment/',views.Accviewappointment,name='Acceptedappointment'),
    path('Rejectedappointment/',views.Rejviewappointment,name='Rejectedappointment'),



]