from django.shortcuts import render,redirect
from Admin.models import *
from Hospital.models import *
from User.models import *


# Create your views here.
def Home(request):
    hosdata=tbl_newhospital.objects.get(id=request.session['hid'])
    gobj=tbl_gallery.objects.filter(hospital=hosdata)
    return render(request,"Hospital/Hoshome.html",{'hos':hosdata,'data':gobj} )

def adddoctor(request):
    depObj=tbl_department.objects.all()
    hosdata=tbl_newhospital.objects.get(id=request.session['hid'])
    docdata=tbl_doctor.objects.filter(hospital=hosdata)
    if request.method=="POST":
        depid=tbl_department.objects.get(id=request.POST.get("sel_department"))
        hosid=tbl_newhospital.objects.get(id=request.session['hid'])
        tbl_doctor.objects.create(doctor_name=request.POST.get("txtname"),
        doctor_address=request.POST.get("txtadd"),
        doctor_Contact=request.POST.get("txtcon"),
        doctor_gender=request.POST.get("txtgen"),
        doctor_email=request.POST.get("txtemail"),
        doctor_photo=request.FILES.get("filepic"),
        doctor_proof=request.FILES.get("filepro"),
        doctor_password=request.POST.get("txtpass"),
        Department=depid,
        hospital=hosid
        )
        return render(request,"Hospital/AddDoctor.html",{'dep':depObj,'adata':docdata})    
    else:
        return render(request,"Hospital/AddDoctor.html",{'dep':depObj,'adata':docdata})

def del_adddoctor(request,did):
    tbl_doctor.objects.get(id=did).delete()
    return redirect('whospital:AddDoctor')

def addconsultancy(request):
    hosdata=tbl_newhospital.objects.get(id=request.session['hid'])
    conObj=tbl_consultancy.objects.filter(hospital=hosdata)
    if request.method=="POST":
        hosid=tbl_newhospital.objects.get(id=request.session['hid'])
        tbl_consultancy.objects.create(consultancy_name=request.POST.get("txtname"),
        consultancy_email=request.POST.get("txtemail"),
        consultancy_head=request.POST.get("txthead"),
        consultancy_password=request.POST.get("txtpass"),
        hospital=hosid)
        return render(request,"Hospital/AddConsultancy.html",{'padd': conObj})    
    else:
        return render(request,"Hospital/AddConsultancy.html",{'padd': conObj})

def del_addconsultancy(request,did):
    tbl_consultancy.objects.get(id=did).delete()
    return redirect('whospital:AddConsultancy')

def edi_addconsultancy(request,eid):
    conObj=tbl_consultancy.objects.get(id=eid)
    if request.method=="POST":
        conObj.consultancy_name=request.POST.get("txtname")
        conObj.consultancy_email=request.POST.get("txtemail")
        conObj.consultancy_head=request.POST.get("txthead")
        conObj.consultancy_password=request.POST.get("txtpass")
        conObj.save()
        return redirect('whospital:AddConsultancy')
    else:
        return render(request,"Hospital/AddConsultancy.html",{'con':conObj})

def Myprofile(request):
    hosdata=tbl_newhospital.objects.get(id=request.session['hid'])
    return render(request,"Hospital/Myprofile.html",{'hospital':hosdata})


def ChangePassword(request):
    if request.method=="POST":
        print(request.POST.get("txtpass"))
        print(request.session["hid"])
        hosdata=tbl_newhospital.objects.get(id=request.session["hid"],hospital_password=request.POST.get("txtpass"))
        cpass=request.POST.get("txtpass2")
        new=request.POST.get("txtpass1")
        if cpass==new:
            hosdata.hospital_password=request.POST.get("txtpass2")
            hosdata.save()
            return redirect('whospital:Myprofile')
        else:
            msg="Password Mismatch!!"
            return render(request,"Hospital/Changepassword.html",{'msg':msg})
    else:
        return render(request,"Hospital/Changepassword.html")


def EditProfile(request):
    hosdata=tbl_newhospital.objects.get(id=request.session["hid"])
    if request.method=="POST":
        hosdata.hospital_name=request.POST.get("txtname")
        hosdata.hospital_address=request.POST.get("txtadd")
        hosdata.hospital_contact=request.POST.get("txtcon")
        hosdata.hospital_email=request.POST.get("txtemail")
        hosdata.save()
        return redirect('whospital:Myprofile')
    else:
        return render(request,"Hospital/EditProfile.html",{'hospital':hosdata})

def complaint(request):
    comobj=tbl_complaint.objects.filter(hospital=request.session["hid"])
    if request.method=="POST":
        ho=tbl_newhospital.objects.get(id=request.session["hid"])
        tbl_complaint.objects.create(complaint_title=request.POST.get("txttitle"),
        complaint_com=request.POST.get("txtcom"),
        hospital=ho)
        return render(request, "Hospital/Complaint.html", {'data':comobj})
    else:
        return render(request, "Hospital/Complaint.html", {'data':comobj})


def delc(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect('whospital:Complaint')

def edtc(request,eid):
    cdata=tbl_complaint.objects.get(id=eid) 
    if request.method=="POST":
        cdata.complaint_title=request.POST.get("txttitle")
        cdata.complaint_com=request.POST.get("txtcom")
        cdata.save()
        return redirect('whospital:Complaint')
    else:
        return render(request,"Hospital/Complaint.html",{'datac':cdata})


def feedback(request):
    feedobj=tbl_feedback.objects.filter(hospital=request.session["hid"])
    if request.method=="POST":
        ho=tbl_newhospital.objects.get(id=request.session["hid"])
        tbl_feedback.objects.create(feedback_title=request.POST.get("txtfeed"),
        hospital=ho)
        return render(request, "Hospital/Feedback.html", {'cdata':feedobj})
    else:
        return render(request, "Hospital/Feedback.html", {'cdata':feedobj})

def delf(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect('whospital:feedback')

def edtf(request,eid):
    fdata=tbl_feedback.objects.get(id=eid) 
    if request.method=="POST":
        fdata.feedback_title=request.POST.get("txtfeed")
        fdata.save()
        return redirect('whospital:feedback')
    else:
        return render(request,"Hospital/Feedback.html",{'adata':fdata})


def gallery(request):
    ho=tbl_newhospital.objects.get(id=request.session["hid"])
    gobj=tbl_gallery.objects.filter(hospital=request.session["hid"])
    if request.method=="POST":
        tbl_gallery.objects.create(gallery_pic=request.FILES.get("txtfile"),
        hospital=ho)
        return render(request, "Hospital/AddGallery.html", {'data':gobj})
    else:
        return render(request, "Hospital/AddGallery.html", {'data':gobj})