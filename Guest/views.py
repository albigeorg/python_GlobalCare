from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Hospital.models import *
from Doctor.models import *
from User.models import *



# Create your views here.

def mainpage(request):
    feed=tbl_feedback.objects.all()
    return render(request,"Guest/index.html",{'feed':feed})

def ajaxplace(request):
    disObj=tbl_district.objects.get(id=request.GET.get('DIST'))
    place=tbl_place.objects.filter(district=disObj)
    return render(request,"Guest/AjaxPlace.html",{'plc':place})

def newHospital(request):
    disObj=tbl_district.objects.all()
    typeObj=tbl_hospitaltype.objects.all()
    if request.method=="POST":
        hos=tbl_hospitaltype.objects.get(id=request.POST.get('sel_Hospital'))
        pl=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_newhospital.objects.create(hospital_name=request.POST.get("txtna"),
        hospital_email=request.POST.get("txtema"),
        hospital_contact=request.POST.get("txtcont"),
        hospital_address=request.POST.get("txtadd"),
        hospital_logo=request.FILES.get("filepic"),
        hospital_proof=request.FILES.get("filepro"),
        hospital_password=request.POST.get("txtpass"),
        hospitaltype=hos,
        place=pl,)
        return render(request,"Guest/NewHospital.html",{'disdata':disObj,'data':typeObj})    
    else:
        return render(request,"Guest/NewHospital.html",{'disdata':disObj,'data':typeObj})


def userregistration(request):
    uObj=tbl_district.objects.all()
    if request.method=="POST":
        pl=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),
        user_address=request.POST.get("txtadd"),
        user_email=request.POST.get("txtemail"),
        user_contact=request.POST.get("txtcon"),
        user_gender=request.POST.get("txtgen"),
        user_photo=request.FILES.get("filepic"),
        user_password=request.POST.get("txtpass"),
        place=pl,)
        return render(request,"Guest/UserRegistration.html",{'data':uObj})    
    else:
        return render(request,"Guest/UserRegistration.html",{'data':uObj})


def Login(request):
    if request.method=="POST":
        Email=request.POST.get('txtemail')
        Password=request.POST.get('txtpass')
        ucount=tbl_user.objects.filter(user_email=Email,user_password=Password).count()
        hcount=tbl_newhospital.objects.filter(hospital_email=Email,hospital_password=Password).count()
        concount=tbl_consultancy.objects.filter(consultancy_email=Email,consultancy_password=Password).count()
        dcount=tbl_doctor.objects.filter(doctor_email=Email,doctor_password=Password).count()
        acount=tbl_admin.objects.filter(admin_email=Email,admin_password=Password).count()
        if ucount > 0:
            userdata=tbl_user.objects.get(user_email=Email,user_password=Password)
            request.session['uid']=userdata.id
            return redirect('webuser:userhome')
        
        elif hcount > 0:
            hosdata=tbl_newhospital.objects.get(hospital_email=Email,hospital_password=Password)
            request.session['hid']=hosdata.id
            return redirect('whospital:Hoshome')

        elif concount > 0:
            condata=tbl_consultancy.objects.get(consultancy_email=Email,consultancy_password=Password)
            request.session['cid']=condata.id
            return redirect('webConsultancy:Consultancyhome')

        elif dcount > 0:
            docdata=tbl_doctor.objects.get(doctor_email=Email,doctor_password=Password)
            request.session["dname"]=docdata.doctor_name
            request.session['docid']=docdata.id
            return redirect('webDoctor:Doctorhome')

        elif acount > 0:
            adata=tbl_admin.objects.get(admin_email=Email,admin_password=Password)
            request.session['aid']=adata.id
            return redirect('webadmin:Adminhome')


        else:
            msg="Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'msg':msg})
    else:
        return render(request,"Guest/Login.html")

