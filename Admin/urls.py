from django.urls import path
from Admin import views


app_name="webadmin"


urlpatterns = [

    path('Adminhome/',views.adminhome,name="Adminhome"),

    path('District/',views.District,name="District"),
    path('del_district/<int:did>',views.del_district,name="del_district"),
    path('edi_district/<int:eid>',views.edi_district,name="edit_district"),




    path('Place/',views.Place,name="Place"),
    path('del_Place/<int:did>',views.del_Place,name="del_Place"),
    path('edi_Place/<int:eid>',views.edi_Place,name="edit_Place"),


    path('Department/',views.Department,name='Department'),
    path('del_department/<int:did>',views.del_department,name="del_department"),
    path('edi_department/<int:eid>',views.edi_department,name="edit_department"),



    path('Hospitaltype/',views.Hospitaltype,name='Hospitaltype'),
    path('del_Hospitaltype/<int:did>',views.del_Hospitaltype,name="del_Hospitaltype"),
    path('edi_Hospitaltype/<int:eid>',views.edi_Hospitaltype,name="edi_Hospitaltype"),


    path('Hospitalverification/',views.Hospitalverification,name='Hospitalverification'),
    path('acc_Hospitalverification/<int:aid>',views.acc_Hospitalverification,name="acc_Hospitalverification"),
    path('rej_Hospitalverification/<int:rid>',views.rej_Hospitalverification,name="rej_Hospitalverification"),


    path('AcceptHospital/',views.AccHospital,name='AcceptHospital'),
    path('RejectHospital/',views.RejHospital,name='RejectHospital'),


    path('Viewcomplaint/',views.viewcomplaint,name='Viewcomplaint'),

    path('Reply/<int:rid>',views.reply,name='Reply'),

    path('Viewfeedback/',views.viewfeedback,name='Viewfeedback'),






    
]