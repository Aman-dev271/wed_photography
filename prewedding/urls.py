from django.urls import path
from.import views
urlpatterns = [
	path('pre_wed/',views.pre_wed_page, name='pre_wed_page'),
	path('pre_reviews/',views.pre_wedding_Review, name='pre_wedding_Review'),
	path('pre_Wedding_photo_shoot_view/<int:myid>',views.pre_Wedding_photo_shoot_view,name='pre_Wedding_photo_shoot_view'),
	path('pre_wed_book_view/',views.pre_wed_book_view,name='pre_wed_book_view'),
	path('pre_wed_shoot_view/',views.pre_wed_shoot_view,name='pre_wed_shoot_view'),
	path('pre_wed_main_slide_show/',views.pre_wed_main_slide_show,name='pre_wed_main_slide_show'),
	path('pre_wed_main_slider_detail_view/<int:myid>',views.pre_wed_main_slider_detail_view , name='pre_wed_main_slider_detail_view'),
	path('about_us_fun/',views.about_us_fun,name='about_us_fun'),
	path('employee_detail_view/<int:myid>',views.employee_detail_view,name='employee_detail_view'),
	path('pre_wed_shoot_view_full/<int:myid>',views.pre_wed_shoot_view_full,name='pre_wed_shoot_view_full'),


]
