from django.shortcuts import render
from.models import wedding_book,wedding_main_slider, Wedding_photo_shoot, wedding_reviews,wedding_coustomer_slider, testimonials_for_wedding,contact_form,footer,vediolink
from math import ceil
# Create your views here.
def wedding_main_page(request):
	if (request.method == 'POST'):
		data=wedding_book(
			name = request.POST['name'],
			email = request.POST['email'],
			#Address = request.POST['address'],
			Address2 = request.POST['address1'],
			city = request.POST['city'],
			state = request.POST['state'],
			zipcode = request.POST['zipcode'],
			telephone = request.POST['telephone'],
			make = request.POST['make1'],
			makeup = request.POST['make2'],
			date1 = request.POST['date1'],
			date2 = request.POST['date2'],
		)
		data.save()


	wedding = wedding_book.objects.all()
	slider = wedding_main_slider.objects.all()
	n = len(slider)
	nSlides = n//1 + ceil((n/1)-(n//1))


	wed_shoot = Wedding_photo_shoot.objects.all()
	n = len(slider)
	nwed_shoot = n//4 + ceil((n/4)-(n//4))

	coustm_slider = wedding_coustomer_slider.objects.all()
	n = len(coustm_slider)
	coustm_range = n//1 + ceil((n/1)-(n//1))
	wed_testimonial = testimonials_for_wedding.objects.all()
	n = len(wed_testimonial)
	wed_testimonial_ranger = n//1 + ceil((n/1)-(n//1))
	vediodemo = vediolink.objects.all()
	return render(request, 'wedding_main_page.html',{'title':'i am title of home page','wed_book':wedding,'no_of_slides':nSlides,'range':range(1,nSlides),'slider':slider,'shoot_ranger':range(1,nwed_shoot),'no_of_shoot':nwed_shoot,'wed_shoot':wed_shoot,'coustm_range':range(1,coustm_range),'coustm_slider':coustm_slider, 'coustm_slider':coustm_slider,'wed_testimonial_ranger':range(1,wed_testimonial_ranger),'wed_testimonial':wed_testimonial,'nomber_of_testimonial_wed':wed_testimonial_ranger,"vediodemo":vediodemo})



	  #

# reviews on wedding
def wedding_Review(request):
	if(request.method == 'POST'):
		data = wedding_reviews(
			email = request.POST['email'],
			name = request.POST['name'],
			comment = request.POST['comment'],

		)
		data.save()
	reviews = wedding_reviews.objects.all()
	return render(request, 'wedding_Review.html', {'title':'i am wed_rev page','reviews':reviews})

def Wedding_photo_shoot_view(request, myid):
	wed_pic_view = Wedding_photo_shoot.objects.filter(id=myid)
	dictionary = {'wed_pic_view':wed_pic_view[0], 'title':'title of picvirew'}
	return render(request, 'wed_pic_view.html',dictionary)
def wed_book_view(request):
	wed_booking = wedding_book.objects.all()
	dict = {'title':'i am the tableviews page' ,'wed_booking':wed_booking }
	return render(request, 'wed_book_view.html',dict)

def wed_shoot_view(request):
	wed_shoot_pics = Wedding_photo_shoot.objects.all()
	dict ={'title':'i am the pics page', 'wed_shoot_pics':wed_shoot_pics}
	return render(request, 'wed_shoot_pics.html', dict)


def contacts(request):
	if(request.method == 'POST'):
		data = contact_form(
		name = request.POST['name'],
		email = request.POST['email'],
		phone = request.POST['phone'],
		Question = request.POST['Question'],
		)
		data.save()
	contacts = contact_form.objects.all()
	dict = {'title':'iam the contact page','contacts':contacts}

	return render(request, 'contact.html',dict)


def questionViews(request):
	contact = contact_form.objects.all()
	return render(request, 'contactviews.html',{'title':'i am questionviewpage','contact':contact})
def footer_data(request):
	footr = footer.objects.all()
	return render(request, 'base.html',{'footr':footr})


def wed_main_slider_photo_show(request):
	photo = wedding_main_slider.objects.all()
	dict = {'title':'i am title of slidershowpics','photo':photo}
	return render(request,'wed_main_slider_photo_show.html',dict)


def Wedding_main_slider_detail_view(request, myid):
	wed_main_slider_view = wedding_main_slider.objects.filter(id=myid)
	dictionary = {'wed_main_slider_view':wed_main_slider_view[0], 'title':'title of slidervirew'}
	return render(request, 'wed_main_slider_view.html',dictionary)

def wed_shoot_view_full_view(request,myid):
	wed_shoot_pics = Wedding_photo_shoot.objects.filter(id=myid)
	dict ={'title':'i am the pics page', 'wed_shoot_pics':wed_shoot_pics[0]}
	return render(request, 'wed_shoot_pics_full.html', dict)
