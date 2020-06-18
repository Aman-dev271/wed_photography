from django.db import models

# Create your models here.
# data base for the wedding bookin form
class wedding_book(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    Address = models.TextField(max_length= 100)
    Address2 = models.TextField(max_length = 100, default= "")
    city  = models.CharField(max_length= 20)
    state = models.CharField(max_length = 20)
    telephone = models.CharField(max_length=10)
    zipcode = models.IntegerField()
    make = models.CharField(max_length= 40, default="")
    makeup = models.CharField(max_length = 40, default="")
    date1 = models.CharField(max_length = 40,default="")
    date2 = models.CharField(max_length=40,default="")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.email}"
    objects = models.Manager
# databse for  wedding page main slider
class wedding_main_slider(models.Model):
    heading = models.CharField(max_length=100 ,default=" ")
    caption2 = models.CharField(max_length=100,default=" ")
    image = models.ImageField(upload_to='wedding/wedding_main_slider',help_text="Size: 1920x570",default=" ")
    Camra = models.ImageField(upload_to='wedding/wedding_man_slider_pics',default=" ")
    name_of_camra =models.CharField(max_length=30,default=" ")
    camra_details = models.TextField(max_length=1000,default=" ")
    pub_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.heading}"
# databse for wedding shoot
class Wedding_photo_shoot(models.Model):
    images = models.ImageField(upload_to="wedding/wed_shoot")
    name = models.CharField(max_length= 30)
    desc = models.TextField(max_length=3000)
    camra = models.ImageField(upload_to="wedding/wed_shoot/camra",default=" ")
    nameof_camra = models.CharField(max_length=30,default=" ")
    detail_of_camra = models.TextField(max_length=4000,default=" ")
    created_at = models.DateTimeField(auto_now= True)
# databse for wedding page revies
class wedding_reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length= 20)
    comment = models.TextField(max_length=200)
    def __str__(self):
        return self.name
class wedding_coustomer_slider(models.Model):
    email = models.EmailField(max_length =20,default= "")
    name = models.CharField(max_length = 20,default= "")
    image = models.ImageField( upload_to="wedding/wed_coustemer_slider",default= "")
    phone = models.IntegerField()


    def __str__(self):
        return f"{self.name}"
class testimonials_for_wedding(models.Model):
    heading = models.CharField(max_length=20, default="")
    caption = models.TextField(max_length=2000,default="")
    image = models.ImageField(upload_to="wedding/image_testimonial_for_wedding",default="")
    name= models.CharField(max_length=200,default="")
    post = models.CharField(max_length=200,default="")
    pic = models.ImageField(upload_to="wedding/image_testimonial_for_wedding",default="")
    def __str__(self):
        return f"{self.heading}"
class contact_form(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(max_length = 30)
    phone = models.IntegerField()
    Question =models.TextField(max_length=1000)
    Answer = models.TextField(max_length = 1000)
    def __str__(self):
        return f"{self.name}"

class footer(models.Model):
    link = models.URLField(max_length=200)
    pic = models.ImageField(upload_to= 'wedding/footer_image')
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    color_class = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name}"



class vediolink(models.Model):
    link = models.URLField(max_length=300)
    desc=models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now= True)
    def __str__(self):
        return f"{self.link}"
