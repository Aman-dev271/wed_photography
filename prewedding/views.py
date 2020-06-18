from django.shortcuts import render
from.models import pre_weding_booking, pre_wedding_reviews, pre_Wedding_photo_shoot, pre_wedding_main_slider,pre_wedding_coustomer_slider,testimonials_for_pre_wedding,about_us_page,logo,workdemo
from math import ceil

# Create your views here.

# for pre wedding webpage

def pre_wed_page(request):
	if (request.method == 'POST'):
		information = pre_weding_booking(
			name = request.POST['name'],
			email = request.POST['email'],
			address1 = request.POST['address'],
			city=request.POST['city'],
			state=request.POST['state'],
			zipcode=request.POST['zipcode'],
			telephone = request.POST['telephone'],
			make = request.POST['make1'],
			makeup = request.POST['make2'],
			date11 = request.POST['date1'],
			date21 = request.POST['date2'],


		)
		information.save()
	pre_wed = pre_weding_booking.objects.all()
	pre_wed_shoot = pre_Wedding_photo_shoot.objects.all()
	n = len(pre_wed_shoot)
	photo_range =n//1 + ceil((n/1)-(n//1))

	pre_wed_slider = pre_wedding_main_slider.objects.all()
	print(pre_wed_slider)
	n = len(pre_wed_slider)
	nSlides = n//1 + ceil((n/1)-(n//1))

	pre_wed_testimonial = testimonials_for_pre_wedding.objects.all()
	n = len(pre_wed_testimonial)
	range_pre_wed_testimonial = n//1+ceil((n/1)-(n//1))

	pre_wed_coust_slide =pre_wedding_coustomer_slider.objects.all()
	n = len(pre_wed_coust_slide)
	range_for_pre_wed_coustomer = n // 4 + ceil((n / 4) - (n // 4))
	demo = workdemo.objects.all()






	return render(request, 'pre_wed_page.html',{'title':'i am title of pre_wed_page','pre_wed':pre_wed,'pre_wed_shoot':pre_wed_shoot,'pre_wed_slider':pre_wed_slider,'slider_range':range(1,nSlides), 'no_of_slide':pre_wed_slider,'range_pre_wed_testimonial':(1,range_pre_wed_testimonial),'pre_wed_testimonial':pre_wed_testimonial,'pre_wed_coust_slide':pre_wed_coust_slide,'range_for_pre_wed_coustomer':range(1,range_for_pre_wed_coustomer),'demo':demo} )


# reviews on Pre-wedding
def pre_wedding_Review(request):
	if(request.method == 'POST'):
		data = pre_wedding_reviews(
			email = request.POST['email'],
			name = request.POST['name'],
			comment = request.POST['message'],

		)
		data.save()
	reviews = pre_wedding_reviews.objects.all()
	print(reviews)

	return render(request, 'pre_wedding_Review.html', {'title':'i am pre-wed_rev page','reviews':reviews})
def pre_Wedding_photo_shoot_view(request, myid):
	pre_wed_pic_view = pre_Wedding_photo_shoot.objects.filter(id=myid)
	dictionary = {'pre_wed_pic_view':pre_wed_pic_view[0], 'title':'title of picvirew'}
	return render(request, 'pre_wed_pic_view.html',dictionary)



def pre_wed_book_view(request):
	pre_wed_booking = pre_weding_booking.objects.all()
	dict = {'title':'i am the tableviews page' ,'pre_wed_booking':pre_wed_booking }
	return render(request, 'pre_wed_book_view.html',dict)


def pre_wed_shoot_view(request):
	pre_wed_shoot_pics = pre_Wedding_photo_shoot.objects.all()
	dict ={'title':'i am the pics page', 'pre_wed_shoot_pics':pre_wed_shoot_pics}
	return render(request, 'pre_wed_shoot_pics.html', dict)


def pre_wed_main_slide_show(request):
	pre_wed_main_slider = pre_wedding_main_slider.objects.all()
	dict = {'title':"i am mainslidepage",'pre_wed_main_slider':pre_wed_main_slider}
	return render(request, 'pre_wed_main_slider_pic_show.html',dict)
def pre_wed_main_slider_detail_view(request, myid):
	pre_wed_slider_detail =pre_wedding_main_slider.objects.filter(id=myid)
	dict = {'title':'iam detailviews','pre_wed_slider_detail':pre_wed_slider_detail[0]}
	return render(request,'pre_wed_main_slider_detail_view.html',dict)
def about_us_fun(request):
	about  =about_us_page.objects.all()
	ab = len(about)
	aboutrange = ab//1 + ceil((ab/1)-(ab//1))



	dict = {'title':'about us','about':about,'aboutrange':range(1,aboutrange)}
	return render(request, 'aboutus.html',dict)
def logo_pag(request):
	logo = logo.objects.all()
	return render(request,'layout.html',{'logo':logo})
def employee_detail_view(request, myid):
	aboutus_detail_views  = about_us_page.objects.filter(id=myid)
	dict = {'title':'i am aboutdetail','aboutus_detail_views':aboutus_detail_views[0]}
	return render(request, 'aboutusdetailview.html',dict)


def pre_wed_shoot_view_full(request,myid):
	pre_wed_shoot_pics_full = pre_Wedding_photo_shoot.objects.filter(id=myid)
	dict ={'title':'i am the pics page', 'pre_wed_shoot_pics_full':pre_wed_shoot_pics_full[0]}
	return render(request, 'pre_wed_shoot_pics_full.html', dict)
