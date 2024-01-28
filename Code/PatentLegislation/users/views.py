from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import  HttpResponse


# Create your views here.
from users.forms import userForm, UploadForm
from users.models import UserModel, UploadModel


def index(request):
    return render(request,'index.html')

def logout(request):
    return render(request,'index.html')

def userlogin(request):
    return render(request,"user/userlogin.html")

def userregister(request):
    if request.method=='POST':
        form1 = userForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "user/userlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userForm()
        return render(request,"user/userregister.html",{"form":form})


def userlogincheck(request):
    if request.method == "POST":
        email = request.POST.get('uname')
        pswd = request.POST.get('upasswd')
        print("Email = ", email, ' Password = ', pswd)
        try:
            check = UserModel.objects.get(email=email,passwd=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "Activated":
                request.session['id'] = check.id
                #request.session['name'] = check.name
                request.session['email'] = check.email
                print("User id At", check.id, status,check.email)
                return render(request, 'user/userpage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'user/userlogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Email id and password')
    return render(request, 'user/userlogin.html')


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("form saved")
            files = UploadModel.objects.filter(email=request.session['email'])
            return render(request, 'user/upload_list.html',{'files': files})
    else:
        data = {'email': request.session['email'],'category':'Computer Technology','title':'title','description':'Description','file':'python library with versions.txt','status':'waiting','adminstatus':'waiting'}
        form = UploadForm(data=data)
    return render(request, 'user/uploadfile.html', {'form': form})

def upload_list(request):
    files = UploadModel.objects.all()
    return render(request, 'user/upload_list.html', {'files': files})

def granted(request):
    email = request.session['email']
    sts = 'granted'
    dict = UploadModel.objects.filter(email=email)
    return render(request,'user/granted.html',{'object':dict})