from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from users.models import UserModel, UploadModel


def adminlogin(request):
    return render(request, "admins/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname == 'admin' and passwd == 'admin@2020':
            return render(request,"admins/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")

def viewusers(request):
    object = UserModel.objects.all()
    return render(request, "admins/viewusers.html", {"object": object})

def viewdata(request):
    object = UploadModel.objects.all()
    return render(request, "admins/viewdata.html", {"object": object})


def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        UserModel.objects.filter(id=uname).update(status=status)
        object=UserModel.objects.all()
        return render(request,"admins/viewusers.html",{"object":object})

def AdminAccept(request):
    id = request.GET.get('id')
    UploadModel.objects.filter(id=id).update(adminstatus='granted')
    object = UploadModel.objects.all()
    return render(request, "admins/viewdata.html", {"object": object})
def AdminDelete(request):
    id = request.GET.get('id')
    UploadModel.objects.filter(id=id).delete()
    object = UploadModel.objects.all()
    return render(request, "admins/viewdata.html", {"object": object})
