from django.shortcuts import render,redirect
from User.models import *
from Hospital.models import *
from Consultancy.models import *
from Doctor.models import *



# Create your views here.


def ajaxplace(request):
    disObj=tbl_district.objects.get(id=request.GET.get('DIST'))
    place=tbl_place.objects.filter(district=disObj)
    return render(request,"Guest/AjaxPlace.html",{'plc':place})

def userhome(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/UserHome.html",{'user':userdata})

def Myprofile(request):
    if 'uid' in request.session:
        userdata=tbl_user.objects.get(id=request.session["uid"])
        return render(request,"User/Myprofile.html",{'user':userdata})
    


def ChangePassword(request):
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get("txtpass"))
        cpass=request.POST.get("txtpass2")
        new=request.POST.get("txtpass1")
        if cpass==new:
            userdata.user_password=request.POST.get("txtpass2")
            userdata.save()
            return redirect('webuser:Myprofile')
        else:
            return render(request,"User/Changepassword.html")
    else:
        return render(request,"User/Changepassword.html")


def EditProfile(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        userdata.user_name=request.POST.get("txtname")
        userdata.user_address=request.POST.get("txtadd")
        userdata.user_contact=request.POST.get("txtcon")
        userdata.user_email=request.POST.get("txtemail")
        userdata.save()
        return redirect('webuser:Myprofile')
    else:
        return render(request,"User/EditProfile.html",{'user':userdata})



def searchdoctor(request,hid):
    depObj=tbl_department.objects.all()
    hosObj=tbl_newhospital.objects.get(id=hid)
    request.session["hos"]=hosObj.id
    docdata=tbl_doctor.objects.filter(hospital=hosObj)
    return render(request,"User/SearchDoctor.html",{'dep':depObj,'hos':hosObj,'adata':docdata})    

def ajaxdepartment(request):
    ddata=tbl_department.objects.get(id=request.GET.get('dep'))
    hosObj=tbl_newhospital.objects.get(id=request.session["hos"])
    doctor=tbl_doctor.objects.filter(Department=ddata,hospital=hosObj)
    print(doctor)
    return render(request,"User/AjaxDepartment.html",{'depart':doctor})


def ajaxhospital(request):
    if (request.GET.get("pid") != "") and (request.GET.get("hid") != ""):
        placedata=tbl_place.objects.get(id=request.GET.get("pid"))
        hsptdata = tbl_hospitaltype.objects.get(id=request.GET.get("hid"))
        hsptl=tbl_newhospital.objects.filter(hospitaltype=hsptdata,place=placedata,hospital_vstatus=1)
        return render(request,"User/AjaxHospital.html",{'hospital':hsptl})
    elif request.GET.get("pid") != "":
        placedata=tbl_place.objects.get(id=request.GET.get("pid"))
        hsptl=tbl_newhospital.objects.filter(place=placedata,hospital_vstatus=1)
        return render(request,"User/AjaxHospital.html",{'hospital':hsptl})
    else:
        hsptdata = tbl_hospitaltype.objects.get(id=request.GET.get("hid"))
        hsptl=tbl_newhospital.objects.filter(hospitaltype=hsptdata,hospital_vstatus=1)
        return render(request,"User/AjaxHospital.html",{'hospital':hsptl})
    

def searchHospital(request):
    uObj=tbl_district.objects.all()
    hosdata=tbl_hospitaltype.objects.all()
    hosobj=tbl_newhospital.objects.filter(hospital_vstatus=1)
    # if request.method=="POST":
    #     pl=tbl_place.objects.get(id=request.POST.get('sel_place'))
    #     hosid=tbl_hospitaltype.objects.get(id=request.session['hid'])
    #     return render(request,"User/searchHospital.html",{'data':uObj,'adata':hosdata,'hdata':hosobj})    
    # else:
    return render(request,"User/searchHospital.html",{'data':uObj,'adata':hosdata,'hdata':hosobj})


def viewavailable(request,docid):
    docObj=tbl_doctor.objects.get(id=docid)
    aObj=tbl_available.objects.filter(Doctor = docObj)
    return render(request,"User/Viewavailable.html",{'data':aObj})

def viewSlot(request,aid):
    available=tbl_available.objects.get(id=aid)
    slotObj=tbl_slots.objects.filter(available=available,slot_status=0)
    return render(request,"User/ViewSlot.html",{'data':slotObj})

def appointment(request,sid):
    slot=tbl_slots.objects.get(id=sid)
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session['uid'])
        tbl_appointment.objects.create(slot=slot,user=userdata)
        slot.slot_status=1
        slot.save()
        return redirect("webuser:Viewmybooking")
    else:
        return render(request,"User/Appointment.html",{'data':slot})

def viewmybooking(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    vObj=tbl_appointment.objects.filter(user=user)
    return render(request,"User/ViewMyBooking.html",{'data':vObj})

def complaint(request):
    comobj=tbl_complaint.objects.filter(user=request.session["uid"])
    if request.method=="POST":
        us=tbl_user.objects.get(id=request.session["uid"])
        tbl_complaint.objects.create(complaint_title=request.POST.get("txttitle"),
        complaint_com=request.POST.get("txtcom"),
        user=us)
        return render(request, "User/Complaint.html", {'data':comobj})
    else:
        return render(request, "User/Complaint.html", {'data':comobj})

def delc(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect('webuser:Complaint')

def edtc(request,eid):
    cdata=tbl_complaint.objects.get(id=eid) 
    if request.method=="POST":
        cdata.complaint_title=request.POST.get("txttitle")
        cdata.complaint_com=request.POST.get("txtcom")
        cdata.save()
        return redirect('webuser:Complaint')
    else:
        return render(request,"User/Complaint.html",{'datac':cdata})


def feedback(request):
    feedobj=tbl_feedback.objects.filter(user=request.session["uid"])
    if request.method=="POST":
        us=tbl_user.objects.get(id=request.session["uid"])
        tbl_feedback.objects.create(feedback_title=request.POST.get("txtfeed"),
        user=us)
        return render(request, "User/Feedback.html", {'cdata':feedobj})
    else:
        return render(request, "User/Feedback.html", {'cdata':feedobj})

def delf(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect('webuser:feedback')

def edtf(request,eid):
    fdata=tbl_feedback.objects.get(id=eid) 
    if request.method=="POST":
        fdata.feedback_title=request.POST.get("txtfeed")
        fdata.save()
        return redirect('webuser:feedback')
    else:
        return render(request,"User/Feedback.html",{'adata':fdata})

def viewprescribtion(request,pid):
    appoint=tbl_appointment.objects.get(id=pid)
    preObj=tbl_prescribtion.objects.filter(appointment__user=request.session["uid"],appointment=appoint)
    return render(request,"User/Viewprescribtion.html",{'data':preObj})

def viewmedicalreport(request,mid):
    appoint=tbl_appointment.objects.get(id=mid)
    mObj = tbl_updatemedicine.objects.filter(appointment__user=request.session["uid"],appointment=appoint)
    return render(request,"User/Viewmedicalreport.html",{'data':mObj}) 











































    
    
    







