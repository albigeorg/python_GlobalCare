from django.shortcuts import render,redirect
from Hospital.models import *
from User.models import *
from Doctor.models import *
from Consultancy.models import *


# Create your views here.


def DoctorHome(request):
    if 'docid' in request.session:
        doctor_name=request.session["dname"]
        docdata=tbl_doctor.objects.get(id=request.session["docid"])
        feed=tbl_feedback.objects.all()
        return render(request,"Doctor/Doctorhome.html",{'doctor':doctor_name,'doc':docdata,'feed':feed})
    else:
        return redirect("webguest:Login")

def Myprofile(request):
        docdata=tbl_doctor.objects.get(id=request.session["docid"])
        return render(request,"Doctor/Myprofile.html",{'doc':docdata})

def ChangePassword(request):
    if request.method=="POST":
        docdata=tbl_doctor.objects.get(id=request.session["docid"],doctor_password=request.POST.get("txtpass"))
        cpass=request.POST.get("txtpass2")
        new=request.POST.get("txtpass1")
        if cpass==new:
            docdata.doctor_password=request.POST.get("txtpass2")
            docdata.save()
            return redirect('webDoctor:Myprofile')
        else:
            return render(request,"Doctor/Changepassword.html")
    else:
        return render(request,"Doctor/Changepassword.html")


def EditProfile(request):
    docdata=tbl_doctor.objects.get(id=request.session["docid"])
    if request.method=="POST":
        docdata.doctor_name=request.POST.get("txtname")
        docdata.doctor_address=request.POST.get("txtadd")
        docdata.doctor_Contact=request.POST.get("txtcon")
        docdata.doctor_email=request.POST.get("txtemail")
        docdata.save()
        return redirect('webDoctor:Myprofile')
    else:
        return render(request,"Doctor/EditProfile.html",{'doctor':docdata})

def viewappointment(request):
    doctor = tbl_doctor.objects.get(id=request.session["docid"])  
    appObj = tbl_appointment.objects.filter(slot__available__Doctor=doctor, appointment_status=1)
  
    return render(request,"Doctor/Viewappointment.html",{'adata':appObj})

def consuttedappointment(request,aid):
    conObj=tbl_appointment.objects.get(id=aid)
    conObj.appointment_status=3
    conObj.save()  
    return redirect("webDoctor:Consulted")

def consulted(request):
    doctor = tbl_doctor.objects.get(id=request.session["docid"]) 
    cdata=tbl_appointment.objects.filter(appointment_status=3,slot__available__Doctor=doctor)
    return render(request,"Doctor/Consuttedappointment.html",{"cdata":cdata})



def feedback(request):
    feedobj=tbl_feedback.objects.filter(doctor=request.session["docid"])
    if request.method=="POST":
        do=tbl_doctor.objects.get(id=request.session["docid"])
        tbl_feedback.objects.create(feedback_title=request.POST.get("txtfeed"),
        doctor=do)
        return render(request, "Doctor/Feedback.html", {'cdata':feedobj})
    else:
        return render(request, "Doctor/Feedback.html", {'cdata':feedobj})

def delt(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect('webDoctor:feedback')

def edt(request,eid):
    fdata=tbl_feedback.objects.get(id=eid) 
    if request.method=="POST":
        fdata.feedback_title=request.POST.get("txtfeed")
        fdata.save()
        return redirect('webDoctor:feedback')
    else:
        return render(request,"Doctor/Feedback.html",{'adata':fdata})


def updatemedicine(request,mid):
    meddata=tbl_updatemedicine.objects.all()
    if request.method=="POST":
        appdata=tbl_appointment.objects.get(id=mid)
        tbl_updatemedicine.objects.create(updatemedicine_report=request.FILES.get("txtfile"),
        updatemedicine_medical=request.POST.get("txtmed"),
        updatemedicine_major=request.POST.get("txtmajor"),
        appointment=appdata)
        return redirect("webDoctor:Consulted")
    else:
        return render(request,"Doctor/UpdateMedicineReport.html",{'data':meddata})

def prescribtion(request,pid):
    pdata=tbl_prescribtion.objects.all()
    if request.method=="POST":
        appdata=tbl_appointment.objects.get(id=pid)
        tbl_prescribtion.objects.create(prescribtion_medicine=request.POST.get("txtmed"),
        prescribtion_diet=request.POST.get("txtdiet"),
        appointment=appdata)
        return render(request,"Doctor/Addprescribtion.html",{'data':pdata})    
    else:
        return render(request,"Doctor/Addprescribtion.html",{'data':pdata})

def complaint(request):
    comobj=tbl_complaint.objects.filter(doctor=request.session["docid"])
    if request.method=="POST":
        do=tbl_doctor.objects.get(id=request.session["docid"])
        tbl_complaint.objects.create(complaint_title=request.POST.get("txttitle"),
        complaint_com=request.POST.get("txtcom"),
        doctor=do)
        return render(request, "Doctor/Complaint.html", {'data':comobj})
    else:
        return render(request, "Doctor/Complaint.html", {'data':comobj})

def dele(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect('webDoctor:Complaint')

def edit(request,eid):
    cdata=tbl_complaint.objects.get(id=eid) 
    if request.method=="POST":
        cdata.complaint_title=request.POST.get("txttitle")
        cdata.complaint_com=request.POST.get("txtcom")
        cdata.save()
        return redirect('webDoctor:Complaint')
    else:
        return render(request,"Doctor/Complaint.html",{'datac':cdata})


def previousmedical(request,pmid):
    appoin=tbl_appointment.objects.get(id=pmid)
    user=appoin.user.id
    medical=tbl_updatemedicine.objects.filter(appointment__user=user)
    prescription=tbl_prescribtion.objects.filter(appointment__user=user)
    return render(request,"Doctor/Viewpreviousmedical.html",{'medical':medical,'prescribtion':prescription})