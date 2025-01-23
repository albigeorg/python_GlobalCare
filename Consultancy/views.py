from django.shortcuts import get_object_or_404, render,redirect
from Consultancy.models import *
from Hospital.models import *
from User.models import *
# Create your views here.

def Home(request):
    cdata=tbl_consultancy.objects.get(id=request.session["cid"])
    hsptl=cdata.hospital
    hdata=tbl_newhospital.objects.get(id=hsptl.id)
    doObj=tbl_doctor.objects.filter(hospital=hdata)
    return render(request,"Consultancy/Consultancyhome.html",{'data':doObj,'hos':hdata})


def availabledoctor(request):
    cdata=tbl_consultancy.objects.get(id=request.session["cid"])
    hsptl=cdata.hospital
    hdata=tbl_newhospital.objects.get(id=hsptl.id)
    doObj=tbl_doctor.objects.filter(hospital=hdata)
    adObj = tbl_available.objects.filter(Doctor__in=doObj)
    if request.method=="POST":
        ad=tbl_doctor.objects.get(id=request.POST.get('sel_doctor'))
        tbl_available.objects.create(available_date=request.POST.get("txtdate"),
        available_formtime=request.POST.get("txttime"),
        available_totime=request.POST.get("txtti"),
        Doctor=ad)
        return render(request,"Consultancy/AvailabiliatyOfDoctors.html",{'adata':adObj,'data':doObj})    
    else:
        return render(request,"Consultancy/AvailabiliatyOfDoctors.html",{'adata':adObj,'data':doObj})

def del_availabledoctor(request,did):
    tbl_available.objects.get(id=did).delete()
    return redirect('webConsultancy:AvailabiliatyOfDoctors')


def slots(request,sid):
    sl=tbl_available.objects.get(id=sid)
    sObj=tbl_slots.objects.filter(available=sl)
  
    if request.method=="POST":
        slot=int(request.POST.get("txtslot"))
        for i in range(1,slot+1):
           tbl_slots.objects.create(slots=i,available=sl)
        return render(request,"Consultancy/Slots.html",{'data':sObj})    
    else:
        return render(request,"Consultancy/Slots.html",{'data':sObj})
    



def del_slots(request,did):
    tbl_slots.objects.get(id=did).delete()
    return redirect('webConsultancy:availabledoctor')

def edi_slots(request,eid):
    slObj=tbl_slots.objects.get(id=eid)
    if request.method=="POST":
        slObj.slots=request.POST.get("txtslot")
        slObj.save()
        return redirect('webConsultancy:availabledoctor')
    else:
        return render(request,"Consultancy/Slots.html",{'slot':slObj})

def complaint(request):
    comobj=tbl_complaint.objects.filter(consultancy=request.session["cid"])
    if request.method=="POST":
        co=tbl_consultancy.objects.get(id=request.session["cid"])
        tbl_complaint.objects.create(complaint_title=request.POST.get("txttitle"),
        complaint_com=request.POST.get("txtcom"),
        consultancy=co)
        return render(request, "Consultancy/Complaint.html", {'data':comobj})
    else:
        return render(request, "Consultancy/Complaint.html", {'data':comobj})

def delc(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect('webConsultancy:Complaint')

def edtc(request,eid):
    cdata=tbl_complaint.objects.get(id=eid) 
    if request.method=="POST":
        cdata.complaint_title=request.POST.get("txttitle")
        cdata.complaint_com=request.POST.get("txtcom")
        cdata.save()
        return redirect('webConsultancy:Complaint')
    else:
        return render(request,"Consultancy/Complaint.html",{'datac':cdata})


def feedback(request):
    feedobj=tbl_feedback.objects.filter(consultancy=request.session["cid"])
    if request.method=="POST":
        co=tbl_consultancy.objects.get(id=request.session["cid"])
        tbl_feedback.objects.create(feedback_title=request.POST.get("txtfeed"),
        consultancy=co)
        return render(request, "Consultancy/Feedback.html", {'cdata':feedobj})
    else:
        return render(request, "Consultancy/Feedback.html", {'cdata':feedobj})

def delf(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect('webConsultancy:feedback')

def edtf(request,eid):
    fdata=tbl_feedback.objects.get(id=eid) 
    if request.method=="POST":
        fdata.feedback_title=request.POST.get("txtfeed")
        fdata.save()
        return redirect('webConsultancy:feedback')
    else:
        return render(request,"Consultancy/Feedback.html",{'adata':fdata})


def viewappointment(request):
    con=tbl_consultancy.objects.get(id=request.session["cid"])
    hsptl=con.hospital.id
    ddata=tbl_newhospital.objects.get(id=hsptl)
    dr=tbl_doctor.objects.filter(hospital=ddata)
    avail=tbl_available.objects.get(doctor=dr)
    appObj=tbl_appointment.objects.filter(slots__available=avail)
    if request.method=="POST":
        return render(request,"Consultancy/Viewappointment.html",{'adata':appObj})      
    else:
        return render(request,"Consultancy/Viewappointment.html",{'adata':appObj})
    

def viewappointment(request):
    consultancy_id = request.session.get("cid")
    consultancy = get_object_or_404(tbl_consultancy, id=consultancy_id)
    hospital = consultancy.hospital
    appointments = tbl_appointment.objects.filter(slot__available__Doctor__hospital=hospital,appointment_status=0)
    return render(request, "Consultancy/Viewappointment.html", {'adata': appointments})      
   

def acc_viewappointment(request,aid):
    accdata=tbl_appointment.objects.get(id=aid)
    accdata.appointment_status=1
    accdata.save()
    return redirect('webConsultancy:Viewappointment')


def rej_viewappointment(request,rid):
    accObj=tbl_appointment.objects.get(id=rid)
    accObj.appointment_status=2
    accObj.save()
    return redirect('webConsultancy:Viewappointment')

def Accviewappointment(request):
    appObj=tbl_appointment.objects.filter(appointment_status=1)
    if request.method=="POST":
        return render(request,"Consultancy/Acceptedappointment.html",{'data':appObj})    
    else:
        return render(request,"Consultancy/Acceptedappointment.html",{'data':appObj})

def Rejviewappointment(request):
    appObj=tbl_appointment.objects.filter(appointment_status=2)
    if request.method=="POST":
        return render(request,"Consultancy/Rejectedappointment.html",{'data':appObj})    
    else:
        return render(request,"Consultancy/Rejectedappointment.html",{'data':appObj})



