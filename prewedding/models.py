from django.db import models

# Create your models here.

# pre wedding models
class pre_weding_booking(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    address1 = models.TextField(max_length= 100)
    city  = models.CharField(max_length= 20)
    state = models.CharField(max_length = 20)
    telephone = models.CharField(max_length=10)
    zipcode = models.IntegerField()
    make = models.CharField(max_length= 40, default="")
    makeup = models.CharField(max_length = 40, default="")
    date11 = models.CharField(max_length = 40,default="")
    date21 = models.CharField(max_length=40,default="")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.email}"
    objects = models.Manager
# databse for pre-wedding page revies
class pre_wedding_reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length= 20)
    comment = models.TextField(max_length=200)
    def __str__(self):
        return self.name


# databse for Pre-wedding shoot
class pre_Wedding_photo_shoot(models.Model):
    photo = models.ImageField(upload_to="pre_wedding/pre_wed_shoot")
    name = models.CharField(max_length= 30)
    desc = models.TextField(max_length=3000)
    camra = models.ImageField(upload_to="pre_wedding/pre_wed_shoot/camra",default=" ")
    nameof_camra = models.CharField(max_length=30,default=" ")
    detail_of_camra = models.TextField(max_length=4000,default=" ")
    created_at = models.DateTimeField(auto_now= True)
# databse for  pre-wedding page main slider
class pre_wedding_main_slider(models.Model):
    heading = models.CharField(max_length=100 ,default=" ")
    caption2 = models.CharField(max_length=1000,default=" ")
    image = models.ImageField(upload_to='pre_wedding/pre_wedding_main_slider',help_text="Size: 1920x570")
    Camra = models.ImageField(upload_to='wedding/wedding_man_slider_pics',default=" ")
    name_of_camra =models.CharField(max_length=30,default=" ")
    camra_details = models.TextField(max_length=1000,default=" ")
    pub_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.heading}"
# database for pre wedding coustomers
class pre_wedding_coustomer_slider(models.Model):
    email = models.EmailField(max_length =20,default= "")
    name = models.CharField(max_length = 20,default= "")
    image = models.ImageField( upload_to="pre_wedding/pre_wed_coustemer_slider",default= "")
    phone = models.IntegerField(default= "")


    def __str__(self):
        return f"{self.name}"

# database for pre_wedding testimonials
class testimonials_for_pre_wedding(models.Model):
    heading = models.CharField(max_length=20, default="")
    caption = models.TextField(max_length=2000,default="")
    image = models.ImageField(upload_to="pre_wedding/pre_wed_image_testimonial_for_wedding",default="")
    name= models.CharField(max_length=200,default="")
    post = models.CharField(max_length=200,default="")
    pic = models.ImageField(upload_to="pre_wedding/image_testimonial_for_wedding",default="")
    def __str__(self):
        return f"{self.heading}"


class about_us_page(models.Model):
    name = models.CharField(max_length=40, default="")
    emailem = models.EmailField(max_length=20)
    phone = models.IntegerField()
    role = models.CharField(max_length=40, default="")
    image = models.ImageField(upload_to="pre_wedding/About_us", default="")
    work_experiance = models.TextField(max_length=3000, default="")
    content_for_website = models.TextField(max_length=10000, default="None")
    logo = models.ImageField(upload_to="pre_wedding/About_us_logo", default="None")
    maplink= models.URLField(max_length=400,default="")
    def __str__(self):
        return f"{self.name}"

class logo(models.Model):
    logo = models.ImageField(upload_to="pre_wedding/About_us_logo", default="")
class workdemo(models.Model):
    linkv = models.URLField(max_length=400)
    descv = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now= True)
    def __str__(self):
        return f"{self.linkv}"
