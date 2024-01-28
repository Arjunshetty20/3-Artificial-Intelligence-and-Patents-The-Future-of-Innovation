from django.http import HttpResponse
from django.shortcuts import render

import speech_recognition as sr
import pyttsx3
# Create your views here.
from users.models import UploadModel


def copyrightadministered(request):
    return render(request, "copyright/copyrightadministered.html")

def copyrightloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname == 'copyright' and passwd == 'copyright':
            return render(request,"copyright/copyrightloginentered.html")
        else:
            return HttpResponse("invalied credentials")

def permissions(request):
    object = UploadModel.objects.all()
    return render(request, "copyright/userfiles.html",{'object':object})
import requests
def sendpermission(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        print(' ID is = ', id)
        data=UploadModel.objects.get(id=id)
        print(data.file,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        pd=UploadModel.objects.filter(status='granted')
        for x in pd:
            print(x.file,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        if pd:
            cosine_values = []
            for x in pd:
                # ================================================================
                print(data.file,x.file,"===============================================================")
                data1 = requests.get("http://localhost:8000/media/"+str(data.file)+"/")
                data2 = requests.get("http://localhost:8000/media/"+str(x.file)+"/")
                print(data.file,x.file,"=============================================@@@@@@@@@@@@@@@@@@@@@@@@@++++++")
                # =============================================================
                from nltk.corpus import stopwords
                from nltk.tokenize import word_tokenize

                # X = input("Enter first string: ").lower()
                # Y = input("Enter second string: ").lower()
                X = str(data1.content)
                Y = str(data2.content)

                # tokenization
                X_list = word_tokenize(X)
                Y_list = word_tokenize(Y)
                # print(X_list,Y_list,"===============================================================")
                # sw contains the list of stopwords
                sw = stopwords.words('english')
                l1 = [];
                l2 = []

                # remove stop words from the string
                X_set = {w for w in X_list if not w in sw}
                Y_set = {w for w in Y_list if not w in sw}

                # form a set containing keywords of both strings
                rvector = X_set.union(Y_set)
                for w in rvector:
                    if w in X_set:
                        l1.append(1)  # create a vector
                    else:
                        l1.append(0)
                    if w in Y_set:
                        l2.append(1)
                    else:
                        l2.append(0)
                c = 0

                # cosine formula
                for i in range(len(rvector)):
                    c += l1[i] * l2[i]
                cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
                cosine_values.append(cosine)

            print(cosine_values, "+++++++++++++++++++++++++++++++++++++++++++")
            total = 0
            for x in cosine_values:
                total += float(x)
            avg = (total / len(cosine_values))
            print(avg, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            if avg >= 0.1:
                #return render(request, 'user_home.html',
                           #   {"patent": "This ML Idea is Patented by someone else..try with your own idea..!"})
                print("ml idea existed")
                UploadModel.objects.filter(id=id).update(status='Existed')
            else:
                #UploadModel.objects.create(file=data.file)
                qs = UploadModel.objects.filter(id=id)
                print("sucessfully Patented,==========================================")
                UploadModel.objects.filter(id=id).update(status='granted')
               # qs.update(patent_status="Already Patended")
                #return render(request, 'user_home.html', {"patent": "sucessfully Patented"})
        else:
            #UploadModel.objects.create(file=data.file)
            qs = UploadModel.objects.filter(id=id)
            #qs.update(patent_status="Already Patended")
            print("sucessfully Patented")
            UploadModel.objects.filter(id=id).update(status='granted')
            #return render(request, 'user_home.html', {"patent": "sucessfully Patented"})

        #UploadModel.objects.filter(id=id).update(status='granted')
        object = UploadModel.objects.all()
        return render(request, 'copyright/userfiles.html', {'object': object})



def sendreject(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        print(' ID is = ', id)
        UploadModel.objects.filter(id=id).delete()
        object = UploadModel.objects.all()
        return render(request, 'copyright/userfiles.html', {'object': object})

