from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *


# Create your views here.

def adminhome(request):
    adata=tbl_admin.objects.get(id=request.session['aid'])
    return render(request,"Admin/Adminhome.html",{'data':adata})


def District(request):
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("txtdistrict"))
        return render(request,"Admin/District.html",{'data':disObj})
    else:
        return render(request,"Admin/District.html",{'data':disObj})


def del_district(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('webadmin:District')


def edi_district(request,eid):
    disdata=tbl_district.objects.get(id=eid)
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        disdata.district_name=request.POST.get("txtdistrict")
        disdata.save()
        return redirect('webadmin:District')
    else:
        return render(request,"Admin/District.html",{'ddata':disdata,'data':disObj})



def Place(request):
    disObj=tbl_district.objects.all()
    placeObj=tbl_place.objects.all()
    if request.method=="POST":
        disid=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=request.POST.get("txtplace"),district=disid)
        return render(request,"Admin/Place.html",{'disdata':disObj,'dplace': placeObj})    
    else:
        return render(request,"Admin/Place.html",{'disdata':disObj,'dplace': placeObj})

def del_Place(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('webadmin:Place')


def edi_Place(request,eid):
    pldata=tbl_place.objects.get(id=eid)
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        pldata.place_name=request.POST.get("txtplace")
        pldata.District=tbl_district.objects.get(id=request.POST.get("sel_district"))
        pldata.save()
        return redirect('webadmin:Place')
    else:
        return render(request,"Admin/Place.html",{'pdata':pldata,'disdata':disObj})


def Department(request):
    depObj=tbl_department.objects.all()
    if request.method=="POST":
        tbl_department.objects.create(Department=request.POST.get("txtpart"))
        return render(request,"Admin/Department.html",{'pdep': depObj})    
    else:
        return render(request,"Admin/Department.html",{'pdep': depObj})


def del_department(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect('webadmin:Department')


def edi_department(request,eid):
    depObj=tbl_department.objects.get(id=eid)
    if request.method=="POST":
        depObj.Department=request.POST.get("txtpart")
        depObj.save()
        return redirect('webadmin:Department')
    else:
        return render(request,"Admin/Department.html",{'ddata':depObj})



def Hospitaltype(request):
    hosObj=tbl_hospitaltype.objects.all()
    if request.method=="POST":
        tbl_hospitaltype.objects.create(Hospitaltype=request.POST.get("txthos"))
        return render(request,"Admin/Hospitaltype.html",{'data':hosObj})    
    else:
        return render(request,"Admin/Hospitaltype.html",{'data':hosObj})

def del_Hospitaltype(request,did):
    tbl_hospitaltype.objects.get(id=did).delete()
    return redirect('webadmin:Hospitaltype')


def edi_Hospitaltype(request,eid):
    hosObj=tbl_hospitaltype.objects.get(id=eid)
    if request.method=="POST":
        hosObj.Hospitaltype=request.POST.get("txthos")
        hosObj.save()
        return redirect('webadmin:Hospitaltype')
    else:
        return render(request,"Admin/Hospitaltype.html",{'hos':hosObj})


def Hospitalverification(request):
    vObj=tbl_newhospital.objects.filter(hospital_vstatus=0)
    if request.method=="POST":
        return render(request,"Admin/Hospitalverification.html",{'data':vObj})    
    else:
        return render(request,"Admin/Hospitalverification.html",{'data':vObj})

def acc_Hospitalverification(request,aid):
    accdata=tbl_newhospital.objects.get(id=aid)
    accdata.hospital_vstatus=1
    accdata.save()
    return redirect('webadmin:Hospitalverification')


def rej_Hospitalverification(request,rid):
    accObj=tbl_newhospital.objects.get(id=rid)
    accObj.hospital_vstatus=2
    accObj.save()
    return redirect('webadmin:Hospitalverification')

        

def AccHospital(request):
    vObj=tbl_newhospital.objects.filter(hospital_vstatus=1)
    if request.method=="POST":
        return render(request,"Admin/AcceptHospital.html",{'data':vObj})    
    else:
        return render(request,"Admin/AcceptHospital.html",{'data':vObj})

def RejHospital(request):
    vObj=tbl_newhospital.objects.filter(hospital_vstatus=2)
    if request.method=="POST":
        return render(request,"Admin/RejectHospital.html",{'data':vObj})    
    else:
        return render(request,"Admin/RejectHospital.html",{'data':vObj})


def viewcomplaint(request):
    
    coObj=tbl_complaint.objects.filter(complaint_status=0)
    user_complaints = tbl_complaint.objects.filter( user__isnull=False)
    consultancy_complaints = tbl_complaint.objects.filter(consultancy__isnull=False)
    hospital_complaints = tbl_complaint.objects.filter(hospital__isnull=False)
    doctor_complaints = tbl_complaint.objects.filter(doctor__isnull=False)
    return render(request,"Admin/Viewcomplaint.html",{'user':user_complaints,'con':consultancy_complaints,'hos':hospital_complaints,'doc':doctor_complaints})    
    

def reply(request, rid):
    comobj=tbl_complaint.objects.filter(complaint_status=0)
    replydata=tbl_complaint.objects.get(id=rid)
    if request.method=="POST":
        replydata.complaint_reply=request.POST.get("txtrep")
        replydata.complaint_status=1
        replydata.save()
        return redirect('webadmin:Viewcomplaint')
    else:
        return render(request, "Admin/Reply.html",{'datas':comobj})



def viewfeedback(request):
    
    user_complaints = tbl_feedback.objects.filter( user__isnull=False)
    consultancy_complaints = tbl_feedback.objects.filter(consultancy__isnull=False)
    hospital_complaints = tbl_feedback.objects.filter(hospital__isnull=False)
    doctor_complaints = tbl_feedback.objects.filter(doctor__isnull=False)
    return render(request,"Admin/Viewfeedback.html",{'user':user_complaints,'con':consultancy_complaints,'hos':hospital_complaints,'doc':doctor_complaints})    




















