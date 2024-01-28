from django.db import models

# Create your models here.
class UserModel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    qualification = models.CharField(max_length=40)
    city = models.CharField(max_length=50)
    status = models.CharField(max_length=40,default="", editable=True)

    def __str__(self):
        return self.email
    class Meta:
        db_table='userregister'


class UploadModel(models.Model):
    #uuid = models.CharField(max_length=30)
    email = models.EmailField(default="", editable=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=400,unique=True)
    description = models.CharField(max_length=1000,blank=True)
    file = models.FileField(upload_to='files/pdfs/')
    status = models.CharField(max_length=600, default='waiting')
    adminstatus = models.CharField(max_length=600, default='waiting')

    def __str__(self):
        return self.category
    class Meta:
        db_table='Uploadfile'